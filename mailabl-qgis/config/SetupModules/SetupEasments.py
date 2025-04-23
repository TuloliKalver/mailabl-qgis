from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.uic import loadUi
from types import MethodType
from PyQt5.QtWidgets import (
    QDialog, QFrame
    )


from ...KeelelisedMuutujad.modules import Module
from ...utils.ComboBoxHelperX import ComboBoxTools
from ...config.SetupModules.SetupMainLayers import QGIS_items
from ...config.settings import Filepaths, FilesByNames, StartupSettingsLoader
from ...config.settings_new import PluginSettings
from ...utils.ComboboxHelper import GetValuesFromComboBox
from ...KeelelisedMuutujad.messages import Headings, HoiatusTexts, EdukuseTexts
from ...utils.ComboboxHelper import ComboBoxHelper
from ...utils.messagesHelper import ModernMessageDialog
from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ...core.module.TypeManager import TypeModuleSetup
from ...app.MainMenuController import SetupController



pealkiri = Headings()
sisu = HoiatusTexts()
edu = EdukuseTexts()
combo_handler = ComboBoxHelper()


class SetupEasments:
    def __init__(self, parent) -> None:
        self.dialog = parent

    def load_easements_settings_widget(self):
        
        module = Module.EASEMENT
        ui_file_path = Filepaths.get_conf_widget(FilesByNames().easements_setup_ui)
        widget = loadUi(ui_file_path)

        widget.lblTitle.setText("Servituutide mooduli seadistamine...")

        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)

        animation = QPropertyAnimation(widget, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.start()

        SetupEasments.replace_frame(
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




        water_layer_name = PluginSettings.load_setting(
            module=Module.EASEMENT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.WATER        
            )

        sewer_layer_name = PluginSettings.load_setting(
            module=Module.EASEMENT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.SEWER
        )

        pressure_sewer_layer_name = PluginSettings.load_setting(
            module=Module.EASEMENT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.PRESSURE_SEWER
        )
        
        drainage_layer_name = PluginSettings.load_setting(
            module=Module.EASEMENT,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.DRAINAGE
        )

        QGIS_items.clear_and_add_layerNames_selected(widget.cbWater_Pipes, water_layer_name)
        QGIS_items.clear_and_add_layerNames_selected(widget.cbSewer_pipes, sewer_layer_name)
        QGIS_items.clear_and_add_layerNames_selected(widget.cbSewer_Pressure_pipes, pressure_sewer_layer_name)
        QGIS_items.clear_and_add_layerNames_selected(widget.cbDrainage_Pipes, drainage_layer_name)

        # set statuses
        combo_handler.populate_comboBox_smart(
            comboBox=widget.cmbPreferredEasementStatuses,
            module=module,
            context=self,
            preferred_items=False
        )

        # set types
        combo_handler.populate_comboBox_smart(
            comboBox=widget.cbcb_PreferredEasementTypes,
            module=module,
            context=self,
            preferred_items=True
        )

        # Connect buttons to dialog accept/reject
        widget.pbSave.clicked.connect(lambda: SetupEasments._handle_save(widget))
        widget.pbCancel.clicked.connect(lambda: SetupEasments._handle_cancel(widget))

        result = widget.exec_()

        if result == QDialog.Accepted:
            # ✅ Extract values *before* the dialog is deleted

            water_layer_name = ComboBoxTools.get_selected_item_name(widget.cbWater_Pipes)
            sewer_layer_name = ComboBoxTools.get_selected_item_name(widget.cbSewer_pipes)
            pressure_sewer_layer_name = ComboBoxTools.get_selected_item_name(widget.cbSewer_Pressure_pipes)
            drainage_layer_name = ComboBoxTools.get_selected_item_name(widget.cbDrainage_Pipes)

            status_name = GetValuesFromComboBox._get_selected_name_from_combobox(widget.cmbPreferredEasementStatuses)
            status_ids = GetValuesFromComboBox._get_selected_id_from_combobox(widget.cmbPreferredEasementStatuses)


            types_names = widget.cbcb_PreferredEasementTypes.checkedItems()
            types_ids = []
            comboBox = widget.cbcb_PreferredEasementTypes
            for index in range(comboBox.count()):
                if comboBox.itemCheckState(index) == Qt.Checked:
                    types_ids.append(comboBox.itemData(index))


            self.save_easements_settings( 
                                        types_names,
                                        types_ids, 
                                        status_name, 
                                        status_ids,
                                        water_layer_name,
                                        sewer_layer_name,
                                        pressure_sewer_layer_name,
                                        drainage_layer_name
                                        )
            controller = SetupController(self.dialog)
            controller.check_all_modules()

            widget.setAttribute(Qt.WA_DeleteOnClose)
            
            return True
        else:
            widget.setAttribute(Qt.WA_DeleteOnClose)
            return None


    def save_easements_settings(self, type_names, types_ids, status_name, status_ids, water_layer_name, sewer_layer_name, pressure_sewer_layer_name, drainage_layer_name):
        
        module = Module.EASEMENT
        
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
            key_type=PluginSettings.SUB_CONTEXT_IDs,
            value = status_ids
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
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.WATER,
            value = water_layer_name
        )

        PluginSettings.save_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.SEWER,
            value = sewer_layer_name
        )


        PluginSettings.save_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.PRESSURE_SEWER,
            value = pressure_sewer_layer_name
        )
        
        PluginSettings.save_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_LAYER,
            key_type=PluginSettings.DRAINAGE,
            value = drainage_layer_name
        )

        StartupSettingsLoader.startup_label_loader(self)




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


    @staticmethod
    def _handle_save(dialog):
        dialog.accept()

    @staticmethod
    def _handle_cancel(dialog):
        dialog.reject()


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

