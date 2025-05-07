# pylint: disable=missing-class-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=no-name-in-module,import-error


# Related Third-Party Imports
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPropertyAnimation
from types import MethodType
from qgis.utils import iface
from qgis.core import QgsMapLayer, QgsProject
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QListView, QComboBox, QDialog, QFrame

from PyQt5.uic import loadUi

from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame

from ..settings import Filepaths, FilesByNames, SettingsDataSaveAndLoad, StartupSettingsLoader

from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...utils.ComboboxHelper import ComboBoxHelper
from ...utils.messagesHelper import ModernMessageDialog


pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()
combo_handler = ComboBoxHelper()

class SetupCadastralLayers:
    selected_style_path = None  # class-level variable, optional

    def __init__(self, parent) -> None:
        self.dialog = parent

    def load_layer_settings_widget(self):

        ui_file_path = Filepaths.get_conf_widget(FilesByNames().layer_setup_ui)
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



        SetupCadastralLayers.replace_frame(
            widget, 
            "FrameMain", 
            lambda parent: AnimatedGradientBorderFrame(parent,
                                                        style=AnimatedGradientBorderFrame.INSPIRE)
        )
        
        cmbCurrent_Layer = widget.cbCurrent_Cadastral
        button = widget.pbChangLayerStyle


        layer = SettingsDataSaveAndLoad.load_target_cadastral_name(self)
        print(f"Loaded layer from settings: {layer}")
        QGIS_items.clear_and_add_layerNames_selected(cmbCurrent_Layer, layer)

        button.clicked.connect(lambda: SetupCadastralLayers.change_layer_style(widget))

        widget.pbSaveLayerSettings.clicked.connect(lambda: SetupCadastralLayers.on_save_button_clicked(widget))
        widget.pbCancelSave.clicked.connect(lambda: SetupCadastralLayers.on_cancel_button_clicked(widget))

        result = widget.exec_()

        if result == QDialog.Accepted:
            input_value = cmbCurrent_Layer.currentText()
            SettingsDataSaveAndLoad.save_target_cadastral(self,input_value)  #, target_value)
            loader = StartupSettingsLoader(self)
            loader.startup_label_loader()

            # ✅ Apply selected style if we have one
            if SetupCadastralLayers.selected_style_path:
                print(f"Applying style: {SetupCadastralLayers.selected_style_path}")
                layer = QgsProject.instance().mapLayersByName(input_value)
                if layer:
                    layer_obj = layer[0]
                    success = layer_obj.loadNamedStyle(SetupCadastralLayers.selected_style_path)

                    if success[0]:
                        layer_obj.reload()  # 🔧 Force full style reload
                        layer_obj.triggerRepaint()
                        iface.mapCanvas().refresh()
                        print(f"✅ Applied style to layer '{input_value}'")
                    else:
                        print(f"⚠️ Failed to apply style: {success[1]}")
                else:
                    print(f"❌ Layer '{input_value}' not found in map.")                
                SetupCadastralLayers.selected_style_path = None
            
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
    def change_layer_style(widget) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            widget,
            "Vali stiilifail",
            "",  # starting directory
            "QGIS Layer Style (*.qml);;All Files (*)"
        )

        if file_path:
            print(f"✅ Style file selected: {file_path}")
            SetupCadastralLayers.selected_style_path = file_path
            # Optionally call another method to apply it now
        else:
            print("⚠️ User canceled style file selection.")


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





class QGIS_items:
    def __init__(self):
        pass
    #//TODO: refactor this class into a ComboBox helper module
    def clear_and_add_layerNames(combo_box: QComboBox):
        combo_box.clear()
        layer_names = QGIS_items._get_sorted_layer_names()
        combo_box.addItems(layer_names)
        combo_box.setView(QListView())

    def clear_and_add_layerNames_selected(combo_box: QComboBox, layer_name: str = None):
        combo_box.clear()
        layer_names = QGIS_items._get_sorted_layer_names()
        combo_box.addItems(layer_names)   
        # Set the current text of the combo box to the layer name if it exists
        if layer_name:
            combo_box.setCurrentText(layer_name)
        combo_box.setView(QListView())
    
    @staticmethod
    def _get_sorted_layer_names():
        excluded_group = 'Imporditavad kinnistud' 
        layers = []
        for layer_id, layer in QgsProject.instance().mapLayers().items():
            if isinstance(layer, QgsMapLayer) and layer.type() == QgsMapLayer.VectorLayer:
                layer_node = QgsProject.instance().layerTreeRoot().findLayer(layer_id)
                if layer_node is not None and layer_node.parent() is not None and layer_node.parent().name() != excluded_group:
                    layers.append(layer)

        # Get the names of the layers
        layer_names = [layer.name() for layer in layers]

        # Sort layer names alphabetically
        sorted_layer_names = sorted(layer_names)
        return sorted_layer_names
        

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


