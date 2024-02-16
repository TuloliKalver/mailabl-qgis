# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ComboBox design.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
import test_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(497, 320)
        MainWindow.setStyleSheet(u"/*konteinerite peamised omadused*/\n"
"\n"
"QWidget{\n"
"    background-color: #272c35;\n"
"}\n"
"\n"
"/*\u00fcle\u00fcldine taust ja toonid*/\n"
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
"\n"
"/*style the combobox itself*/\n"
"QComboBox{\n"
"	background-color:#40414f;\n"
"	color:#ececf1;\n"
"	border: 1px solid #565869;\n"
"	border-radius: 4px;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"/*Style the dropdown area*/\n"
"QComboBox::drop-down{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:135, stop:0.704545 rgba(64, 65, 79), stop:1 rgba(217, 217, 227));\n"
"	border: 1px solid #565869;\n"
"	border-radius: 8px;\n"
"	height:16px;\n"
"	width: 16px;\n"
"	subcontrol-origin: padding 2px;\n"
"    subcontro"
                        "l-position: left;\n"
"}\n"
"\n"
"QComboBox::on{\n"
"	border: 2px solid #565869;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"	background-color:#40414f;\n"
"	color:#ececf1;\n"
"	border: 1px solid #565869;\n"
"	border-radius: 4px;\n"
"	padding-left: 5px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(58, 30, 251, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 497, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"null", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00fcks", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"kaks", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"kolm", None))

    # retranslateUi

