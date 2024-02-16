# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WStatusBar_County.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Edenemine(object):
    def setupUi(self, Edenemine):
        if not Edenemine.objectName():
            Edenemine.setObjectName(u"Edenemine")
        Edenemine.resize(500, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Edenemine.sizePolicy().hasHeightForWidth())
        Edenemine.setSizePolicy(sizePolicy)
        Edenemine.setStyleSheet(u"*{\n"
"	border: transparent;\n"
"	background-color: transparent;\n"
"    background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #dadee4;\n"
"}\n"
"\n"
"#widget {\n"
"    background-color: #272c35;\n"
"}\n"
"\n"
"#widget_2{\n"
"    background-color: #272c35;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Edenemine)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(Edenemine)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.testBar = QProgressBar(self.widget)
        self.testBar.setObjectName(u"testBar")
        self.testBar.setValue(24)

        self.verticalLayout.addWidget(self.testBar)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.retranslateUi(Edenemine)

        QMetaObject.connectSlotsByName(Edenemine)
    # setupUi

    def retranslateUi(self, Edenemine):
        Edenemine.setWindowTitle(QCoreApplication.translate("Edenemine", u"Otsin maakondasid", None))
        self.label.setText(QCoreApplication.translate("Edenemine", u"\u00dcks hetk. Nuputan, mida sulle j\u00e4rgmisena n\u00e4idata.", None))
        self.label_2.setText(QCoreApplication.translate("Edenemine", u"Kas sa oled t\u00e4na juba arvutiekraanist silmi puhanud?", None))
    # retranslateUi

