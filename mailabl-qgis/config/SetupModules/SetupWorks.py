# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module,import-error


# Related Third-Party Imports
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPropertyAnimation
from types import MethodType
from PyQt5.QtWidgets import QDialog, QFrame

from PyQt5.uic import loadUi

from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame

from ..settings import Filepaths, FilesByNames, StartupSettingsLoader
from ..settings_new import PluginSettings


from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...KeelelisedMuutujad.modules import Module

from ...utils.ComboboxHelper import ComboBoxHelper
from ...utils.messagesHelper import ModernMessageDialog
from ...utils.ComboboxHelper import GetValuesFromComboBox
from .SetupMainLayers import QGIS_items

pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()
combo_handler = ComboBoxHelper()

class SetupWorks:

    def __init__(self, parent) -> None:
        self.dialog = parent

    def load_works_settings_widget(self):

        ui_file_path = Filepaths.get_conf_widget(FilesByNames().works_setup_ui)
        widget = loadUi(ui_file_path)
        
        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)

        # 🔄 Promote dragFrame to custom draggable logic
        drag_frame = widget.findChild(QFrame, "dragFrame")
        if drag_frame:
            # Inject drag behavior via method patching
            drag_frame.mousePressEvent = MethodType(DraggableFrame.mousePressEvent, drag_frame)
            drag_frame.mouseMoveEvent = MethodType(DraggableFrame.mouseMoveEvent, drag_frame)
            drag_frame._drag_pos = None
            drag_frame.setCursor(Qt.OpenHandCursor)   


        widget.lblTitle.setText("Kinnistute mooduli seadistamine")

        animation = QPropertyAnimation(widget, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.start()


        SetupWorks.replace_frame(
            widget, 
            "FrameMain", 
            lambda parent: AnimatedGradientBorderFrame(parent,
                                                        style=AnimatedGradientBorderFrame.INSPIRE)
        )
        
        cmbWorks = widget.cbWorksLayer
        works_layer = StartupSettingsLoader.load_works_settings()
        QGIS_items.clear_and_add_layerNames_selected(cmbWorks, works_layer)


        widget.pbSaveLayerSettings.clicked.connect(lambda: SetupWorks.on_save_button_clicked(widget))
        widget.pbCancelSave.clicked.connect(lambda: SetupWorks.on_cancel_button_clicked(widget))

        result = widget.exec_()

        if result == QDialog.Accepted:
            works_layer_name = GetValuesFromComboBox._get_selected_name_from_combobox(cmbWorks)

            PluginSettings.save_setting(
                module=Module.WORKS,
                context=PluginSettings.CONTEXT_PREFERRED,
                subcontext=PluginSettings.OPTION_LAYER,
                key_type=PluginSettings.WORKS_LAYER,
                value = works_layer_name
            )

            loader = StartupSettingsLoader(self)
            loader.startup_label_loader()

            # ✅ Apply selected style if we have one
            text = "Kõik sai salvestatud"
            heading = pealkiri.tubli
            ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
            # Additional logic if needed

    @staticmethod
    def on_save_button_clicked(widget):
        # Handle logic when the save button is clicked
        widget.accept()  # Close the dialog
    @staticmethod
    def on_cancel_button_clicked(widget):
        # Handle logic when the cancel button is clicked
        widget.reject()  # Close the dialog        



    @staticmethod
    def replace_frame(widget, old_name: str, style: str, new_frame_cls: type = AnimatedGradientBorderFrame, *args, **kwargs) -> QFrame:
        old = widget.findChild(QFrame, old_name)
        if old is None:
            raise ValueError(f"Could not find frame named '{old_name}'.")

        parent_layout = old.parentWidget().layout()
        index = parent_layout.indexOf(old)

        # Grab the layout *before* we detach
        inner_layout = old.layout()

        # Detach widget safely
        parent_layout.removeWidget(old)
        old.setParent(None)
        old.deleteLater()  # schedule safe cleanup

        # Create new styled frame
        new_frame = new_frame_cls(widget, style=style, *args, **kwargs)
        new_frame.setObjectName(old_name)

        if inner_layout:
            new_frame.setLayout(inner_layout)

        parent_layout.insertWidget(index, new_frame)

        return new_frame

        

class DraggableFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._drag_pos = None
        self.setCursor(Qt.OpenHandCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.window().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self._drag_pos:
            self.window().move(event.globalPos() - self._drag_pos)
            event.accept()


