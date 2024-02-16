# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProjectSetup.ui'
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

class Ui_LayeAdjuster(object):
    def setupUi(self, LayeAdjuster):
        if not LayeAdjuster.objectName():
            LayeAdjuster.setObjectName(u"LayeAdjuster")
        LayeAdjuster.resize(718, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LayeAdjuster.sizePolicy().hasHeightForWidth())
        LayeAdjuster.setSizePolicy(sizePolicy)
        LayeAdjuster.setStyleSheet(u"/*\u00fcle\u00fcldine taust ja toonid*/\n"
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
"QLabel {\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(LayeAdjuster)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.f_Label = QFrame(LayeAdjuster)
        self.f_Label.setObjectName(u"f_Label")
        self.f_Label.setFrameShape(QFrame.StyledPanel)
        self.f_Label.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_Label)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.f_Label)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.f_Label)

        self.f_Main = QFrame(LayeAdjuster)
        self.f_Main.setObjectName(u"f_Main")
        self.f_Main.setFrameShape(QFrame.StyledPanel)
        self.f_Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.f_Main)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.f_Main_2 = QFrame(self.f_Main)
        self.f_Main_2.setObjectName(u"f_Main_2")
        self.f_Main_2.setFrameShape(QFrame.StyledPanel)
        self.f_Main_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.f_Main_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.f_Main_3 = QFrame(self.f_Main_2)
        self.f_Main_3.setObjectName(u"f_Main_3")
        self.f_Main_3.setFrameShape(QFrame.StyledPanel)
        self.f_Main_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.f_Main_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lblCurrect_Cadastral_2 = QLabel(self.f_Main_3)
        self.lblCurrect_Cadastral_2.setObjectName(u"lblCurrect_Cadastral_2")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(10)
        self.lblCurrect_Cadastral_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.lblCurrect_Cadastral_2)

        self.cmbProjects_Layer = QComboBox(self.f_Main_3)
        self.cmbProjects_Layer.addItem("")
        self.cmbProjects_Layer.addItem("")
        self.cmbProjects_Layer.addItem("")
        self.cmbProjects_Layer.addItem("")
        self.cmbProjects_Layer.setObjectName(u"cmbProjects_Layer")
        self.cmbProjects_Layer.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(10)
        self.cmbProjects_Layer.setFont(font2)
        self.cmbProjects_Layer.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.cmbProjects_Layer.setIconSize(QSize(6, 6))

        self.horizontalLayout_3.addWidget(self.cmbProjects_Layer)


        self.verticalLayout_3.addWidget(self.f_Main_3)


        self.verticalLayout_4.addWidget(self.f_Main_2)

        self.f_Main_1 = QFrame(self.f_Main)
        self.f_Main_1.setObjectName(u"f_Main_1")
        self.f_Main_1.setFrameShape(QFrame.StyledPanel)
        self.f_Main_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.f_Main_1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblCurrect_Cadastral = QLabel(self.f_Main_1)
        self.lblCurrect_Cadastral.setObjectName(u"lblCurrect_Cadastral")
        self.lblCurrect_Cadastral.setFont(font1)

        self.horizontalLayout.addWidget(self.lblCurrect_Cadastral)

        self.label_2 = QLabel(self.f_Main_1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout_4.addWidget(self.f_Main_1)


        self.verticalLayout.addWidget(self.f_Main)

        self.f_Buttons = QFrame(LayeAdjuster)
        self.f_Buttons.setObjectName(u"f_Buttons")
        self.f_Buttons.setFrameShape(QFrame.StyledPanel)
        self.f_Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.f_Buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(411, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pbCancel = QPushButton(self.f_Buttons)
        self.pbCancel.setObjectName(u"pbCancel")

        self.horizontalLayout_2.addWidget(self.pbCancel)

        self.pbSave = QPushButton(self.f_Buttons)
        self.pbSave.setObjectName(u"pbSave")
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        self.pbSave.setFont(font3)
        icon = QIcon()
        icon.addFile(u"../../icons/Icons_hele/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbSave.setIcon(icon)
        self.pbSave.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.pbSave)


        self.verticalLayout.addWidget(self.f_Buttons)


        self.retranslateUi(LayeAdjuster)

        QMetaObject.connectSlotsByName(LayeAdjuster)
    # setupUi

    def retranslateUi(self, LayeAdjuster):
        LayeAdjuster.setWindowTitle(QCoreApplication.translate("LayeAdjuster", u"Mailabl projektide eelistused", None))
        self.label.setText(QCoreApplication.translate("LayeAdjuster", u"Projektide seadistused", None))
        self.lblCurrect_Cadastral_2.setText(QCoreApplication.translate("LayeAdjuster", u"Projektide kaardikiht", None))
        self.cmbProjects_Layer.setItemText(0, "")
        self.cmbProjects_Layer.setItemText(1, "")
        self.cmbProjects_Layer.setItemText(2, "")
        self.cmbProjects_Layer.setItemText(3, "")

        self.lblCurrect_Cadastral.setText(QCoreApplication.translate("LayeAdjuster", u"Projekti loetelu eelistused", None))
        self.label_2.setText(QCoreApplication.translate("LayeAdjuster", u"Tulekul", None))
        self.pbCancel.setText(QCoreApplication.translate("LayeAdjuster", u"T\u00fchista", None))
        self.pbSave.setText(QCoreApplication.translate("LayeAdjuster", u"Salvesta andmed", None))
    # retranslateUi

