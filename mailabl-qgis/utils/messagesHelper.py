from PyQt5.QtCore import Qt

class ModernMessageDialog():
    def Info_messages_modern(heading, message, message_2=None):

        from ..config.settings import Filepaths, FilesByNames
        widget_name = Filepaths._get_widget_name(FilesByNames().info_message_ui)
        message_box = Filepaths.load_ui_file(widget_name)
        message_box.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        message_box.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        message_box.setAttribute(Qt.WA_TranslucentBackground)
        message_box.setAttribute(Qt.WA_DeleteOnClose)
        #    self.message_box.setAttribute(Qt.WA_DeleteOnClose)
        label_1= message_box.lblSolution
        label_2= message_box.lblInfo
        label_1.hide()
        label_2.hide()        
        title = message_box.lblTitle
        label_1.setText(str(message))
        if message:
            label_1.show()
            label_1.setText(str(message))
        if message_2:
            label_2.show()
            label_2.setText(str(message_2))
        title.setText(str(heading))
        button_box = message_box.buttonBox
        if button_box:
            button_box.accepted.connect(message_box.accept)
            button_box.rejected.connect(message_box.reject)

        message_box.exec_()
