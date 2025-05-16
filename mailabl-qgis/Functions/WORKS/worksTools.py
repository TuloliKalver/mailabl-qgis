import os
import re

from PyQt5.QtCore import Qt

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
        
        label = widget.lblHeadingValue

        if label:
            address = properties_feature[Katastriyksus.l_aadress]
            asum = properties_feature[Katastriyksus.ay_nimi]
            full_address = address + ", " + asum
            label.setText(full_address)
        else:
            print("⚠️ QLabel 'lblHeadingValue' not found in the UI.")
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
        worksTools.setup_combobox_label_update(comboBox, label, prefix_text=full_address, lineEdit=lineEdit)

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