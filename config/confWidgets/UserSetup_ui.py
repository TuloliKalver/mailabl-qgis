# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserSetup.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(u"/*\u00fcle\u00fcldine taust ja toonid*/\n"
"/*--gray-0: #fff;\n"
"    --gray-50: #f7f7f8;\n"
"    --gray-100: #ececf1;\n"
"    --gray-200: #d9d9e3;\n"
"    --gray-300: #c5c5d2;\n"
"    --gray-400: #acacbe;\n"
"    --gray-500: #8e8ea0;\n"
"    --gray-600: #565869;\n"
"    --gray-700: #40414f;\n"
"    --gray-800: #343541;\n"
"    --gray-900: #202123;\n"
"    --gray-950: #050509;\n"
"*/\n"
"\n"
"/*style the combobox itself*/\n"
"\n"
"\n"
"QWidget{\n"
"    background-color: #272c35;\n"
"	color:#c5c5d2\n"
"}\n"
"\n"
"\n"
"/*esialgu jaotamata omadused*/\n"
"QComboBox{\n"
"\n"
"	background-color:#40414f;\n"
"	color:#ececf1;\n"
"	border: 1px solid #565869;\n"
"	border-radius: 3px;\n"
"	padding-left: 5px\n"
"}\n"
"\n"
"/*Style the dropdown area*/\n"
"QComboBox::drop-down{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:135, stop:0.704545 rgba(64, 65, 79), stop:1 rgba(217, 217, 227));\n"
"	border: 1px solid #565869;\n"
"	border-radius: 8px;\n"
"	height:16px;\n"
"	width: 16px;\n"
"	subcontrol-origin: paddin"
                        "g;\n"
"    subcontrol-position: left\n"
"}\n"
"\n"
"QComboBox::on{\n"
"\n"
"  	border: 0.5px solid #acacbe;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"	background-color:#40414f;\n"
"	color:#ececf1;\n"
"	border: 1px solid #565869;\n"
"	border-radius: 4px;\n"
"	padding-left: 5px\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	padding: 2px 8px;\n"
"	text-align: center;\n"
"	border-radius: 6px;\n"
"	background-color:#40414f;\n"
"	border: 1px solid #565869;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #8e8ea0;\n"
"	border: 0.5px solid #acacbe;\n"
"	color: #343541;\n"
"	text-align: center;	\n"
"	padding: 2px 8px;\n"
"    border-radius: 6px;\n"
"	\n"
"}\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 19, 10, 10)
        self.f_Label = QFrame(Dialog)
        self.f_Label.setObjectName(u"f_Label")
        self.f_Label.setFrameShape(QFrame.StyledPanel)
        self.f_Label.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.f_Label)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_Heading = QLabel(self.f_Label)
        self.lbl_Heading.setObjectName(u"lbl_Heading")
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_Heading.setFont(font)

        self.verticalLayout.addWidget(self.lbl_Heading, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.f_Label)

        self.f_Main = QFrame(Dialog)
        self.f_Main.setObjectName(u"f_Main")
        self.f_Main.setFrameShape(QFrame.StyledPanel)
        self.f_Main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.f_Main)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SubFrame_labels = QFrame(self.f_Main)
        self.SubFrame_labels.setObjectName(u"SubFrame_labels")
        self.SubFrame_labels.setFrameShape(QFrame.StyledPanel)
        self.SubFrame_labels.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.SubFrame_labels)
        self.verticalLayout_47.setSpacing(10)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.lblCurrect_Cadastral = QLabel(self.SubFrame_labels)
        self.lblCurrect_Cadastral.setObjectName(u"lblCurrect_Cadastral")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(10)
        self.lblCurrect_Cadastral.setFont(font1)

        self.verticalLayout_47.addWidget(self.lblCurrect_Cadastral)

        self.label = QLabel(self.SubFrame_labels)
        self.label.setObjectName(u"label")

        self.verticalLayout_47.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.SubFrame_labels)

        self.subFrame_comboBoxes = QFrame(self.f_Main)
        self.subFrame_comboBoxes.setObjectName(u"subFrame_comboBoxes")
        self.subFrame_comboBoxes.setFrameShape(QFrame.StyledPanel)
        self.subFrame_comboBoxes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.subFrame_comboBoxes)
        self.verticalLayout_48.setSpacing(10)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.cmbUserLayers = QComboBox(self.subFrame_comboBoxes)
        self.cmbUserLayers.addItem("")
        self.cmbUserLayers.addItem("")
        self.cmbUserLayers.addItem("")
        self.cmbUserLayers.addItem("")
        self.cmbUserLayers.setObjectName(u"cmbUserLayers")
        self.cmbUserLayers.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(10)
        self.cmbUserLayers.setFont(font2)
        self.cmbUserLayers.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.cmbUserLayers.setIconSize(QSize(6, 6))

        self.verticalLayout_48.addWidget(self.cmbUserLayers)

        self.label_2 = QLabel(self.subFrame_comboBoxes)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_48.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.subFrame_comboBoxes)


        self.verticalLayout_2.addWidget(self.f_Main)

        self.f_Buttons = QFrame(Dialog)
        self.f_Buttons.setObjectName(u"f_Buttons")
        self.f_Buttons.setFrameShape(QFrame.StyledPanel)
        self.f_Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.f_Buttons)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 10, 0, 0)
        self.pbDel_Project_Settings = QPushButton(self.f_Buttons)
        self.pbDel_Project_Settings.setObjectName(u"pbDel_Project_Settings")
        icon = QIcon()
        icon.addFile(u"../../icons/Icons_hele/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbDel_Project_Settings.setIcon(icon)
        self.pbDel_Project_Settings.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.pbDel_Project_Settings)

        self.horizontalSpacer = QSpacerItem(411, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pbSave_Projects_Settings = QPushButton(self.f_Buttons)
        self.pbSave_Projects_Settings.setObjectName(u"pbSave_Projects_Settings")
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        self.pbSave_Projects_Settings.setFont(font3)
        icon1 = QIcon()
        icon1.addFile(u"../../icons/Icons_hele/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbSave_Projects_Settings.setIcon(icon1)
        self.pbSave_Projects_Settings.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.pbSave_Projects_Settings)


        self.verticalLayout_2.addWidget(self.f_Buttons)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Kasutaja eelistused", None))
        self.lbl_Heading.setText(QCoreApplication.translate("Dialog", u"Minu eelistused", None))
        self.lblCurrect_Cadastral.setText(QCoreApplication.translate("Dialog", u"Avamisel eelistatav moodul:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Avalehe eelistused:", None))
        self.cmbUserLayers.setItemText(0, "")
        self.cmbUserLayers.setItemText(1, "")
        self.cmbUserLayers.setItemText(2, "")
        self.cmbUserLayers.setItemText(3, "")

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Tulekul", None))
        self.pbDel_Project_Settings.setText(QCoreApplication.translate("Dialog", u"T\u00fchista seadistused", None))
        self.pbSave_Projects_Settings.setText(QCoreApplication.translate("Dialog", u"Salvesta andmed", None))
    # retranslateUi

