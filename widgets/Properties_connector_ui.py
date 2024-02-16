# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Properties_connector.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(783, 352)
        Dialog.setStyleSheet(u"*{\n"
"	border: transparent;\n"
"	background-color: transparent;\n"
"    background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #c5c5d2;\n"
"}\n"
"\n"
"/*konteinerite peamised omadused*/\n"
"\n"
"QDialog{\n"
"    background-color: #272c35;\n"
"}\n"
"\n"
"#swWorkSpace{\n"
"    background-color: #202123;\n"
"}\n"
"#Sevituudid{\n"
"    background-color: #343b47;\n"
"}\n"
"\n"
"#leftMenuContainer{\n"
"    background-color: #202123 ;\n"
"}\n"
"\n"
"#rightMenuContainer{\n"
"    background-color: #272c35;\n"
"}\n"
"\n"
"\n"
"/*nuppu peamised omadused*/\n"
"/*\u00dcldomadused*/\n"
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
"    \n"
"	color: rgb(255, 255, 255);\n"
"	padding: 2px 8px;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fMainLabel = QFrame(Dialog)
        self.fMainLabel.setObjectName(u"fMainLabel")
        self.fMainLabel.setFrameShape(QFrame.StyledPanel)
        self.fMainLabel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fMainLabel)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblDescription = QLabel(self.fMainLabel)
        self.lblDescription.setObjectName(u"lblDescription")

        self.horizontalLayout_2.addWidget(self.lblDescription)

        self.lblProjectNumber = QLabel(self.fMainLabel)
        self.lblProjectNumber.setObjectName(u"lblProjectNumber")

        self.horizontalLayout_2.addWidget(self.lblProjectNumber)

        self.lblProjectName = QLabel(self.fMainLabel)
        self.lblProjectName.setObjectName(u"lblProjectName")

        self.horizontalLayout_2.addWidget(self.lblProjectName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.fMainLabel)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pbClear_list = QPushButton(self.frame_2)
        self.pbClear_list.setObjectName(u"pbClear_list")

        self.verticalLayout_3.addWidget(self.pbClear_list)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_2)

        self.tvProperties_AddTo_Projects = QTableView(self.frame)
        self.tvProperties_AddTo_Projects.setObjectName(u"tvProperties_AddTo_Projects")

        self.horizontalLayout.addWidget(self.tvProperties_AddTo_Projects)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lblDescription.setText(QCoreApplication.translate("Dialog", u"Kinnistud lisatakse projektile:", None))
        self.lblProjectNumber.setText("")
        self.lblProjectName.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"N\u00fc\u00fcd on k\u00f5ik vajalik juba aktiveeritud ja saad alustada kohe kinnistute valikuga. NB! kui varasemalt on kinnituid juba valitud siis need kuvatakse juba tabelis. ", None))
        self.pbClear_list.setText(QCoreApplication.translate("Dialog", u"T\u00fchista valik", None))
    # retranslateUi

