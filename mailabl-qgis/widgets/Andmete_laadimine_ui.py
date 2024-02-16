# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Andmete_laadimine.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(616, 312)
        Dialog.setStyleSheet(u"QWidget{\n"
"    background-color: #272c35;\n"
"	color:#c5c5d2\n"
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
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(Dialog)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pbLisaShpFail = QPushButton(self.widget)
        self.pbLisaShpFail.setObjectName(u"pbLisaShpFail")
        icon = QIcon()
        icon.addFile(u"../icons/Icons_hele/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbLisaShpFail.setIcon(icon)
        self.pbLisaShpFail.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pbLisaShpFail)

        self.pbAvaMaaAmet = QPushButton(self.widget)
        self.pbAvaMaaAmet.setObjectName(u"pbAvaMaaAmet")
        icon1 = QIcon()
        icon1.addFile(u"../icons/Icons_hele/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbAvaMaaAmet.setIcon(icon1)
        self.pbAvaMaaAmet.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pbAvaMaaAmet)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.widget)

        self.textEdit = QTextEdit(self.widget_3)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(527, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pbLisaShpFail.setText(QCoreApplication.translate("Dialog", u"Lae algandmed", None))
        self.pbAvaMaaAmet.setText(QCoreApplication.translate("Dialog", u"Maa_ametisse", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Sulge", None))
    # retranslateUi

