# -*- coding: utf-8 -*-
from functools import partial
from PyQt5.uic import loadUi
from types import MethodType
from PyQt5.QtWidgets import (
    QDialog, QSizePolicy,
    QPushButton, QFrame
    )
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPropertyAnimation
from ...app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ...config.settings import Filepaths, FilesByNames

  
class DecisionDialogHelper:

    @staticmethod
    def ask_user(title: str, message: str, options: dict=None, parent=None, type = AnimatedGradientBorderFrame.MODERN):


        ui_file_path = Filepaths.get_decision_widget(FilesByNames.DecisionMaker_UI)
        #print(f"path: {ui_file_path}")
        # Load the UI from the specified .ui file
        Dialog = loadUi(ui_file_path)

        Dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        Dialog.setAttribute(Qt.WA_DeleteOnClose)



        drag_frame = Dialog.dragFrame
        drag_frame.mousePressEvent = MethodType(DraggableFrame.mousePressEvent, drag_frame)
        drag_frame.mouseMoveEvent = MethodType(DraggableFrame.mouseMoveEvent, drag_frame)
        drag_frame._drag_pos = None
        drag_frame.setCursor(Qt.OpenHandCursor)        

        lblTitle = Dialog.lblTitle
        buttonsLayout = Dialog.ButtonsLAyout.layout()        
        lblSolution = Dialog.lblSolution
        lblframe = Dialog.frame_2

        lblTitle.setText(title)
        lblSolution.setText(message)

        lblSolution.setWordWrap(True)
        lblSolution.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        lblSolution.setContentsMargins(10, 10, 10, 10)

        text_width, text_height = calculate_text_size(lblSolution, message)

        # 💡 Set lblSolution size directly
        lblSolution.setFixedSize(text_width + 20, text_height + 20)

        # 💡 Let lblframe grow (in case its layout constrains height)
        lblframe.setMinimumHeight(text_height + 40)
        lblframe.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)

        # 💡 Let dialog grow
        Dialog.resize(text_width + 60, text_height + 120)

        result = {"choice": None}
        
        if not options:
            options={"keep": "Jäta alles",
                    "delete": "Kustuta", 
                    "cancel": "Tühista"
                    }


        for key, label in options.items():
            button = QPushButton(label)
            button.setMinimumHeight(28)
            button.clicked.connect(partial(DecisionDialogHelper._handle_choice, Dialog, result, key))
            buttonsLayout.addWidget(button)
 

        animation = QPropertyAnimation(Dialog, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.start()

        DecisionDialogHelper.replace_frame(
            Dialog, 
            Dialog.FrameMain, 
            lambda parent: AnimatedGradientBorderFrame(parent,
                                                        style=type)
        )


        if Dialog.exec_() == QDialog.Accepted:
            choice = result["choice"]
            if choice == "delete":
                return True  # ✅ Only return True for delete
            if choice == "keep":
                return False     # ⛔️ Otherwise return False (you could return choice instead if needed)
            if choice == "cancel":
                return None          # 🚫 User closed the dialog or canceled



    @staticmethod
    def replace_frame(widget, old: QFrame, new_frame_cls: type, *args, **kwargs) -> QFrame:
        old_name = old.objectName()
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
    def _handle_choice(dialog, result_dict, key):
        result_dict["choice"] = key
        dialog.accept()




def calculate_text_size(label, text, max_width=500):
    font_metrics = QFontMetrics(label.font())
    # Use boundingRect to calculate size needed for wrapped text
    rect = font_metrics.boundingRect(0, 0, max_width, 1000, Qt.TextWordWrap, text)
    return rect.width(), rect.height()


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

