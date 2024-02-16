# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LayerSetup.ui'
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
        LayeAdjuster.resize(573, 150)
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
"")
        self.verticalLayout_2 = QVBoxLayout(LayeAdjuster)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Layer_Adjuster_Frame = QWidget(LayeAdjuster)
        self.Layer_Adjuster_Frame.setObjectName(u"Layer_Adjuster_Frame")
        self.verticalLayout = QVBoxLayout(self.Layer_Adjuster_Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Hading = QLabel(self.Layer_Adjuster_Frame)
        self.Hading.setObjectName(u"Hading")
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        font.setBold(True)
        self.Hading.setFont(font)

        self.verticalLayout.addWidget(self.Hading, 0, Qt.AlignHCenter)

        self.Main_frame = QWidget(self.Layer_Adjuster_Frame)
        self.Main_frame.setObjectName(u"Main_frame")
        self.Main_frame.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.Main_frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 0, 0, 0)
        self.mainFrame_subFrame = QWidget(self.Main_frame)
        self.mainFrame_subFrame.setObjectName(u"mainFrame_subFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame_subFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame_subFrame.setSizePolicy(sizePolicy)
        self.mainFrame_subFrame.setMinimumSize(QSize(40, 0))
        self.mainFrame_subFrame.setMaximumSize(QSize(16777215, 16777215))
        self.mainFrame_subFrame.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.mainFrame_subFrame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.SubFrame_labels = QFrame(self.mainFrame_subFrame)
        self.SubFrame_labels.setObjectName(u"SubFrame_labels")
        self.SubFrame_labels.setFrameShape(QFrame.StyledPanel)
        self.SubFrame_labels.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.SubFrame_labels)
        self.verticalLayout_47.setSpacing(5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.lblCurrect_Cadastral = QLabel(self.SubFrame_labels)
        self.lblCurrect_Cadastral.setObjectName(u"lblCurrect_Cadastral")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(10)
        self.lblCurrect_Cadastral.setFont(font1)

        self.verticalLayout_47.addWidget(self.lblCurrect_Cadastral)

        self.lblTarget_Cadastral = QLabel(self.SubFrame_labels)
        self.lblTarget_Cadastral.setObjectName(u"lblTarget_Cadastral")
        font2 = QFont()
        font2.setPointSize(10)
        self.lblTarget_Cadastral.setFont(font2)

        self.verticalLayout_47.addWidget(self.lblTarget_Cadastral)


        self.horizontalLayout_9.addWidget(self.SubFrame_labels)

        self.subFrame_comboBoxes = QFrame(self.mainFrame_subFrame)
        self.subFrame_comboBoxes.setObjectName(u"subFrame_comboBoxes")
        self.subFrame_comboBoxes.setFrameShape(QFrame.StyledPanel)
        self.subFrame_comboBoxes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.subFrame_comboBoxes)
        self.verticalLayout_48.setSpacing(5)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.cbCurrent_Cadastral = QComboBox(self.subFrame_comboBoxes)
        self.cbCurrent_Cadastral.addItem("")
        self.cbCurrent_Cadastral.addItem("")
        self.cbCurrent_Cadastral.addItem("")
        self.cbCurrent_Cadastral.addItem("")
        self.cbCurrent_Cadastral.setObjectName(u"cbCurrent_Cadastral")
        self.cbCurrent_Cadastral.setBaseSize(QSize(0, 0))
        self.cbCurrent_Cadastral.setFont(font2)
        self.cbCurrent_Cadastral.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.cbCurrent_Cadastral.setIconSize(QSize(6, 6))

        self.verticalLayout_48.addWidget(self.cbCurrent_Cadastral)

        self.cbTarget_Cadastral = QComboBox(self.subFrame_comboBoxes)
        self.cbTarget_Cadastral.addItem("")
        self.cbTarget_Cadastral.addItem("")
        self.cbTarget_Cadastral.addItem("")
        self.cbTarget_Cadastral.addItem("")
        self.cbTarget_Cadastral.setObjectName(u"cbTarget_Cadastral")
        self.cbTarget_Cadastral.setFont(font2)

        self.verticalLayout_48.addWidget(self.cbTarget_Cadastral)


        self.horizontalLayout_9.addWidget(self.subFrame_comboBoxes)


        self.verticalLayout_16.addWidget(self.mainFrame_subFrame)

        self.Buttons = QFrame(self.Main_frame)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setFrameShape(QFrame.StyledPanel)
        self.Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pbPrintSettings = QPushButton(self.Buttons)
        self.pbPrintSettings.setObjectName(u"pbPrintSettings")
        icon = QIcon()
        icon.addFile(u"../../icons/Icons_hele/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbPrintSettings.setIcon(icon)
        self.pbPrintSettings.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.pbPrintSettings)

        self.horizontalSpacer = QSpacerItem(411, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pbCancelSave = QPushButton(self.Buttons)
        self.pbCancelSave.setObjectName(u"pbCancelSave")
        icon1 = QIcon()
        icon1.addFile(u"../../icons/Icons_hele/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbCancelSave.setIcon(icon1)
        self.pbCancelSave.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.pbCancelSave)

        self.pbSaveLayerSettings = QPushButton(self.Buttons)
        self.pbSaveLayerSettings.setObjectName(u"pbSaveLayerSettings")
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        self.pbSaveLayerSettings.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u"../../icons/Icons_hele/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbSaveLayerSettings.setIcon(icon2)
        self.pbSaveLayerSettings.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.pbSaveLayerSettings)


        self.verticalLayout_16.addWidget(self.Buttons)


        self.verticalLayout.addWidget(self.Main_frame)


        self.verticalLayout_2.addWidget(self.Layer_Adjuster_Frame)


        self.retranslateUi(LayeAdjuster)

        QMetaObject.connectSlotsByName(LayeAdjuster)
    # setupUi

    def retranslateUi(self, LayeAdjuster):
        LayeAdjuster.setWindowTitle(QCoreApplication.translate("LayeAdjuster", u"Projekti kihtide seadistamine", None))
        self.Hading.setText(QCoreApplication.translate("LayeAdjuster", u"Kinnistu kihtide sadistamine", None))
        self.lblCurrect_Cadastral.setText(QCoreApplication.translate("LayeAdjuster", u"Praegune \"Katastri\" aluskiht", None))
        self.lblTarget_Cadastral.setText(QCoreApplication.translate("LayeAdjuster", u"M\u00e4\u00e4ra millisele kihile andmed salvestatakse", None))
        self.cbCurrent_Cadastral.setItemText(0, "")
        self.cbCurrent_Cadastral.setItemText(1, "")
        self.cbCurrent_Cadastral.setItemText(2, "")
        self.cbCurrent_Cadastral.setItemText(3, "")

        self.cbTarget_Cadastral.setItemText(0, "")
        self.cbTarget_Cadastral.setItemText(1, "")
        self.cbTarget_Cadastral.setItemText(2, "")
        self.cbTarget_Cadastral.setItemText(3, "")

        self.pbPrintSettings.setText(QCoreApplication.translate("LayeAdjuster", u"Prindi andmed_pythonis", None))
        self.pbCancelSave.setText(QCoreApplication.translate("LayeAdjuster", u"T\u00fchista seadistused", None))
        self.pbSaveLayerSettings.setText(QCoreApplication.translate("LayeAdjuster", u"Salvesta andmed", None))
    # retranslateUi

