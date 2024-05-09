# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Kalver\Desktop\Plugins\mailabl-qgis\mailabl-qgis\widgets\Properties_connector_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 375)
        Dialog.setMinimumSize(QtCore.QSize(700, 375))
        Dialog.setMaximumSize(QtCore.QSize(700, 375))
        Dialog.setWindowOpacity(1.0)
        Dialog.setStyleSheet("\n"
"\n"
"#lblDescription {\n"
"    border: None;\n"
"    background-color: #272c35;\n"
"    color: #c5c5d2;\n"
"    padding-left: 0px; /* Adjust the left padding as needed */\n"
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
"QComboBox{\n"
"\n"
"    background-color:#40414f;\n"
"    color:#ececf1;\n"
"    border: 1px solid #565869;\n"
"    border-radius: 3px;\n"
"    padding-left: 5px\n"
"}\n"
"\n"
"/*Style the dropdown area*/\n"
"QComboBox::drop-down{\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:135, stop:0.704545 rgba(64, 65, 79), stop:1 rgba(217, 217, 227));\n"
"    border: 1px solid #565869;\n"
"    border-radius: 8px;\n"
"    height:16px;\n"
"    width: 16px;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: left\n"
"}\n"
"\n"
"QComboBox::on{\n"
"\n"
"      border: 0.5px solid #acacbe;\n"
"}\n"
"\n"
"\n"
"QComboBox:disabled {\n"
"    background-color: #303040; /* Adjusted disabled background color */\n"
"    border: 1px solid #707070; /* Adjust border color for disabled state */\n"
"    color: #8a95a5; /* Adjust text color for disabled state */\n"
"}\n"
"\n"
"\n"
"QCheckBox:disabled {\n"
"    color: #8a95a5; /* Adjust text color for disabled state */\n"
"}\n"
"\n"
"\n"
"QAbstractItemView {\n"
"    background-color:#40414f;\n"
"    color:#ececf1;\n"
"    border: 1px solid #565869;\n"
"    border-radius: 4px;\n"
"    padding-left: 0px\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    padding: 2px 5px;\n"
"    text-align: center;\n"
"    border-radius: 5px;\n"
"    background-color:#40414f;\n"
"    border: 1px solid #565869;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #8e8ea0;\n"
"    border: 0.5px solid #acacbe;\n"
"    color: #343541;\n"
"    text-align: center;\n"
"    padding: 2px 5px;\n"
"    border-radius: 5px;    \n"
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
"    padding: 1px 4px 1px 4px;\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #35363f;  /* Lighter background color */\n"
"    color: #ececf1;\n"
"    border: 1px solid #4d4d5b;  /*Thinner border with a different color */\n"
"    border-radius: 5px;\n"
"    padding: 1px 4px 1px 4px;    \n"
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
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frHeading = QtWidgets.QFrame(self.frame_3)
        self.frHeading.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frHeading.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frHeading.setObjectName("frHeading")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frHeading)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frHeading)
        self.frame.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblDescription = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDescription.setFont(font)
        self.lblDescription.setObjectName("lblDescription")
        self.horizontalLayout_3.addWidget(self.lblDescription)
        self.leElementNumber = QtWidgets.QLineEdit(self.frame)
        self.leElementNumber.setMinimumSize(QtCore.QSize(100, 0))
        self.leElementNumber.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leElementNumber.setAcceptDrops(False)
        self.leElementNumber.setReadOnly(True)
        self.leElementNumber.setObjectName("leElementNumber")
        self.horizontalLayout_3.addWidget(self.leElementNumber)
        self.leElementName = QtWidgets.QLineEdit(self.frame)
        self.leElementName.setAcceptDrops(False)
        self.leElementName.setReadOnly(True)
        self.leElementName.setObjectName("leElementName")
        self.horizontalLayout_3.addWidget(self.leElementName)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_4.addWidget(self.frHeading)
        self.frTable = QtWidgets.QFrame(self.frame_3)
        self.frTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frTable.setObjectName("frTable")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frTable)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tvProperties = QtWidgets.QTableView(self.frTable)
        self.tvProperties.setObjectName("tvProperties")
        self.horizontalLayout.addWidget(self.tvProperties)
        self.verticalLayout_4.addWidget(self.frTable)
        self.fButtons = QtWidgets.QFrame(self.frame_3)
        self.fButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fButtons.setObjectName("fButtons")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.fButtons)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pbClear_list = QtWidgets.QPushButton(self.fButtons)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\widgets\\../icons/Icons_hele/refresh-cw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbClear_list.setIcon(icon)
        self.pbClear_list.setObjectName("pbClear_list")
        self.horizontalLayout_7.addWidget(self.pbClear_list)
        spacerItem = QtWidgets.QSpacerItem(411, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.pbCancel = QtWidgets.QPushButton(self.fButtons)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\widgets\\../icons/Icons_hele/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancel.setIcon(icon1)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_7.addWidget(self.pbCancel)
        self.pbSave = QtWidgets.QPushButton(self.fButtons)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.pbSave.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\widgets\\../icons/Icons_hele/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSave.setIcon(icon2)
        self.pbSave.setIconSize(QtCore.QSize(16, 16))
        self.pbSave.setObjectName("pbSave")
        self.horizontalLayout_7.addWidget(self.pbSave)
        self.verticalLayout_4.addWidget(self.fButtons)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.fHelpMenu = QtWidgets.QFrame(self.frame_2)
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
        self.horizontalLayout_2.addWidget(self.fHelpMenu)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kinnistutega sidumine"))
        self.lblDescription.setText(_translate("Dialog", "Objekti nimetus:"))
        self.pbClear_list.setText(_translate("Dialog", "Alusta valimist uuesti"))
        self.pbCancel.setText(_translate("Dialog", "Tühista"))
        self.pbSave.setText(_translate("Dialog", "Salvesta"))
        self.label_4.setText(_translate("Dialog", "Kuidas tööriista\n"
"kasutada?\n"
"(juhend koostamisel)"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Oled aktiveerinud kinnistu kihi ning võid alustada kinnistute valimisega. <br />Valikuid saad teha:<br />1. valides ühe kinnistu - iga clik mille ekraanil teed valib uue kinnistu. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. hoides all ctrl ja vajutades kinnistutel jääb eelnev vaik alles. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. hoides all vasakut hiire nuppu saad kasutada ruut valikut. Kõik kinnistud mis jäevad ruudu sisse kaasatakse valikusse. <br /><br />Sul on võimalik kasutada ka muid QGIS valiku meetodeid. Kuniks see tööriist on avatud ja valikuid teostatakse kinnistute kihil kaasatakse kinnistud lisatavate kinnistute hulka. </p></body></html>"))
