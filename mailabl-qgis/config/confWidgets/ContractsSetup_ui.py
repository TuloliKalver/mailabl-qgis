# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Kalver\Desktop\Plugins\mailabl-qgis\mailabl-qgis\config\confWidgets\ContractsSetup.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContractSettings(object):
    def setupUi(self, ContractSettings):
        ContractSettings.setObjectName("ContractSettings")
        ContractSettings.resize(900, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ContractSettings.sizePolicy().hasHeightForWidth())
        ContractSettings.setSizePolicy(sizePolicy)
        ContractSettings.setMinimumSize(QtCore.QSize(900, 350))
        ContractSettings.setMaximumSize(QtCore.QSize(900, 350))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        ContractSettings.setFont(font)
        ContractSettings.setStyleSheet("\n"
"\n"
"#fHelpMenu, \n"
"#fSettingsPreferrences\n"
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
"    border-radius: 6px;\n"
"    \n"
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
"\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(ContractSettings)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fContent = QtWidgets.QFrame(ContractSettings)
        self.fContent.setMinimumSize(QtCore.QSize(0, 100))
        self.fContent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fContent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fContent.setObjectName("fContent")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.fContent)
        self.horizontalLayout_6.setContentsMargins(0, 10, 10, 10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fSettingsMain = QtWidgets.QFrame(self.fContent)
        self.fSettingsMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fSettingsMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fSettingsMain.setObjectName("fSettingsMain")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fSettingsMain)
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fSettingsPreferrences = QtWidgets.QFrame(self.fSettingsMain)
        self.fSettingsPreferrences.setStyleSheet("")
        self.fSettingsPreferrences.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fSettingsPreferrences.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fSettingsPreferrences.setObjectName("fSettingsPreferrences")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fSettingsPreferrences)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.f_Main_5 = QtWidgets.QFrame(self.fSettingsPreferrences)
        self.f_Main_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_Main_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_Main_5.setObjectName("f_Main_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.f_Main_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblCurrect_Cadastral_3 = QtWidgets.QLabel(self.f_Main_5)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lblCurrect_Cadastral_3.setFont(font)
        self.lblCurrect_Cadastral_3.setObjectName("lblCurrect_Cadastral_3")
        self.horizontalLayout_5.addWidget(self.lblCurrect_Cadastral_3, 0, QtCore.Qt.AlignLeft)
        self.cmbPreferredContractStatuses = QtWidgets.QComboBox(self.f_Main_5)
        self.cmbPreferredContractStatuses.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbPreferredContractStatuses.setFont(font)
        self.cmbPreferredContractStatuses.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbPreferredContractStatuses.setIconSize(QtCore.QSize(6, 6))
        self.cmbPreferredContractStatuses.setObjectName("cmbPreferredContractStatuses")
        self.cmbPreferredContractStatuses.addItem("")
        self.cmbPreferredContractStatuses.setItemText(0, "")
        self.cmbPreferredContractStatuses.addItem("")
        self.cmbPreferredContractStatuses.setItemText(1, "")
        self.cmbPreferredContractStatuses.addItem("")
        self.cmbPreferredContractStatuses.setItemText(2, "")
        self.cmbPreferredContractStatuses.addItem("")
        self.cmbPreferredContractStatuses.setItemText(3, "")
        self.horizontalLayout_5.addWidget(self.cmbPreferredContractStatuses)
        self.verticalLayout_3.addWidget(self.f_Main_5)
        self.f_Main_4 = QtWidgets.QFrame(self.fSettingsPreferrences)
        self.f_Main_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_Main_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_Main_4.setObjectName("f_Main_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.f_Main_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblPreferedContractTypes_2 = QtWidgets.QLabel(self.f_Main_4)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lblPreferedContractTypes_2.setFont(font)
        self.lblPreferedContractTypes_2.setObjectName("lblPreferedContractTypes_2")
        self.horizontalLayout_4.addWidget(self.lblPreferedContractTypes_2, 0, QtCore.Qt.AlignLeft)
        self.cbcb_PreferredContractTypes = QgsCheckableComboBox(self.f_Main_4)
        self.cbcb_PreferredContractTypes.setObjectName("cbcb_PreferredContractTypes")
        self.horizontalLayout_4.addWidget(self.cbcb_PreferredContractTypes)
        self.verticalLayout_3.addWidget(self.f_Main_4)
        self.verticalLayout_2.addWidget(self.fSettingsPreferrences)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.f_Buttons = QtWidgets.QFrame(self.fSettingsMain)
        self.f_Buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_Buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_Buttons.setObjectName("f_Buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.f_Buttons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(411, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pbCancel = QtWidgets.QPushButton(self.f_Buttons)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\config\\confWidgets\\../../icons/Icons_hele/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancel.setIcon(icon)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_2.addWidget(self.pbCancel)
        self.pbSave = QtWidgets.QPushButton(self.f_Buttons)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.pbSave.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\config\\confWidgets\\../../icons/Icons_hele/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSave.setIcon(icon1)
        self.pbSave.setIconSize(QtCore.QSize(18, 18))
        self.pbSave.setObjectName("pbSave")
        self.horizontalLayout_2.addWidget(self.pbSave)
        self.verticalLayout_2.addWidget(self.f_Buttons)
        self.horizontalLayout_6.addWidget(self.fSettingsMain)
        self.fHelpMenu = QtWidgets.QFrame(self.fContent)
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
        self.label_2 = QtWidgets.QLabel(self.fHelpMenu)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.fHelpMenu)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_10.addWidget(self.textEdit)
        self.horizontalLayout_6.addWidget(self.fHelpMenu)
        self.verticalLayout.addWidget(self.fContent)

        self.retranslateUi(ContractSettings)
        QtCore.QMetaObject.connectSlotsByName(ContractSettings)

    def retranslateUi(self, ContractSettings):
        _translate = QtCore.QCoreApplication.translate
        ContractSettings.setWindowTitle(_translate("ContractSettings", "Lepingute seaded"))
        self.lblCurrect_Cadastral_3.setText(_translate("ContractSettings", "Eelistatud staatus"))
        self.lblPreferedContractTypes_2.setText(_translate("ContractSettings", "Eelistatud lepingu liik"))
        self.pbCancel.setText(_translate("ContractSettings", "Tühista"))
        self.pbSave.setText(_translate("ContractSettings", "Salvesta"))
        self.label_2.setText(_translate("ContractSettings", "Seadete selgitused"))
        self.textEdit.setHtml(_translate("ContractSettings", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Eelistatud staatus</span><br /><span style=\" font-size:9pt;\">Saad teha valiku, millise staatusega lepinguid lehe avamisel kuvatakse.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Eelistatud lepingu liigid</span><br /><span style=\" font-size:9pt;\">Saad teha valiku, milliste liikidega lepinguid lehe avamisel kuvatakse.</span></p></body></html>"))
from qgscheckablecombobox import QgsCheckableComboBox
