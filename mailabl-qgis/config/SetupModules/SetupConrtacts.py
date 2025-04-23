from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.uic import loadUi
from types import MethodType
from PyQt5.QtWidgets import (
    QDialog, QFrame
    )



from ...KeelelisedMuutujad.modules import Module
from ...config.settings import Filepaths, FilesByNames, SettingsDataSaveAndLoad, StartupSettingsLoader
from ...utils.ComboboxHelper import GetValuesFromComboBox
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...utils.ComboboxHelper import ComboBoxHelper
from ...utils.messagesHelper import ModernMessageDialog
from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ...config.settings_new import PluginSettings
from ...app.MainMenuController import SetupController



pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()
combo_handler = ComboBoxHelper()

class SetupConrtacts:
    def __init__(self, parent) -> None:
        self.dialog = parent

    def load_contract_settings_widget(self):

        module = Module.CONTRACT
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().contracts_setup_ui)

        widget = loadUi(ui_file_path)

        save_button = widget.pbSave
        cancel_button = widget.pbCancel

        widget.lblTitle.setText("Lepingute mooduli seadistamine...")

        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)

        animation = QPropertyAnimation(widget, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.start()

        SetupConrtacts.replace_frame(
            widget, 
            "FrameMain", 
            lambda parent: AnimatedGradientBorderFrame(parent,
                                                        style=AnimatedGradientBorderFrame.MODERN)
        )

        # 🔄 Promote dragFrame to custom draggable logic
        drag_frame = widget.dragFrame
        if drag_frame:
            # Inject drag behavior via method patching
            drag_frame.mousePressEvent = MethodType(DraggableFrame.mousePressEvent, drag_frame)
            drag_frame.mouseMoveEvent = MethodType(DraggableFrame.mouseMoveEvent, drag_frame)
            drag_frame._drag_pos = None
            drag_frame.setCursor(Qt.OpenHandCursor)

        
        statuses_combo_box = widget.cmbPreferredContractStatuses
        combo_handler.populate_comboBox_smart(
            comboBox=statuses_combo_box,
            module=module,
            context=self,
            preferred_items=False
        )

        types_combo_box = widget.cbcb_PreferredContractTypes
        combo_handler.populate_comboBox_smart(
            comboBox=types_combo_box,
            module=module,
            context=self,
            preferred_items=True
        )

        # Connect signals to functions
        save_button.clicked.connect(lambda: SetupConrtacts._handle_save(widget))
        cancel_button.clicked.connect(lambda: SetupConrtacts._handle_cancel(widget))

        result = widget.exec_()

        if result == QDialog.Accepted:
            status_value_name = GetValuesFromComboBox._get_selected_name_from_combobox(statuses_combo_box)
            status_value_ids = GetValuesFromComboBox._get_selected_id_from_combobox(statuses_combo_box)
            
            types_ids = []
            types_names = types_combo_box.checkedItems()
            for index in range(types_combo_box.count()):
                if types_combo_box.itemCheckState(index) == Qt.Checked:
                    types_ids.append(types_combo_box.itemData(index))

            self.save_contract_settings(types_names, types_ids, 
                                        status_value_name, status_value_ids
                                        )


            controller = SetupController(self.dialog)
            controller.check_all_modules()

            widget.setAttribute(Qt.WA_DeleteOnClose)
            
            return True
        else:
            widget.setAttribute(Qt.WA_DeleteOnClose)
            return None


    @staticmethod
    def _handle_save(dialog):
        dialog.accept()

    @staticmethod
    def _handle_cancel(dialog):
        text = sisu.kasutaja_peatas_protsessi
        heading = pealkiri.warningSimple
        ModernMessageDialog.Info_messages_modern_REPLACE_WITH_DECISIONMAKER(heading, text)
        dialog.reject()



    @staticmethod
    def replace_frame(widget, old_name: str, new_frame_cls: type, *args, **kwargs) -> QFrame:
        old = widget.findChild(QFrame, old_name)
        if old is None:
            raise ValueError(f"Could not find frame named '{old_name}'.")

        layout = old.parentWidget().layout()
        index = layout.indexOf(old)
        layout.removeWidget(old)
        old.deleteLater()

        new_frame = new_frame_cls(widget, *args, **kwargs)
        new_frame.setObjectName(old_name)
        new_frame.setLayout(old.layout())  # reuse inner layout if needed
        layout.insertWidget(index, new_frame)
        return new_frame


    def save_contract_settings(self, type_names, types_ids, status_name, status_ids):
        module = Module.CONTRACT
        
        PluginSettings.save_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_TYPE,
            key_type=PluginSettings.SUB_CONTEXT_NAME,
            value = type_names
            )

        PluginSettings.save_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_TYPE,
            key_type=PluginSettings.SUB_CONTEXT_IDs,
            value = types_ids
            )
        
        PluginSettings.save_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_STATUS,
            key_type=PluginSettings.SUB_CONTEXT_NAME,
            value = status_name
            )

        PluginSettings.save_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_STATUS,
            key_type=PluginSettings.SUB_CONTEXT_IDs,
            value = status_ids
            )

        StartupSettingsLoader.startup_label_loader(self)



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


