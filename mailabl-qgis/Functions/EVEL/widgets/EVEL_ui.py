# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Kalver\Desktop\Plugins\mailabl-qgis\mailabl-qgis\Functions\EVEL\widgets\EVEL.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EVEL(object):
    def setupUi(self, EVEL):
        EVEL.setObjectName("EVEL")
        EVEL.resize(900, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EVEL.sizePolicy().hasHeightForWidth())
        EVEL.setSizePolicy(sizePolicy)
        EVEL.setMinimumSize(QtCore.QSize(900, 750))
        EVEL.setMaximumSize(QtCore.QSize(900, 750))
        EVEL.setStyleSheet("\n"
"#lblDialer{\n"
"    background-color: None;\n"
"    backround: None;\n"
"    border: None\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#leInfo,#leSelectedProperties {\n"
"    border: None;\n"
"    background-color: #272c35;\n"
"    color: #c5c5d2;\n"
"    padding-left: 10px; /* Adjust the left padding as needed */\n"
"    padding-right: 0px; /* Adjust the right padding as needed */\n"
"    padding-top: 0px; /* Adjust the top padding as needed */\n"
"    padding-bottom: 0px; /* Adjust the bottom padding as needed */\n"
"}\n"
"\n"
"\n"
"#fHeader, #fHelpMenu, \n"
"#fSettingsFolders, #fSettingsFolderStucture,\n"
"#fSettingsMain \n"
"{\n"
"   border: 2px solid #4d4d5b;    /*Same border style as QLineEdit */\n"
"    border-radius: 5px;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"}\n"
"\n"
"\n"
"QWidget{\n"
"    background-color: #272c35;\n"
"    color:#c5c5d2\n"
"}\n"
"\n"
"\n"
"/*esialgu jaotamata omadused*/\n"
"QComboBox {\n"
"    background-color: #40414f; /* Set the background color */\n"
"    color: #ececf1;\n"
"    border: 1px solid #565869;\n"
"    border-radius: 3px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"/* Style the dropdown area */\n"
"QComboBox::drop-down {\n"
"    background-color: #40414f;\n"
"    border: 0px solid #40414f;\n"
"    border-radius: 10px;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: left; /* Center the arrow icon */\n"
"}\n"
"\n"
"/* Style the arrow inside the dropdown */\n"
"QComboBox::down-arrow {\n"
"\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid #40414f;\n"
"    border-right: 6px solid #40414f;\n"
"    border-top: 8px solid #ececf1; /* Adjust the color to match your design */\n"
"    margin: 8px auto; /* Center the arrow */\n"
"}\n"
"\n"
"QComboBox::on {\n"
"    border: 0.5px solid #acacbe;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"   background-color: #3d3e47;\n"
" /* Set the background color for the disabled state */\n"
"    border: 1px solid #565869; /* Adjust border color for disabled state */\n"
"    color: #8a95a5; /* Adjust text color for disabled state */\n"
"}\n"
"\n"
"\n"
"QCheckBox:disabled {\n"
"    color: #8a95a5; /* Adjust text color for disabled state */\n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QAbstractItemView {\n"
"    background-color:#40414f;\n"
"    color:#ececf1;\n"
"    border: 1px solid #565869;\n"
"    border-radius: 4px;\n"
"    padding-left: 5px\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    padding: 2px 8px;\n"
"    text-align: center;\n"
"    border-radius: 6px;\n"
"    background-color:#40414f;\n"
"    border: 1px solid #565869;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #8e8ea0;\n"
"    border: 0.5px solid #acacbe;\n"
"    color: #343541;\n"
"    text-align: center;    \n"
"    padding: 2px 8px;\n"
"    border-radius: 6px;    \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #303040; /* Adjusted disabled background color */\n"
"    border: 1px solid #707070; /* Adjust border color for disabled state */\n"
"    color: #8a95a5; /* Adjust text color for disabled state */\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: #40414f;\n"
"    color: #ececf1;\n"
"    border: 1px solid #565869;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"#label_12,\n"
"#label_11\n"
" {\n"
"    background-color: #40414f;\n"
"    color: #ececf1;\n"
"    border: 1px solid #565869;\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #35363f;  /* Lighter background color */\n"
"    color: #ececf1;\n"
"    /*border: 1px solid #4d4d5b;  Thinner border with a different color */\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #3d3e47;  /* Slightly darker background color on hover */\n"
"}\n"
"\n"
"/* Remove top and side borders */\n"
"QLineEdit {\n"
"    border-top: none;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    color: #8a95a5; /* Adjust text color for disabled state */\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(EVEL)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fMain = QtWidgets.QFrame(EVEL)
        self.fMain.setMinimumSize(QtCore.QSize(0, 200))
        self.fMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fMain.setObjectName("fMain")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fMain)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fMainTools = QtWidgets.QFrame(self.fMain)
        self.fMainTools.setStyleSheet("")
        self.fMainTools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fMainTools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fMainTools.setObjectName("fMainTools")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fMainTools)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fEVEL_settings = QtWidgets.QFrame(self.fMainTools)
        self.fEVEL_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fEVEL_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fEVEL_settings.setObjectName("fEVEL_settings")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fEVEL_settings)
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.fEVEL_settings)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_2.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_2.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_2.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_2.addWidget(self.checkBox_8)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_2.addWidget(self.checkBox_9)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.frame = QtWidgets.QFrame(self.fEVEL_settings)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout_4.addWidget(self.checkBox_10)
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout_4.addWidget(self.checkBox_11)
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout_4.addWidget(self.checkBox_12)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.fEVEL_settings)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.fButtons = QtWidgets.QFrame(self.fMainTools)
        self.fButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fButtons.setObjectName("fButtons")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.fButtons)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(411, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.pbCancel = QtWidgets.QPushButton(self.fButtons)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pbCancel.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\Functions\\EVEL\\widgets\\../../icons/Icons_hele/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancel.setIcon(icon)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_7.addWidget(self.pbCancel)
        self.pbSave = QtWidgets.QPushButton(self.fButtons)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        self.pbSave.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\Functions\\EVEL\\widgets\\../../icons/Icons_hele/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSave.setIcon(icon1)
        self.pbSave.setIconSize(QtCore.QSize(16, 16))
        self.pbSave.setObjectName("pbSave")
        self.horizontalLayout_7.addWidget(self.pbSave)
        self.verticalLayout.addWidget(self.fButtons)
        self.horizontalLayout.addWidget(self.fMainTools)
        self.fHelpMenu = QtWidgets.QFrame(self.fMain)
        self.fHelpMenu.setMinimumSize(QtCore.QSize(200, 0))
        self.fHelpMenu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fHelpMenu.setStyleSheet("")
        self.fHelpMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fHelpMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fHelpMenu.setObjectName("fHelpMenu")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.fHelpMenu)
        self.verticalLayout_10.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.fHelpMenu)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        self.textEdit = QtWidgets.QTextEdit(self.fHelpMenu)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_10.addWidget(self.textEdit)
        self.horizontalLayout.addWidget(self.fHelpMenu)
        self.horizontalLayout_3.addWidget(self.fMain)

        self.retranslateUi(EVEL)
        QtCore.QMetaObject.connectSlotsByName(EVEL)

    def retranslateUi(self, EVEL):
        _translate = QtCore.QCoreApplication.translate
        EVEL.setWindowTitle(_translate("EVEL", "EVEL generaator"))
        self.groupBox.setTitle(_translate("EVEL", "EVEL andmekiht"))
        self.checkBox.setText(_translate("EVEL", "Vesi"))
        self.checkBox_2.setText(_translate("EVEL", "Kanal"))
        self.checkBox_3.setText(_translate("EVEL", "Sademevesi"))
        self.checkBox_4.setText(_translate("EVEL", "Pumpla"))
        self.checkBox_5.setText(_translate("EVEL", "Reoveepuhastid"))
        self.checkBox_6.setText(_translate("EVEL", "Liitumispunktid"))
        self.checkBox_7.setText(_translate("EVEL", "Servituudid"))
        self.checkBox_8.setText(_translate("EVEL", "Võrgusündmused"))
        self.checkBox_9.setText(_translate("EVEL", "SN-väärtused"))
        self.groupBox_2.setTitle(_translate("EVEL", "Andmebaasi tüüp"))
        self.checkBox_10.setText(_translate("EVEL", "Geopakage"))
        self.checkBox_11.setText(_translate("EVEL", "SQL"))
        self.checkBox_12.setText(_translate("EVEL", "Postgre"))
        self.groupBox_3.setTitle(_translate("EVEL", "Andmebaasi nimetus/asukoht"))
        self.label_2.setText(_translate("EVEL", "Nimetus"))
        self.label.setText(_translate("EVEL", "Asukoht"))
        self.pushButton_2.setText(_translate("EVEL", "Määra faili asukoht"))
        self.pushButton.setText(_translate("EVEL", "Genereeri virtuaalkihid"))
        self.pbCancel.setText(_translate("EVEL", "Tühista"))
        self.pbSave.setText(_translate("EVEL", "Salvesta"))
        self.label_4.setText(_translate("EVEL", "Kuidas tööriista\n"
"kasutada?"))
        self.textEdit.setHtml(_translate("EVEL", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
