from functools import partial

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QHBoxLayout, 
    QPushButton, QWidget, QFrame, QGraphicsDropShadowEffect
    )
from PyQt5.QtCore import Qt



class DecisionDialogHelper:
    @staticmethod
    def ask_user(title: str, message: str, options: dict, parent=None):
        """
        Show a universal decision dialog.

        :param title: Window title.
        :param message: Main message text.
        :param options: Dict mapping return keys to button labels.
                        Example: { "yes": "Yes", "no": "No", "cancel": "Cancel" }
        :param parent: Optional parent widget.
        :return: Selected option key (e.g. "yes", "no", "cancel")
        """
        dialog = QDialog(parent)
        dialog.setWindowTitle(title)
        dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        dialog.setAttribute(Qt.WA_TranslucentBackground)
        dialog.setAttribute(Qt.WA_DeleteOnClose)

        # Outer transparent layout (fills dialog)
        outer_layout = QVBoxLayout(dialog)
        outer_layout.setContentsMargins(0, 0, 0, 0)


        # 🟦 Main container frame with white background and rounded corners
        main_frame = QFrame()
        main_frame.setObjectName("mainFrame")
        main_frame.setStyleSheet("""
            #mainFrame {
                background-color: rgba(45, 55, 65, 0.95);
                border-radius: 10px;
            }
            QLabel {
                font-size: 14px;
            }
            QPushButton {
                padding: 6px 12px;
                border-radius: 4px;
            }
        """)


        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(Qt.black)
        main_frame.setGraphicsEffect(shadow)



        inner_layout = QVBoxLayout(main_frame)
        inner_layout.setContentsMargins(1, 1, 1, 1)  # 🟩 Only 1px padding all around
        inner_layout.setSpacing(0)                  # 🟩 No spacing between widgets



        styled_drag_container = QFrame()
        styled_drag_container.setObjectName("dragFrame")  # This is what QSS will style
        styled_drag_container.setStyleSheet("""
            #dragFrame {
                border-top-left-radius: 7px;
                border-top-right-radius: 7px;
                border-bottom-left-radius: 0px;
                border-bottom-right-radius: 0px;
                background-color: rgba(9, 144, 143, 1.0);
                min-height: 32px;
                padding-left: 6px;
                padding-right: 6px;
            }
        """)


        drag_inner = DraggableFrame(dialog)
        drag_layout = QHBoxLayout(styled_drag_container)
        drag_layout.setContentsMargins(0, 0, 0, 0)

        drag_layout.addWidget(drag_inner)
        inner_layout.addWidget(styled_drag_container)

        
        # 🔤 Message label
        label = QLabel(message)
        label.setWordWrap(True)
        inner_layout.addWidget(label)

        # ✅ Buttons row
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(6)                  # 🟩 No spacing between widgets
        inner_layout.setContentsMargins(10, 10, 5, 5)  # 🟩 Only 1px padding all around


        buttons = {}

        result = {"choice": None}

        for key, label_text in options.items():
            button = QPushButton(label_text)
            buttons_layout.addWidget(button)
            buttons[key] = button



        # Connect button handlers
        for key, button in buttons.items():
            button.clicked.connect(partial(DecisionDialogHelper._handle_choice, dialog, result, key))

        inner_layout.addLayout(buttons_layout)

        # Add fully-styled main frame to dialog layout
        outer_layout.addWidget(main_frame)

        if dialog.exec_() == QDialog.Accepted:
            choice = result["choice"]
            if choice == "delete":
                return True  # ✅ Only return True for delete
            return False     # ⛔️ Otherwise return False (you could return choice instead if needed)
        return None          # 🚫 User closed the dialog or canceled

    @staticmethod
    def _handle_choice(dialog, result_dict, key):
        result_dict["choice"] = key
        dialog.accept()

class DraggableFrame(QWidget):
    def __init__(self, parent=None, title: str = ""):
        super().__init__(parent)
        self._drag_pos = None
        self.setCursor(Qt.OpenHandCursor)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(6, 0, 6, 0)  # Adjust padding as needed
        layout.setSpacing(4)

        self.title_label = QLabel(title)
        self.title_label.setObjectName("titleLable")
        self.title_label.setStyleSheet("""
            QLabel#titleLable {
                background: transparent;
                color: #ececf1;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        self.title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        layout.addWidget(self.title_label)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.window().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self._drag_pos:
            self.window().move(event.globalPos() - self._drag_pos)
            event.accept()
