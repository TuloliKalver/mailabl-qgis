# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Kalver\Desktop\Plugins\mailabl-qgis\mailabl-qgis\config\confWidgets\ProjectSetup.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LayeAdjuster(object):
    def setupUi(self, LayeAdjuster):
        LayeAdjuster.setObjectName("LayeAdjuster")
        LayeAdjuster.resize(900, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LayeAdjuster.sizePolicy().hasHeightForWidth())
        LayeAdjuster.setSizePolicy(sizePolicy)
        LayeAdjuster.setMinimumSize(QtCore.QSize(900, 530))
        LayeAdjuster.setMaximumSize(QtCore.QSize(900, 530))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        LayeAdjuster.setFont(font)
        LayeAdjuster.setStyleSheet("\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(LayeAdjuster)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fContent = QtWidgets.QFrame(LayeAdjuster)
        self.fContent.setMinimumSize(QtCore.QSize(0, 100))
        self.fContent.setStyleSheet("")
        self.fContent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fContent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fContent.setObjectName("fContent")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fContent)
        self.horizontalLayout_4.setContentsMargins(0, 10, 10, 10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SettingElements = QtWidgets.QFrame(self.fContent)
        self.SettingElements.setMinimumSize(QtCore.QSize(0, 450))
        self.SettingElements.setStyleSheet("")
        self.SettingElements.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SettingElements.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SettingElements.setObjectName("SettingElements")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.SettingElements)
        self.verticalLayout_9.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.fMainLeft = QtWidgets.QFrame(self.SettingElements)
        self.fMainLeft.setMinimumSize(QtCore.QSize(0, 100))
        self.fMainLeft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fMainLeft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fMainLeft.setObjectName("fMainLeft")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.fMainLeft)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.fSettingsMain = QtWidgets.QFrame(self.fMainLeft)
        self.fSettingsMain.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.fSettingsMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fSettingsMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fSettingsMain.setObjectName("fSettingsMain")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fSettingsMain)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.f_Main_2 = QtWidgets.QFrame(self.fSettingsMain)
        self.f_Main_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_Main_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_Main_2.setObjectName("f_Main_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.f_Main_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.f_Main_3 = QtWidgets.QFrame(self.f_Main_2)
        self.f_Main_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_Main_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_Main_3.setObjectName("f_Main_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.f_Main_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblCurrect_Cadastral_2 = QtWidgets.QLabel(self.f_Main_3)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lblCurrect_Cadastral_2.setFont(font)
        self.lblCurrect_Cadastral_2.setObjectName("lblCurrect_Cadastral_2")
        self.horizontalLayout_3.addWidget(self.lblCurrect_Cadastral_2, 0, QtCore.Qt.AlignLeft)
        self.cmbProjects_Layer = QtWidgets.QComboBox(self.f_Main_3)
        self.cmbProjects_Layer.setMinimumSize(QtCore.QSize(0, 0))
        self.cmbProjects_Layer.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbProjects_Layer.setFont(font)
        self.cmbProjects_Layer.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbProjects_Layer.setIconSize(QtCore.QSize(6, 6))
        self.cmbProjects_Layer.setObjectName("cmbProjects_Layer")
        self.cmbProjects_Layer.addItem("")
        self.cmbProjects_Layer.setItemText(0, "")
        self.cmbProjects_Layer.addItem("")
        self.cmbProjects_Layer.setItemText(1, "")
        self.cmbProjects_Layer.addItem("")
        self.cmbProjects_Layer.setItemText(2, "")
        self.cmbProjects_Layer.addItem("")
        self.cmbProjects_Layer.setItemText(3, "")
        self.horizontalLayout_3.addWidget(self.cmbProjects_Layer)
        self.verticalLayout_3.addWidget(self.f_Main_3)
        self.verticalLayout_4.addWidget(self.f_Main_2)
        self.f_Main_1 = QtWidgets.QFrame(self.fSettingsMain)
        self.f_Main_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_Main_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_Main_1.setObjectName("f_Main_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.f_Main_1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblCurrect_Cadastral = QtWidgets.QLabel(self.f_Main_1)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lblCurrect_Cadastral.setFont(font)
        self.lblCurrect_Cadastral.setObjectName("lblCurrect_Cadastral")
        self.horizontalLayout.addWidget(self.lblCurrect_Cadastral, 0, QtCore.Qt.AlignLeft)
        self.cmbPreferred_Project_status = QtWidgets.QComboBox(self.f_Main_1)
        self.cmbPreferred_Project_status.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbPreferred_Project_status.setFont(font)
        self.cmbPreferred_Project_status.setObjectName("cmbPreferred_Project_status")
        self.horizontalLayout.addWidget(self.cmbPreferred_Project_status)
        self.verticalLayout_4.addWidget(self.f_Main_1)
        self.verticalLayout_8.addWidget(self.fSettingsMain)
        self.fSettingsFolders = QtWidgets.QFrame(self.fMainLeft)
        self.fSettingsFolders.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fSettingsFolders.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fSettingsFolders.setObjectName("fSettingsFolders")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fSettingsFolders)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Projekcts_FolderSetup_2 = QtWidgets.QFrame(self.fSettingsFolders)
        self.Projekcts_FolderSetup_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Projekcts_FolderSetup_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Projekcts_FolderSetup_2.setObjectName("Projekcts_FolderSetup_2")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout(self.Projekcts_FolderSetup_2)
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_63.setSpacing(10)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.lblProjectsTargetFolder = QtWidgets.QLabel(self.Projekcts_FolderSetup_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblProjectsTargetFolder.setFont(font)
        self.lblProjectsTargetFolder.setObjectName("lblProjectsTargetFolder")
        self.horizontalLayout_63.addWidget(self.lblProjectsTargetFolder, 0, QtCore.Qt.AlignLeft)
        self.leProjectsTargetFolder_location = QtWidgets.QLineEdit(self.Projekcts_FolderSetup_2)
        self.leProjectsTargetFolder_location.setMinimumSize(QtCore.QSize(500, 0))
        self.leProjectsTargetFolder_location.setObjectName("leProjectsTargetFolder_location")
        self.horizontalLayout_63.addWidget(self.leProjectsTargetFolder_location)
        self.verticalLayout_2.addWidget(self.Projekcts_FolderSetup_2)
        self.Projekcts_FolderSetup = QtWidgets.QFrame(self.fSettingsFolders)
        self.Projekcts_FolderSetup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Projekcts_FolderSetup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Projekcts_FolderSetup.setObjectName("Projekcts_FolderSetup")
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout(self.Projekcts_FolderSetup)
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_62.setSpacing(10)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.lblProjectsFolder = QtWidgets.QLabel(self.Projekcts_FolderSetup)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblProjectsFolder.setFont(font)
        self.lblProjectsFolder.setObjectName("lblProjectsFolder")
        self.horizontalLayout_62.addWidget(self.lblProjectsFolder)
        self.leProjectsFolder_location = QtWidgets.QLineEdit(self.Projekcts_FolderSetup)
        self.leProjectsFolder_location.setMinimumSize(QtCore.QSize(500, 0))
        self.leProjectsFolder_location.setObjectName("leProjectsFolder_location")
        self.horizontalLayout_62.addWidget(self.leProjectsFolder_location)
        self.verticalLayout_2.addWidget(self.Projekcts_FolderSetup)
        self.frame_22 = QtWidgets.QFrame(self.fSettingsFolders)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.lblPhtoslabel = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblPhtoslabel.setFont(font)
        self.lblPhtoslabel.setObjectName("lblPhtoslabel")
        self.horizontalLayout_35.addWidget(self.lblPhtoslabel)
        self.lePhotos = QtWidgets.QLineEdit(self.frame_22)
        self.lePhotos.setObjectName("lePhotos")
        self.horizontalLayout_35.addWidget(self.lePhotos)
        self.verticalLayout_2.addWidget(self.frame_22)
        self.verticalLayout_8.addWidget(self.fSettingsFolders)
        self.fSettingsFolderStucture = QtWidgets.QFrame(self.fMainLeft)
        self.fSettingsFolderStucture.setMinimumSize(QtCore.QSize(0, 100))
        self.fSettingsFolderStucture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fSettingsFolderStucture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fSettingsFolderStucture.setObjectName("fSettingsFolderStucture")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.fSettingsFolderStucture)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox = QtWidgets.QGroupBox(self.fSettingsFolderStucture)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cmbNameElements = QtWidgets.QComboBox(self.frame_2)
        self.cmbNameElements.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbNameElements.setFont(font)
        self.cmbNameElements.setObjectName("cmbNameElements")
        self.cmbNameElements.addItem("")
        self.cmbNameElements.addItem("")
        self.cmbNameElements.addItem("")
        self.horizontalLayout_5.addWidget(self.cmbNameElements)
        self.Confir_selecteded_element = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Confir_selecteded_element.setFont(font)
        self.Confir_selecteded_element.setObjectName("Confir_selecteded_element")
        self.horizontalLayout_5.addWidget(self.Confir_selecteded_element)
        self.verticalLayout_13.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft)
        self.leSymbolCharacter = QtWidgets.QLineEdit(self.frame_4)
        self.leSymbolCharacter.setMinimumSize(QtCore.QSize(400, 0))
        self.leSymbolCharacter.setMaximumSize(QtCore.QSize(300, 16777215))
        self.leSymbolCharacter.setMaxLength(5)
        self.leSymbolCharacter.setPlaceholderText("")
        self.leSymbolCharacter.setObjectName("leSymbolCharacter")
        self.verticalLayout_13.addWidget(self.leSymbolCharacter)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblPreferedFolderNamStructure = QtWidgets.QLabel(self.frame_3)
        self.lblPreferedFolderNamStructure.setMinimumSize(QtCore.QSize(400, 0))
        self.lblPreferedFolderNamStructure.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lblPreferedFolderNamStructure.setText("")
        self.lblPreferedFolderNamStructure.setObjectName("lblPreferedFolderNamStructure")
        self.horizontalLayout_6.addWidget(self.lblPreferedFolderNamStructure)
        self.pbResetFolderSetup = QtWidgets.QPushButton(self.frame_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\config\\confWidgets\\../../icons/Icons_hele/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbResetFolderSetup.setIcon(icon)
        self.pbResetFolderSetup.setObjectName("pbResetFolderSetup")
        self.horizontalLayout_6.addWidget(self.pbResetFolderSetup, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.verticalLayout_7.addWidget(self.frame)
        self.verticalLayout_11.addWidget(self.groupBox)
        self.verticalLayout_8.addWidget(self.fSettingsFolderStucture)
        spacerItem = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.fButtons = QtWidgets.QFrame(self.fMainLeft)
        self.fButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fButtons.setObjectName("fButtons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fButtons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(411, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pbCancel = QtWidgets.QPushButton(self.fButtons)
        self.pbCancel.setIcon(icon)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_2.addWidget(self.pbCancel)
        self.pbSave = QtWidgets.QPushButton(self.fButtons)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.pbSave.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Kalver\\Desktop\\Plugins\\mailabl-qgis\\mailabl-qgis\\config\\confWidgets\\../../icons/Icons_hele/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSave.setIcon(icon1)
        self.pbSave.setIconSize(QtCore.QSize(16, 16))
        self.pbSave.setObjectName("pbSave")
        self.horizontalLayout_2.addWidget(self.pbSave)
        self.verticalLayout_8.addWidget(self.fButtons)
        self.verticalLayout_9.addWidget(self.fMainLeft)
        self.horizontalLayout_4.addWidget(self.SettingElements)
        self.fHelpMenu = QtWidgets.QFrame(self.fContent)
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
        self.label_2 = QtWidgets.QLabel(self.fHelpMenu)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.fHelpMenu)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_10.addWidget(self.textEdit)
        self.horizontalLayout_4.addWidget(self.fHelpMenu)
        self.verticalLayout.addWidget(self.fContent)

        self.retranslateUi(LayeAdjuster)
        self.cmbNameElements.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(LayeAdjuster)

    def retranslateUi(self, LayeAdjuster):
        _translate = QtCore.QCoreApplication.translate
        LayeAdjuster.setWindowTitle(_translate("LayeAdjuster", "Projektide seaded"))
        self.lblCurrect_Cadastral_2.setText(_translate("LayeAdjuster", "Kaardikiht"))
        self.lblCurrect_Cadastral.setText(_translate("LayeAdjuster", "Eelistatud staatus"))
        self.lblProjectsTargetFolder.setText(_translate("LayeAdjuster", "Projekti sihtkaus"))
        self.lblProjectsFolder.setText(_translate("LayeAdjuster", "Projekti baaskaust"))
        self.lblPhtoslabel.setText(_translate("LayeAdjuster", "Projekti fotod*"))
        self.groupBox.setTitle(_translate("LayeAdjuster", "Projekti kausta nime seadistamine"))
        self.cmbNameElements.setPlaceholderText(_translate("LayeAdjuster", "Vali element"))
        self.cmbNameElements.setItemText(0, _translate("LayeAdjuster", "Projekti number"))
        self.cmbNameElements.setItemText(1, _translate("LayeAdjuster", "Sümbol"))
        self.cmbNameElements.setItemText(2, _translate("LayeAdjuster", "Projekti nimetus"))
        self.Confir_selecteded_element.setText(_translate("LayeAdjuster", "Lisa"))
        self.pbResetFolderSetup.setText(_translate("LayeAdjuster", "Seadista uuesti"))
        self.pbCancel.setText(_translate("LayeAdjuster", "Tühista"))
        self.pbSave.setText(_translate("LayeAdjuster", "Salvesta"))
        self.label_2.setText(_translate("LayeAdjuster", "Seadete selgitused"))
        self.textEdit.setHtml(_translate("LayeAdjuster", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Kaardikiht*:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; text-decoration: underline;\">NB! Omadus on loomisel ja luuakse koos vajalike tööriistadega.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">See on funktsionaalsus, kus projekti element seostatakse projekti ala jooniskihiga. Nt vajalik tänavaala detailsem projekti ulatus jne. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Eelistatud kaardikiht:</span><br />...</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Projekti kaust:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;Projekti kaust&quot; on omadus, mis võimaldab genereerida kokkulepitud struktuuriga &quot;baas kaust&quot; ja selle sisu ning paigutada see kokkulepitud asukohta, kokkulepitud nime struktuuri genereerimisega.  Vaata täpsemalt &quot;Projekti kausta nime seadistamisest&quot;. Projekti kausta teekond tuleb lisada täis lingina:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Projekti fotod*:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lisa kausta nimetus, kus hoiustatakse projektiga seotud fotosid.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Eelistatud staatus:</span><br />Millise staatusega projekte eelistad lepingu mooduli avamisel?</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Projekti kausta nime seadistamine:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nime genereerimisel saab kasutada: Projekti nime, &quot;elementi&quot;, projekti numbrit. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">NB! projekti kausta nimedes ei saa kasutada (kuna need ei vasta Windowsi standarditele) järgmisi sümboleid: &quot;&lt;&gt;:&quot;/\\\\|?*.&quot;, </span></p></body></html>"))
