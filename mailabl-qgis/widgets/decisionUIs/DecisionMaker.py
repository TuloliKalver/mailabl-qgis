# -*- coding: utf-8 -*-
from functools import partial

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QHBoxLayout, 
    QPushButton, QWidget, QFrame, QGraphicsDropShadowEffect
    )
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation


class DecisionDialogHelper:

    def ask_user(title: str, message: str, options: dict=None, parent=None):

        Dialog = QDialog(parent)

        Dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)
        Dialog.setAttribute(Qt.WA_DeleteOnClose)


        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(20)
        shadow.setYOffset(4)
        shadow.setColor(QColor(9, 144, 143, 175))  # 100 = semi-transparent teal
        Dialog.setGraphicsEffect(shadow)


        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 125)
        Dialog.setStyleSheet("/* ====================================================== */\n"
            "/* 🎨 Global Theme - Base Colors, Background & Typography */\n"
            "/* ====================================================== */\n"
            "* {\n"
            "    border: transparent;\n"
            "    boreder-radius: 7px;\n"
            "    background-color: #1d252b; /* Updated background */\n"
            "    padding: 0;\n"
            "    margin: 0;\n"
            "    color: #ececf1; /* Brighter default text */\n"
            "}\n"
            "\n"
            "QWidget {\n"
            "\n"
            "    border: 1px solid #4d4d4d;\n"
            "    border-radius: 7px;\n"
            "    border-top-left-radius: 7px;     /* Rounded top-left corner */\n"
            "    border-top-right-radius: 7px;    /* Rounded top-right corner */\n"
            "    border-right-radius: 7px;        /* No rounding on right side */\n"
            "    border-left-radius: 7px;    \n"
            "    background-color: rgba(29, 37, 43, 0.85);  /* 10% transparency */\n"
            "}\n"
            "\n"
            "QLabel, QLabel:focus, QLabel:hover {\n"
            "    border: None;\n"
            "    color: #ececf1; /* Brighter default text */\n"
            "}\n"
            "\n"
            "/* 🔘 QPushButton Styling */\n"

            "QPushButton {\n"
            "    padding: 4px 8px;\n"
            "    text-align: center;\n"
            "    border-radius: 5px;\n"
            "    background-color: rgb(9, 144, 143);\n"
            "    border: 1px solid #565869;\n"
            "    color: #ffffff; /* Brighter text */\n"
            "}\n"
            "\n"

            "QPushButton:hover {\n"
            "    background-color: #5c5d6e;\n"
            "    border: 1px solid #acacbe;\n"
            "    color: #ffffff;\n"
            "}\n"
            "\n"

            "QPushButton:pressed {\n"
            "    background-color: #2d2e3a;\n"
            "    border: 1px solid #8e8ea0;\n"
            "    color: #ececf1; /* Brighter default text */    \n"
            "}\n"
            "\n"

            "QPushButton:disabled {\n"
            "    background-color: #24252e;\n"
            "    border: 1px dashed rgba(120, 120, 130, 0.5);\n"
            "    color: rgba(200, 200, 210, 0.3);   \n"
            "}\n"
            "\n"

            "QPushButton:focus {\n"
            "    border: 1px solid;\n"
            "    border-left-color: qradialgradient(spread:pad, cx:0, cy:0.347273, radius:0.826, fx:0.453364, fy:0.097,\n"
            "        stop:0.125 rgba(9, 144, 143, 88), stop:1 rgba(46, 47, 56, 76));\n"
            "    border-top-color: qradialgradient(spread:pad, cx:0, cy:0.347273, radius:0.826, fx:0.453364, fy:0.097,\n"
            "        stop:0.125 rgba(9, 144, 143, 88), stop:1 rgba(46, 47, 56, 76));\n"
            "    border-bottom-color: qradialgradient(spread:pad, cx:1, cy:0.728, radius:0.826, fx:0.498455, fy:0.95,\n"
            "        stop:0.125 rgba(9, 144, 143, 88), stop:1 rgba(46, 47, 56, 76));\n"
            "    border-right-color: qradialgradient(spread:pad, cx:1, cy:0.728, radius:0.826, fx:0.498455, fy:0.95,\n"
            "        stop:0.125 rgba(9, 144, 143, 88), stop:1 rgba(46, 47, 56, 76));\n"
            "    background-color: rgb(31, 93, 92);\n"
            "    color: #ececf1; /* Brighter default text */\n"
            "}\n"
            "\n"

            "#dragFrame {\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "    border-bottom-right-radius: 0px;\n"
            "    border-bottom-left-radius: 0px;\n"
            "    background-color: rgba(9, 144, 143, 1.0);\n"
            "    cursor: move;\n"
            "    color: #ececf1; /* Brighter default text */\n"
            "}\n"
            "\n"

            "#frame{\n"
            "     border-top-right-radius: 0px;\n"
            "    border-top-left-radius: 0px\n"
            "}\n"
            "\n"

            "#buttonsContainer{\n"
            "    background: None;\n"
            "    border: None\n"
            "}\n"

            "\n"
            "QLabel{\n"
            "    background: None;\n"
            "    }\n"
            "")
        mainLayout = QVBoxLayout(Dialog)
        mainLayout.setContentsMargins(0, 0, 0, 30)
        mainLayout.setSpacing(0)
        mainLayout.setObjectName("mainLayout")
        

        dragFrame = DraggableFrame(Dialog)
        dragFrame.setMinimumSize(QSize(0, 25))
        dragFrame.setMaximumSize(QSize(1000000, 25))
        dragFrame.setFrameShape(QFrame.StyledPanel)
        dragFrame.setFrameShadow(QFrame.Raised)
        dragFrame.setObjectName("dragFrame")
        mainLayout.addWidget(dragFrame)

        
        titleLayout = QHBoxLayout(dragFrame)
        titleLayout.setContentsMargins(20, 0, 0, 0)
        titleLayout.setSpacing(0)
        titleLayout.setObjectName("titleLayout")
        
        lblTitle = QLabel(dragFrame)
        lblTitle.setObjectName("lblTitle")
        titleLayout.addWidget(lblTitle)
        
        
        frame = QFrame(Dialog)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setObjectName("frame")

        contentLayout = QVBoxLayout(frame)
        contentLayout.setContentsMargins(40, 20, 40, 20)
        contentLayout.setSpacing(20)
        contentLayout.setObjectName("contentLayout")
        
        lblSolution = QLabel(frame)
        lblSolution.setAlignment(Qt.AlignCenter)
        lblSolution.setObjectName("lblSolution")
        contentLayout.addWidget(lblSolution)
        mainLayout.addWidget(frame)

        # Create a wrapper layout that holds buttonsContainer centered
        centerWrapper = QHBoxLayout()
        centerWrapper.setContentsMargins(0, 0, 0, 0)
        centerWrapper.setAlignment(Qt.AlignHCenter)  # ⬅️ Center horizontally

        buttonsContainer = QWidget(Dialog)
        buttonsContainer.setObjectName("buttonsContainer")

        buttonsLayout = QHBoxLayout(buttonsContainer)        
        buttonsContainer.setLayout(buttonsLayout)
        buttonsLayout.setContentsMargins(0, 0, 0, 0)
        # Add stretch spacers before and after the buttons
        
        buttonsLayout.setSpacing(10)  # left spacer
        
        contentLayout.addWidget(buttonsContainer)

        lblTitle.setText(title)
        lblSolution.setText(message)

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

            # Add buttonsContainer to centerWrapper
            centerWrapper.addWidget(buttonsContainer)

            # Add wrapper to the main layout (which was `verticalLayout` or `contentLayout`)
            contentLayout.addLayout(centerWrapper)


        animation = QPropertyAnimation(Dialog, b"windowOpacity")
        animation.setDuration(300)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.start()

        if Dialog.exec_() == QDialog.Accepted:
            choice = result["choice"]
            if choice == "delete":
                return True  # ✅ Only return True for delete
            return False     # ⛔️ Otherwise return False (you could return choice instead if needed)
        return None          # 🚫 User closed the dialog or canceled


    @staticmethod
    def _handle_choice(dialog, result_dict, key):
        result_dict["choice"] = key
        dialog.accept()


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
