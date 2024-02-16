# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Confirmation_list.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 500)
        Dialog.setStyleSheet(u"/*\u00fcle\u00fcldine taust ja toonid*/\n"
"/*   *{ \n"
"    --gray-0: #fff;\n"
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
"    gray-950: #050509\n"
"    }*/\n"
"\n"
"\n"
"\n"
"/*\u00fcle\u00fcldine taust ja toonid*/\n"
"\n"
"*{\n"
"	border: transparent;\n"
"	background-color: transparent;\n"
"    background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #c5c5d2;\n"
"}\n"
"\n"
"\n"
"#Dialog{\n"
"    background-color: #202123;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	padding: 1px 8px;\n"
"    border-radius: 6px;\n"
"	background-color:#40414f;\n"
"	border: 0.5px solid #565869;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #8e8ea0;\n"
"	padding: 1px 8px;\n"
"    border-radius: 8px;\n"
"	border: 0.5px solid #acacbe;\n"
"	color: rgb(255, 255, 255"
                        ");\n"
"	padding: 2px 8px;\n"
"    border-radius: 6px\n"
"}\n"
"\n"
"\n"
"\n"
"#f_heading, #f_results, #tblW_confirmation{\n"
"\n"
"        border: 1px solid #2c313c;\n"
"        border-radius: 3px\n"
"		\n"
"    }\n"
"\n"
"\n"
"#f_buttons {\n"
"    border-top: 1px solid #2c313c; \n"
"    border-radius: 1px\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(Dialog)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.f_heading = QFrame(self.MainFrame)
        self.f_heading.setObjectName(u"f_heading")
        self.f_heading.setFrameShape(QFrame.StyledPanel)
        self.f_heading.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.f_heading)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_info = QLabel(self.f_heading)
        self.lb_info.setObjectName(u"lb_info")

        self.horizontalLayout.addWidget(self.lb_info)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.f_heading)

        self.f_results = QFrame(self.MainFrame)
        self.f_results.setObjectName(u"f_results")
        self.f_results.setFrameShape(QFrame.StyledPanel)
        self.f_results.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_results)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tblW_confirmation = QTableWidget(self.f_results)
        self.tblW_confirmation.setObjectName(u"tblW_confirmation")

        self.verticalLayout_2.addWidget(self.tblW_confirmation)


        self.verticalLayout_4.addWidget(self.f_results)

        self.f_footer = QFrame(self.MainFrame)
        self.f_footer.setObjectName(u"f_footer")
        self.f_footer.setStyleSheet(u"")
        self.f_footer.setFrameShape(QFrame.StyledPanel)
        self.f_footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.f_footer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(6, 0, 6, 0)
        self.frame_5 = QFrame(self.f_footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lb_results = QLabel(self.frame_5)
        self.lb_results.setObjectName(u"lb_results")

        self.horizontalLayout_4.addWidget(self.lb_results)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.f_footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lbl_Total_toAdd = QLabel(self.frame_6)
        self.lbl_Total_toAdd.setObjectName(u"lbl_Total_toAdd")

        self.horizontalLayout_5.addWidget(self.lbl_Total_toAdd)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.f_footer)


        self.verticalLayout.addWidget(self.MainFrame)

        self.f_buttons = QFrame(Dialog)
        self.f_buttons.setObjectName(u"f_buttons")
        self.f_buttons.setFrameShape(QFrame.StyledPanel)
        self.f_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.f_buttons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.buttonBox = QDialogButtonBox(self.f_buttons)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.verticalLayout.addWidget(self.f_buttons, 0, Qt.AlignBottom)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lb_info.setText(QCoreApplication.translate("Dialog", u"Tuvastasin, et allpool toodud kinnistud on Mailablis juba olemas ning neid ei lisata.", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Kokku on Mailablis juba olemas:", None))
        self.lb_results.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Eelnevalt tehtud valimist on vaja lisad:", None))
        self.lbl_Total_toAdd.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

