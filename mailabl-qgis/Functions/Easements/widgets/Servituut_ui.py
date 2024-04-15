# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Kalver\Desktop\Plugins\mailabl-qgis\mailabl-qgis\Functions\Easements\widgets\Servituut.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_servituutDialogBase(object):
    def setupUi(self, servituutDialogBase):
        servituutDialogBase.setObjectName("servituutDialogBase")
        servituutDialogBase.resize(900, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(servituutDialogBase.sizePolicy().hasHeightForWidth())
        servituutDialogBase.setSizePolicy(sizePolicy)
        servituutDialogBase.setMinimumSize(QtCore.QSize(900, 750))
        servituutDialogBase.setMaximumSize(QtCore.QSize(900, 750))
        servituutDialogBase.setStyleSheet("#pbClearPuhver2m,#pbClearEvvServituudid\n"
"{\n"
"background-color: qradialgradient(spread:pad, cx:0.494, cy:0.5, radius:0.5, fx:0.42, fy:0.5, stop:0 rgba(218, 0, 0, 232), stop:1 rgba(255, 81, 81, 200));\n"
"    color: rgb(238, 238, 238);\n"
"    border-radiusr: 1px;\n"
"}\n"
"\n"
"\n"
"#leInfo,#leSelectedProperties {\n"
"    border: None;\n"
"    background-color: #272c35;\n"
"    color: #c5c5d2;\n"
"    padding-left: 10px; /* Adjust the left padding as needed */\n"
"    padding-right: 0px; /* Adjust the right padding as needed */\n"
"    padding-top: 0px; /* Adjust the top padding as needed */\n"
"    padding-bottom: 0px; /* Adjust the bottom padding as needed */\n"
"}\n"
"\n"
"/*style the combobox itself*/\n"
"\n"
"#fHeader, #fHelpMenu, \n"
"#fSettingsFolders, #fSettingsFolderStucture,\n"
"#fSettingsMain \n"
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
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(servituutDialogBase)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.fHeading = QtWidgets.QFrame(servituutDialogBase)
        self.fHeading.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fHeading.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fHeading.setObjectName("fHeading")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.fHeading)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_5 = QtWidgets.QLabel(self.fHeading)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6.addWidget(self.fHeading)
        self.fMain = QtWidgets.QFrame(servituutDialogBase)
        self.fMain.setMinimumSize(QtCore.QSize(0, 200))
        self.fMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fMain.setObjectName("fMain")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fMain)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fMainTools = QtWidgets.QFrame(self.fMain)
        self.fMainTools.setStyleSheet("")
        self.fMainTools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fMainTools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fMainTools.setObjectName("fMainTools")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.fMainTools)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.fSelectedItem = QtWidgets.QFrame(self.fMainTools)
        self.fSelectedItem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fSelectedItem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fSelectedItem.setObjectName("fSelectedItem")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.fSelectedItem)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.leInfo = QtWidgets.QLineEdit(self.fSelectedItem)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.leInfo.setFont(font)
        self.leInfo.setReadOnly(True)
        self.leInfo.setObjectName("leInfo")
        self.verticalLayout_7.addWidget(self.leInfo)
        self.lSelectedEasment = QtWidgets.QLabel(self.fSelectedItem)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lSelectedEasment.setFont(font)
        self.lSelectedEasment.setObjectName("lSelectedEasment")
        self.verticalLayout_7.addWidget(self.lSelectedEasment)
        self.fItemSelections = QtWidgets.QFrame(self.fSelectedItem)
        self.fItemSelections.setMinimumSize(QtCore.QSize(0, 77))
        self.fItemSelections.setMaximumSize(QtCore.QSize(16777215, 77))
        self.fItemSelections.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fItemSelections.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fItemSelections.setObjectName("fItemSelections")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fItemSelections)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(self.fItemSelections)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.leSelectedProperties = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.leSelectedProperties.setFont(font)
        self.leSelectedProperties.setReadOnly(True)
        self.leSelectedProperties.setObjectName("leSelectedProperties")
        self.verticalLayout_5.addWidget(self.leSelectedProperties)
        self.tvProperties = QtWidgets.QTableView(self.frame)
        self.tvProperties.setObjectName("tvProperties")
        self.verticalLayout_5.addWidget(self.tvProperties)
        self.horizontalLayout_5.addWidget(self.frame)
        self.frame_6 = QtWidgets.QFrame(self.fItemSelections)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout.setContentsMargins(0, 18, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbValiKinnistu = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbValiKinnistu.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\Functions\\Easements\\widgets\\../../../icons/iconoir--map-pin-plus_asukoht.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbValiKinnistu.setIcon(icon)
        self.pbValiKinnistu.setIconSize(QtCore.QSize(18, 18))
        self.pbValiKinnistu.setObjectName("pbValiKinnistu")
        self.verticalLayout.addWidget(self.pbValiKinnistu)
        self.pbClearCadastrals = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbClearCadastrals.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\Functions\\Easements\\widgets\\../../../icons/Icons_hele/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbClearCadastrals.setIcon(icon1)
        self.pbClearCadastrals.setIconSize(QtCore.QSize(16, 16))
        self.pbClearCadastrals.setObjectName("pbClearCadastrals")
        self.verticalLayout.addWidget(self.pbClearCadastrals)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5.addWidget(self.frame_6)
        self.verticalLayout_7.addWidget(self.fItemSelections)
        self.verticalLayout_9.addWidget(self.fSelectedItem, 0, QtCore.Qt.AlignTop)
        self.fBaseSetup = QtWidgets.QFrame(self.fMainTools)
        self.fBaseSetup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fBaseSetup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fBaseSetup.setObjectName("fBaseSetup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fBaseSetup)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.frame_4 = QtWidgets.QFrame(self.fBaseSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dPuhvriSuurus = QtWidgets.QDial(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dPuhvriSuurus.sizePolicy().hasHeightForWidth())
        self.dPuhvriSuurus.setSizePolicy(sizePolicy)
        self.dPuhvriSuurus.setObjectName("dPuhvriSuurus")
        self.gridLayout_2.addWidget(self.dPuhvriSuurus, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.fBaseSetup)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.cbV = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbV.setChecked(True)
        self.cbV.setObjectName("cbV")
        self.gridLayout_7.addWidget(self.cbV, 0, 0, 1, 2)
        self.cbK = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbK.setChecked(True)
        self.cbK.setObjectName("cbK")
        self.gridLayout_7.addWidget(self.cbK, 1, 0, 1, 2)
        self.cbKSK = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbKSK.setChecked(True)
        self.cbKSK.setObjectName("cbKSK")
        self.gridLayout_7.addWidget(self.cbKSK, 2, 0, 1, 2)
        self.cbKSK_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbKSK_2.setChecked(True)
        self.cbKSK_2.setObjectName("cbKSK_2")
        self.gridLayout_7.addWidget(self.cbKSK_2, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 4, 0, 1, 1)
        self.verticalLayout_11.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_2 = QtWidgets.QFrame(self.fBaseSetup)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pbPuhverYle = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbPuhverYle.setFont(font)
        self.pbPuhverYle.setObjectName("pbPuhverYle")
        self.verticalLayout_12.addWidget(self.pbPuhverYle)
        self.pbTest = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pbTest.setFont(font)
        self.pbTest.setAutoFillBackground(False)
        self.pbTest.setObjectName("pbTest")
        self.verticalLayout_12.addWidget(self.pbTest)
        self.pbKoostaServituut = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pbKoostaServituut.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Icons_a/cloud-lightning.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbKoostaServituut.setIcon(icon2)
        self.pbKoostaServituut.setIconSize(QtCore.QSize(25, 25))
        self.pbKoostaServituut.setObjectName("pbKoostaServituut")
        self.verticalLayout_12.addWidget(self.pbKoostaServituut)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.fBaseSetup)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pbClearPuhver2m = QtWidgets.QPushButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pbClearPuhver2m.setFont(font)
        self.pbClearPuhver2m.setObjectName("pbClearPuhver2m")
        self.verticalLayout_2.addWidget(self.pbClearPuhver2m)
        self.pbClearEvvServituudid = QtWidgets.QPushButton(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbClearEvvServituudid.setFont(font)
        self.pbClearEvvServituudid.setObjectName("pbClearEvvServituudid")
        self.verticalLayout_2.addWidget(self.pbClearEvvServituudid)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_9.addWidget(self.fBaseSetup)
        self.ActionTools = QtWidgets.QFrame(self.fMainTools)
        self.ActionTools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ActionTools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ActionTools.setObjectName("ActionTools")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.ActionTools)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_4 = QtWidgets.QGroupBox(self.ActionTools)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.pbKinnistuAndmed = QtWidgets.QPushButton(self.groupBox_4)
        self.pbKinnistuAndmed.setObjectName("pbKinnistuAndmed")
        self.verticalLayout_4.addWidget(self.pbKinnistuAndmed)
        self.pbServituutInfo = QtWidgets.QPushButton(self.groupBox_4)
        self.pbServituutInfo.setObjectName("pbServituutInfo")
        self.verticalLayout_4.addWidget(self.pbServituutInfo)
        self.horizontalLayout_8.addWidget(self.groupBox_4)
        self.verticalLayout_9.addWidget(self.ActionTools)
        self.tabWidget = QtWidgets.QTabWidget(self.fMainTools)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.tabWidget.setObjectName("tabWidget")
        self.taKinnistuLabel = QtWidgets.QWidget()
        self.taKinnistuLabel.setObjectName("taKinnistuLabel")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.taKinnistuLabel)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lnameKataster = QtWidgets.QLabel(self.taKinnistuLabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnameKataster.sizePolicy().hasHeightForWidth())
        self.lnameKataster.setSizePolicy(sizePolicy)
        self.lnameKataster.setObjectName("lnameKataster")
        self.horizontalLayout_4.addWidget(self.lnameKataster)
        self.laKataster = QtWidgets.QLabel(self.taKinnistuLabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.laKataster.sizePolicy().hasHeightForWidth())
        self.laKataster.setSizePolicy(sizePolicy)
        self.laKataster.setMinimumSize(QtCore.QSize(0, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.laKataster.setFont(font)
        self.laKataster.setObjectName("laKataster")
        self.horizontalLayout_4.addWidget(self.laKataster)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.taKinnistuLabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.laAadress = QtWidgets.QLabel(self.taKinnistuLabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.laAadress.sizePolicy().hasHeightForWidth())
        self.laAadress.setSizePolicy(sizePolicy)
        self.laAadress.setMinimumSize(QtCore.QSize(0, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.laAadress.setFont(font)
        self.laAadress.setObjectName("laAadress")
        self.horizontalLayout_6.addWidget(self.laAadress)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.gridLayout_9.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.taKinnistuLabel, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pbTesting = QtWidgets.QPushButton(self.tab)
        self.pbTesting.setObjectName("pbTesting")
        self.gridLayout_10.addWidget(self.pbTesting, 5, 1, 1, 1)
        self.tbServituut = QtWidgets.QTableWidget(self.tab)
        self.tbServituut.setAlternatingRowColors(True)
        self.tbServituut.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbServituut.setObjectName("tbServituut")
        self.tbServituut.setColumnCount(0)
        self.tbServituut.setRowCount(0)
        self.gridLayout_10.addWidget(self.tbServituut, 2, 0, 5, 1)
        self.pbCountSelectedRows = QtWidgets.QPushButton(self.tab)
        self.pbCountSelectedRows.setObjectName("pbCountSelectedRows")
        self.gridLayout_10.addWidget(self.pbCountSelectedRows, 6, 1, 1, 1)
        self.pbMailabl = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbMailabl.sizePolicy().hasHeightForWidth())
        self.pbMailabl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pbMailabl.setFont(font)
        self.pbMailabl.setObjectName("pbMailabl")
        self.gridLayout_10.addWidget(self.pbMailabl, 2, 1, 1, 1)
        self.pbAddServituutType = QtWidgets.QPushButton(self.tab)
        self.pbAddServituutType.setObjectName("pbAddServituutType")
        self.gridLayout_10.addWidget(self.pbAddServituutType, 4, 1, 1, 1)
        self.cmbValik = QtWidgets.QComboBox(self.tab)
        self.cmbValik.setObjectName("cmbValik")
        self.gridLayout_10.addWidget(self.cmbValik, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(240, 10, 256, 151))
        self.graphicsView.setObjectName("graphicsView")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_9.addWidget(self.tabWidget)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem6)
        self.fButtons = QtWidgets.QFrame(self.fMainTools)
        self.fButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fButtons.setObjectName("fButtons")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.fButtons)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(411, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.pbCancel = QtWidgets.QPushButton(self.fButtons)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\Functions\\Easements\\widgets\\../../icons/Icons_hele/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancel.setIcon(icon3)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_7.addWidget(self.pbCancel)
        self.pbSave = QtWidgets.QPushButton(self.fButtons)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.pbSave.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\Functions\\Easements\\widgets\\../../icons/Icons_hele/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSave.setIcon(icon4)
        self.pbSave.setIconSize(QtCore.QSize(16, 16))
        self.pbSave.setObjectName("pbSave")
        self.horizontalLayout_7.addWidget(self.pbSave)
        self.verticalLayout_9.addWidget(self.fButtons)
        self.horizontalLayout.addWidget(self.fMainTools)
        self.fHelpMenu = QtWidgets.QFrame(self.fMain)
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
        self.label_4 = QtWidgets.QLabel(self.fHelpMenu)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        self.textEdit = QtWidgets.QTextEdit(self.fHelpMenu)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_10.addWidget(self.textEdit)
        self.horizontalLayout.addWidget(self.fHelpMenu)
        self.verticalLayout_6.addWidget(self.fMain)

        self.retranslateUi(servituutDialogBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(servituutDialogBase)

    def retranslateUi(self, servituutDialogBase):
        _translate = QtCore.QCoreApplication.translate
        servituutDialogBase.setWindowTitle(_translate("servituutDialogBase", "servituut"))
        self.label_5.setText(_translate("servituutDialogBase", "NB! tööriist on eksperimentaalne*"))
        self.leInfo.setText(_translate("servituutDialogBase", "Ala koostatakse järgmisele kandele"))
        self.lSelectedEasment.setText(_translate("servituutDialogBase", "Valituut servituudi kanne"))
        self.leSelectedProperties.setText(_translate("servituutDialogBase", "Kinnistud"))
        self.pbValiKinnistu.setText(_translate("servituutDialogBase", "Vali kinnistu"))
        self.pbClearCadastrals.setText(_translate("servituutDialogBase", "Tühista"))
        self.label.setText(_translate("servituutDialogBase", "Puhver: 0"))
        self.groupBox_2.setTitle(_translate("servituutDialogBase", "Torude valimine"))
        self.cbV.setText(_translate("servituutDialogBase", "Veetorud"))
        self.cbK.setText(_translate("servituutDialogBase", "Kanalitorud"))
        self.cbKSK.setText(_translate("servituutDialogBase", "Survekanalitorud"))
        self.cbKSK_2.setText(_translate("servituutDialogBase", "Drenaaž"))
        self.pbPuhverYle.setText(_translate("servituutDialogBase", "Leia torud läheduses"))
        self.pbTest.setText(_translate("servituutDialogBase", "Koosta puhver"))
        self.pbKoostaServituut.setText(_translate("servituutDialogBase", "Koosta servituut"))
        self.groupBox_5.setTitle(_translate("servituutDialogBase", "Reset"))
        self.pbClearPuhver2m.setText(_translate("servituutDialogBase", "2m"))
        self.pbClearEvvServituudid.setText(_translate("servituutDialogBase", "Servituudid"))
        self.groupBox_4.setTitle(_translate("servituutDialogBase", "Lõika kinnistuga"))
        self.pushButton_5.setText(_translate("servituutDialogBase", "Puhver"))
        self.pbKinnistuAndmed.setText(_translate("servituutDialogBase", "Mis see on"))
        self.pbServituutInfo.setText(_translate("servituutDialogBase", "Servituudi info"))
        self.lnameKataster.setText(_translate("servituutDialogBase", "Kataster:"))
        self.laKataster.setText(_translate("servituutDialogBase", "TextLabel"))
        self.label_2.setText(_translate("servituutDialogBase", "Aadress:"))
        self.laAadress.setText(_translate("servituutDialogBase", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.taKinnistuLabel), _translate("servituutDialogBase", "Kinnistu Label"))
        self.pbTesting.setText(_translate("servituutDialogBase", "?"))
        self.pbCountSelectedRows.setText(_translate("servituutDialogBase", "Valitud ridu"))
        self.pbMailabl.setText(_translate("servituutDialogBase", "Mailabl"))
        self.pbAddServituutType.setText(_translate("servituutDialogBase", "Sisesta valik"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("servituutDialogBase", "Servituut"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("servituutDialogBase", "Page"))
        self.pbCancel.setText(_translate("servituutDialogBase", "Tühista"))
        self.pbSave.setText(_translate("servituutDialogBase", "Salvesta"))
        self.label_4.setText(_translate("servituutDialogBase", "Kuidas tööriista kasutada"))
        self.textEdit.setHtml(_translate("servituutDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Juhend on koostamisel</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Vali kinnistu:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Aktiveerib kinnistute aluskihi ning võimaldab valida kinnistuid:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Vali kinnistu</span> vajutades hiirega sobival kinnistul. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Mitme kinnistu</span> valimiseks hoia all Ctrl klahvi.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hoides all Ctrl saad kinnistuid<span style=\" font-style:italic;\"> lisada/või eemaldada</span> valikust.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Tühista:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tühistab varasema kinnistute valiku.</p></body></html>"))
