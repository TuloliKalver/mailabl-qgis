import os
import re

from PyQt5.QtCore import Qt
from datetime import datetime

from types import MethodType
from PyQt5.QtWidgets import (
    QDialog,QCheckBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QTextEdit, QVBoxLayout, QGroupBox
)

from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ...config.settings import Filepaths, FilesByNames
from ...config.SetupModules.AsBuitSettings import AsBuiltDrawings, DraggableFrame
from ...config.settings_new import PluginSettings

from PyQt5.QtCore import QPropertyAnimation

from ...KeelelisedMuutujad.Maa_amet_fields import Katastriyksus
from ...KeelelisedMuutujad.modules import Module

from ...utils.ComboboxHelper import ComboBoxHelper

from ...queries.python.users.user import UserSettings
from ...utils.TableUtilys.FlagIconHelper import FlagIconHelper

combo_handler = ComboBoxHelper()


class worksTools():

    def __init__(self, parent) -> None:
        self.dialog = parent
        
    def load_worksTools(self, feature, properties_feature):
        widget_name = Filepaths._get_widget_name(FilesByNames().worksTools_UI)
        widget = Filepaths.load_ui_file(widget_name)
        
        widget.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool) #| Qt.WindowStaysOnTopHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)


        drag_frame = widget.findChild(QFrame, "dragFrame")
        if drag_frame:
            # Inject drag behavior via method patching
            drag_frame.mousePressEvent = MethodType(DraggableFrame.mousePressEvent, drag_frame)
            drag_frame.mouseMoveEvent = MethodType(DraggableFrame.mouseMoveEvent, drag_frame)
            drag_frame._drag_pos = None
            drag_frame.setCursor(Qt.OpenHandCursor)   

        widget.adjustSize()


        widget.pbSave.clicked.connect(lambda: worksTools._handle_save(widget))
        widget.pbCancel.clicked.connect(lambda: worksTools._handle_cancel(widget))

        animation = QPropertyAnimation(widget, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.start()

        AsBuiltDrawings.replace_frame(
            widget,
            "FrameMain",
            style=AnimatedGradientBorderFrame.GENTLEMAN,
        )
        
        worksTools.definedata(widget, feature, properties_feature)



        result = widget.exec_()
        if result == QDialog.Accepted:
            print("Dialog accepted")


            # Set default fields
            feature.setAttribute("datetime", datetime.now().strftime("%Y-%m-%d %H:%M"))
            feature.setAttribute("created_at", datetime.now().isoformat())
            feature.setAttribute("updated_at", datetime.now().isoformat())
                        
            description = widget.worksDesc.toPlainText()
            feature.setAttribute("description", description)

            responsible = widget.cmbResponsible.currentText().strip()
            if not responsible:
                responsible = "Määramata"
            feature.setAttribute("responsible_team", responsible)
            index = widget.cmbResponsible.currentIndex()
            responsible_id = widget.cmbResponsible.itemData(index, Qt.UserRole)

            # For multi-user combobox
            selected_user_ids = []
            for i in range(widget.mcbxUsers.count()):
                if widget.mcbxUsers.itemData(i, Qt.CheckStateRole) == Qt.Checked:
                    selected_user_ids.append(widget.mcbxUsers.itemData(i, Qt.UserRole))

            print(f"selected_user_ids: {selected_user_ids}")
            print(f"responsible_id: {responsible_id}")


            types =widget.workTypes.currentText().strip()
            feature.setAttribute("type", types)

            index = widget.cmbPriority.currentIndex()
            selected_enum = widget.cmbPriority.itemData(index, Qt.UserRole)

            feature.setAttribute("priority", selected_enum)
    
            feature.setAttribute("active", True)        

            widget.setAttribute(Qt.WA_DeleteOnClose)
            
            return True
        else:
            print("Dialog rejected")
            widget.setAttribute(Qt.WA_DeleteOnClose)
            return False

    @staticmethod
    def _handle_save(dialog):
        dialog.accept()

    @staticmethod
    def _handle_cancel(dialog):
        dialog.reject()

    def definedata(widget, feature, properties_feature):
        
        task_label = widget.lblHeadingValue
        if task_label:
            address = properties_feature[Katastriyksus.l_aadress]
            asum = properties_feature[Katastriyksus.ay_nimi]
            full_address = address + ", " + asum
            task_label.setText(full_address)
        else:
            print("⚠️ QLabel 'lblHeadingValue' not found in the UI.")


        cmbPriority = widget.cmbPriority

        # Mapping from enum to Estonian display
        priority_map = {
            "URGENT": "Kiire",
            "HIGH": "Kõrge",
            "MEDIUM": "Keskmine",
            "LOW": "Madal"
        }

        # Fill combobox
        for enum_value, display_name in priority_map.items():
            icon = FlagIconHelper.generate_icon(priority=enum_value, size=18)
            cmbPriority.addItem(icon, display_name)
            # Store the original enum as UserRole data
            cmbPriority.setItemData(cmbPriority.count() - 1, enum_value, Qt.UserRole)
            
        lblStartTime = widget.lblStartTime
        lblStartDate = widget.lblStartDate

        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M")

        lblStartDate.setText(date)
        lblStartTime.setText(time)


        users =UserSettings.load_users()
        print(f"users: {users}")
        cmbResponsible = widget.cmbResponsible
        cmbUsers = widget.mcbxUsers

        cmbResponsible.clear()
        for label, user_id in users:
            cmbResponsible.addItem(label)
            cmbResponsible.setItemData(cmbResponsible.count() - 1, user_id, Qt.UserRole)

        cmbUsers.clear()
        for label, user_id in users:
            cmbUsers.addItem(label)
            index = cmbUsers.findText(label)
            cmbUsers.setItemData(index, user_id, Qt.UserRole)  # Store user ID for later
            cmbUsers.setItemData(index, Qt.Unchecked, Qt.CheckStateRole)


        comboBox=widget.workTypes
        module=Module.WORKS

        group_values = PluginSettings.load_setting(
            module=module,
            context=PluginSettings.CONTEXT_PREFERRED,
            subcontext=PluginSettings.OPTION_TYPE,
            key_type=PluginSettings.SUB_CONTEXT_TYPE_GROUP,
            text_fomated=True
            )
        
        combo_handler.refresh_combo_box_with_group_values(comboBox, module, group_values)

        lineEdit = widget.worksTitleadition
        worksTools.setup_combobox_label_update(comboBox, task_label, prefix_text=full_address, lineEdit=lineEdit)

    @staticmethod
    def setup_combobox_label_update(comboBox, label, prefix_text="", lineEdit=None):
        def update_label():
            type_text = comboBox.currentText()
            addition = lineEdit.text().strip() if lineEdit else ""
            if addition:
                label.setText(f"{prefix_text} - {type_text} - {addition}")
            else:
                label.setText(f"{prefix_text} - {type_text}")

        comboBox.currentIndexChanged.connect(lambda _: update_label())
        if lineEdit:
            lineEdit.textChanged.connect(lambda _: update_label())

        # Initialize the label immediately
        update_label()