# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ContractsPropertiesConnector.ui'
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
        Dialog.resize(543, 352)
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

        self.lblContractNumber = QLabel(self.fMainLabel)
        self.lblContractNumber.setObjectName(u"lblContractNumber")

        self.horizontalLayout_2.addWidget(self.lblContractNumber)

        self.lblContractName = QLabel(self.fMainLabel)
        self.lblContractName.setObjectName(u"lblContractName")

        self.horizontalLayout_2.addWidget(self.lblContractName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.fMainLabel)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tvProperties_AddTo_Contracts = QTableView(self.frame)
        self.tvProperties_AddTo_Contracts.setObjectName(u"tvProperties_AddTo_Contracts")

        self.horizontalLayout.addWidget(self.tvProperties_AddTo_Contracts)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 6, 6)
        self.pbClear_list = QPushButton(self.frame_2)
        self.pbClear_list.setObjectName(u"pbClear_list")

        self.verticalLayout_3.addWidget(self.pbClear_list, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_2)

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
        self.lblDescription.setText(QCoreApplication.translate("Dialog", u"Kinnistud lisatakse lepingule:", None))
        self.lblContractNumber.setText("")
        self.lblContractName.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"N\u00fc\u00fcd on k\u00f5ik vajalik juba aktiveeritud ja saad alustada kohe kinnistute valikuga.", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u" NB! kui varasemalt on kinnituid juba valitud siis need kuvatakse juba tabelis. ", None))
        self.pbClear_list.setText(QCoreApplication.translate("Dialog", u"T\u00fchista valik", None))
    # retranslateUi

