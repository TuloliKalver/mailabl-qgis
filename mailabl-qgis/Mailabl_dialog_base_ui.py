# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mailabl_dialog_base.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDialog, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableView, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MailablDialogBase(object):
    def setupUi(self, MailablDialogBase):
        if not MailablDialogBase.objectName():
            MailablDialogBase.setObjectName(u"MailablDialogBase")
        MailablDialogBase.resize(1136, 853)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MailablDialogBase.sizePolicy().hasHeightForWidth())
        MailablDialogBase.setSizePolicy(sizePolicy)
        MailablDialogBase.setMaximumSize(QSize(16777215, 16777215))
        MailablDialogBase.setStyleSheet(u"/*\u00fcle\u00fcldine taust ja toonid*/\n"
"/*    *{ \n"
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
"    }\n"
"*/\n"
"\n"
"\n"
"/*\u00fcle\u00fcldine taust ja toonid*/\n"
"*{\n"
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
"#centerMenuSubContainer{\n"
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
"#SetupL"
                        "ayers, #SetupLayers_2, #SetupUserData {\n"
"border: none;\n"
"border-bottom: 1px solid rgb(131, 142, 162);\n"
"}\n"
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
"\n"
"\n"
"\n"
"#UC_Main_Frame QPushButton,#pbChoose_Properties_for_Projects{\n"
"	padding: 1px 8px;\n"
"    border-radiusr: 6px;\n"
"}\n"
"\n"
"#UC_Main_Frame QPushButton:hover{\n"
"\n"
"	padding: 1px 8px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"#wOl_Settings QPushButton{\n"
"	padding: 1px 8px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#wOl_Settings QPushButton:hover{\n"
"	padding: 1px 8px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#rightMenuConta"
                        "iner QPushButton{\n"
"	text-align: right;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"    \n"
"}\n"
"\n"
"#rightMenuContainer QPushButton:hover{\n"
"    text-align: right;\n"
"    border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;  \n"
"}\n"
"\n"
"\n"
"#leftMenuContainer QPushButton{\n"
"	text-align: left;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;	\n"
"}\n"
"#leftMenuContainer QPushButton:hover{\n"
"    text-align: left;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"\n"
"}\n"
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
"	border-radius:"
                        " 8px;\n"
"	height:16px;\n"
"	width: 16px;\n"
"	subcontrol-origin: padding;\n"
"    subcontrol-position: left\n"
"}\n"
"\n"
"QComboBox::on{\n"
"    border: 0.5px solid #acacbe;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(MailablDialogBase)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QFrame(MailablDialogBase)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setStyleSheet(u"")
        self.leftMenuContainer.setFrameShape(QFrame.StyledPanel)
        self.leftMenuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QFrame(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        sizePolicy.setHeightForWidth(self.leftMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuSubContainer.setSizePolicy(sizePolicy)
        self.leftMenuSubContainer.setMaximumSize(QSize(200, 16777215))
        self.leftMenuSubContainer.setFrameShape(QFrame.StyledPanel)
        self.leftMenuSubContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(0, -1, -1, -1)
        self.leftMenuSubContaine_ToggleFrame = QFrame(self.leftMenuSubContainer)
        self.leftMenuSubContaine_ToggleFrame.setObjectName(u"leftMenuSubContaine_ToggleFrame")
        self.leftMenuSubContaine_ToggleFrame.setFrameShape(QFrame.StyledPanel)
        self.leftMenuSubContaine_ToggleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.leftMenuSubContaine_ToggleFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.pbMainMenu = QPushButton(self.leftMenuSubContaine_ToggleFrame)
        self.pbMainMenu.setObjectName(u"pbMainMenu")
        icon = QIcon()
        icon.addFile(u"icons/Icons_hele/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbMainMenu.setIcon(icon)
        self.pbMainMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.pbMainMenu)


        self.verticalLayout_142.addWidget(self.leftMenuSubContaine_ToggleFrame)

        self.leftMenuSubMain = QFrame(self.leftMenuSubContainer)
        self.leftMenuSubMain.setObjectName(u"leftMenuSubMain")
        self.leftMenuSubMain.setStyleSheet(u"")
        self.leftMenuSubMain.setFrameShape(QFrame.StyledPanel)
        self.leftMenuSubMain.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.leftMenuSubMain)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.pbHome = QPushButton(self.leftMenuSubMain)
        self.pbHome.setObjectName(u"pbHome")
        self.pbHome.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"icons/Icons_hele/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbHome.setIcon(icon1)
        self.pbHome.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.pbHome)

        self.pbProjects = QPushButton(self.leftMenuSubMain)
        self.pbProjects.setObjectName(u"pbProjects")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pbProjects.sizePolicy().hasHeightForWidth())
        self.pbProjects.setSizePolicy(sizePolicy1)
        self.pbProjects.setMinimumSize(QSize(24, 0))
        icon2 = QIcon()
        icon2.addFile(u"icons/Icons_hele/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbProjects.setIcon(icon2)
        self.pbProjects.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.pbProjects)

        self.pbContracts_Frame = QFrame(self.leftMenuSubMain)
        self.pbContracts_Frame.setObjectName(u"pbContracts_Frame")
        sizePolicy.setHeightForWidth(self.pbContracts_Frame.sizePolicy().hasHeightForWidth())
        self.pbContracts_Frame.setSizePolicy(sizePolicy)
        self.pbContracts_Frame.setFrameShape(QFrame.StyledPanel)
        self.pbContracts_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.pbContracts_Frame)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.pbContracts_ButtonFrame = QFrame(self.pbContracts_Frame)
        self.pbContracts_ButtonFrame.setObjectName(u"pbContracts_ButtonFrame")
        self.pbContracts_ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.pbContracts_ButtonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.pbContracts_ButtonFrame)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.pbContracts = QPushButton(self.pbContracts_ButtonFrame)
        self.pbContracts.setObjectName(u"pbContracts")
        self.pbContracts.setMinimumSize(QSize(0, 24))
        icon3 = QIcon()
        icon3.addFile(u"icons/Icons_hele/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbContracts.setIcon(icon3)
        self.pbContracts.setIconSize(QSize(20, 20))

        self.verticalLayout_76.addWidget(self.pbContracts)


        self.verticalLayout_79.addWidget(self.pbContracts_ButtonFrame)

        self.pbContracts_SliderFrame = QFrame(self.pbContracts_Frame)
        self.pbContracts_SliderFrame.setObjectName(u"pbContracts_SliderFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pbContracts_SliderFrame.sizePolicy().hasHeightForWidth())
        self.pbContracts_SliderFrame.setSizePolicy(sizePolicy2)
        self.pbContracts_SliderFrame.setMaximumSize(QSize(16777215, 0))
        self.pbContracts_SliderFrame.setFrameShape(QFrame.StyledPanel)
        self.pbContracts_SliderFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.pbContracts_SliderFrame)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(6, 6, 0, 0)
        self.pbPreContacts = QPushButton(self.pbContracts_SliderFrame)
        self.pbPreContacts.setObjectName(u"pbPreContacts")
        self.pbPreContacts.setMinimumSize(QSize(0, 24))
        icon4 = QIcon()
        icon4.addFile(u"icons/Icons_hele/battery-charging.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbPreContacts.setIcon(icon4)
        self.pbPreContacts.setIconSize(QSize(20, 20))

        self.verticalLayout_78.addWidget(self.pbPreContacts)

        self.pbMainContract = QPushButton(self.pbContracts_SliderFrame)
        self.pbMainContract.setObjectName(u"pbMainContract")
        self.pbMainContract.setMinimumSize(QSize(0, 24))
        icon5 = QIcon()
        icon5.addFile(u"icons/Icons_hele/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbMainContract.setIcon(icon5)
        self.pbMainContract.setIconSize(QSize(20, 20))

        self.verticalLayout_78.addWidget(self.pbMainContract)


        self.verticalLayout_79.addWidget(self.pbContracts_SliderFrame, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.pbContracts_Frame)

        self.pbSubstitutes = QPushButton(self.leftMenuSubMain)
        self.pbSubstitutes.setObjectName(u"pbSubstitutes")
        icon6 = QIcon()
        icon6.addFile(u"icons/Icons_hele/codepen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbSubstitutes.setIcon(icon6)
        self.pbSubstitutes.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.pbSubstitutes)

        self.pbMapThemes = QPushButton(self.leftMenuSubMain)
        self.pbMapThemes.setObjectName(u"pbMapThemes")
        icon7 = QIcon()
        icon7.addFile(u"icons/Icons_hele/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbMapThemes.setIcon(icon7)
        self.pbMapThemes.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.pbMapThemes)

        self.pbAddDrawings = QPushButton(self.leftMenuSubMain)
        self.pbAddDrawings.setObjectName(u"pbAddDrawings")
        icon8 = QIcon()
        icon8.addFile(u"icons/Icons_hele/pen-tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbAddDrawings.setIcon(icon8)
        self.pbAddDrawings.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.pbAddDrawings)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.LeftFooter_frame = QFrame(self.leftMenuSubMain)
        self.LeftFooter_frame.setObjectName(u"LeftFooter_frame")
        sizePolicy.setHeightForWidth(self.LeftFooter_frame.sizePolicy().hasHeightForWidth())
        self.LeftFooter_frame.setSizePolicy(sizePolicy)
        self.LeftFooter_frame.setStyleSheet(u"")
        self.LeftFooter_frame.setFrameShape(QFrame.StyledPanel)
        self.LeftFooter_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.LeftFooter_frame)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.pbSettings_ButtonFrame = QFrame(self.LeftFooter_frame)
        self.pbSettings_ButtonFrame.setObjectName(u"pbSettings_ButtonFrame")
        self.pbSettings_ButtonFrame.setStyleSheet(u"")
        self.pbSettings_ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.pbSettings_ButtonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.pbSettings_ButtonFrame)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.pbSettings = QPushButton(self.pbSettings_ButtonFrame)
        self.pbSettings.setObjectName(u"pbSettings")
        self.pbSettings.setMinimumSize(QSize(0, 24))
        self.pbSettings.setToolTipDuration(-1)
        icon9 = QIcon()
        icon9.addFile(u"icons/Icons_hele/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbSettings.setIcon(icon9)
        self.pbSettings.setIconSize(QSize(20, 20))

        self.verticalLayout_58.addWidget(self.pbSettings)


        self.verticalLayout_74.addWidget(self.pbSettings_ButtonFrame)

        self.pbSettings_SliderFrame = QFrame(self.LeftFooter_frame)
        self.pbSettings_SliderFrame.setObjectName(u"pbSettings_SliderFrame")
        sizePolicy2.setHeightForWidth(self.pbSettings_SliderFrame.sizePolicy().hasHeightForWidth())
        self.pbSettings_SliderFrame.setSizePolicy(sizePolicy2)
        self.pbSettings_SliderFrame.setMaximumSize(QSize(16777215, 0))
        self.pbSettings_SliderFrame.setStyleSheet(u"")
        self.pbSettings_SliderFrame.setFrameShape(QFrame.StyledPanel)
        self.pbSettings_SliderFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.pbSettings_SliderFrame)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 6, 0, 0)
        self.pbUpdateData_Frame = QFrame(self.pbSettings_SliderFrame)
        self.pbUpdateData_Frame.setObjectName(u"pbUpdateData_Frame")
        self.pbUpdateData_Frame.setStyleSheet(u"")
        self.pbUpdateData_Frame.setFrameShape(QFrame.StyledPanel)
        self.pbUpdateData_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.pbUpdateData_Frame)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.pbUpdateData_ButtonFrame = QFrame(self.pbUpdateData_Frame)
        self.pbUpdateData_ButtonFrame.setObjectName(u"pbUpdateData_ButtonFrame")
        sizePolicy1.setHeightForWidth(self.pbUpdateData_ButtonFrame.sizePolicy().hasHeightForWidth())
        self.pbUpdateData_ButtonFrame.setSizePolicy(sizePolicy1)
        self.pbUpdateData_ButtonFrame.setMaximumSize(QSize(16777215, 24))
        self.pbUpdateData_ButtonFrame.setStyleSheet(u"")
        self.pbUpdateData_ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.pbUpdateData_ButtonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.pbUpdateData_ButtonFrame)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(6, 0, 0, 0)
        self.pbUpdateData = QPushButton(self.pbUpdateData_ButtonFrame)
        self.pbUpdateData.setObjectName(u"pbUpdateData")
        self.pbUpdateData.setMinimumSize(QSize(0, 24))
        icon10 = QIcon()
        icon10.addFile(u"icons/Icons_hele/download-cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbUpdateData.setIcon(icon10)
        self.pbUpdateData.setIconSize(QSize(20, 20))

        self.verticalLayout_63.addWidget(self.pbUpdateData)


        self.verticalLayout_73.addWidget(self.pbUpdateData_ButtonFrame, 0, Qt.AlignTop)

        self.pbUpdateData_SliderFrame = QFrame(self.pbUpdateData_Frame)
        self.pbUpdateData_SliderFrame.setObjectName(u"pbUpdateData_SliderFrame")
        self.pbUpdateData_SliderFrame.setMaximumSize(QSize(16777215, 0))
        self.pbUpdateData_SliderFrame.setFrameShape(QFrame.StyledPanel)
        self.pbUpdateData_SliderFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.pbUpdateData_SliderFrame)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(12, 6, 0, 6)
        self.pbSettings_AddShapeFile = QPushButton(self.pbUpdateData_SliderFrame)
        self.pbSettings_AddShapeFile.setObjectName(u"pbSettings_AddShapeFile")
        self.pbSettings_AddShapeFile.setMinimumSize(QSize(0, 24))
        icon11 = QIcon()
        icon11.addFile(u"icons/Icons_hele/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbSettings_AddShapeFile.setIcon(icon11)
        self.pbSettings_AddShapeFile.setIconSize(QSize(20, 20))

        self.verticalLayout_71.addWidget(self.pbSettings_AddShapeFile)

        self.pbAvaMaaAmet = QPushButton(self.pbUpdateData_SliderFrame)
        self.pbAvaMaaAmet.setObjectName(u"pbAvaMaaAmet")
        self.pbAvaMaaAmet.setMinimumSize(QSize(0, 24))
        icon12 = QIcon()
        icon12.addFile(u"icons/Icons_hele/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbAvaMaaAmet.setIcon(icon12)
        self.pbAvaMaaAmet.setIconSize(QSize(20, 20))

        self.verticalLayout_71.addWidget(self.pbAvaMaaAmet)


        self.verticalLayout_73.addWidget(self.pbUpdateData_SliderFrame, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.pbUpdateData_Frame)

        self.pbCadastralActions_MainFrame = QFrame(self.pbSettings_SliderFrame)
        self.pbCadastralActions_MainFrame.setObjectName(u"pbCadastralActions_MainFrame")
        self.pbCadastralActions_MainFrame.setStyleSheet(u"")
        self.pbCadastralActions_MainFrame.setFrameShape(QFrame.StyledPanel)
        self.pbCadastralActions_MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.pbCadastralActions_MainFrame)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.pbCadastralActions_ButtonFrame = QFrame(self.pbCadastralActions_MainFrame)
        self.pbCadastralActions_ButtonFrame.setObjectName(u"pbCadastralActions_ButtonFrame")
        sizePolicy1.setHeightForWidth(self.pbCadastralActions_ButtonFrame.sizePolicy().hasHeightForWidth())
        self.pbCadastralActions_ButtonFrame.setSizePolicy(sizePolicy1)
        self.pbCadastralActions_ButtonFrame.setMaximumSize(QSize(16777215, 24))
        self.pbCadastralActions_ButtonFrame.setStyleSheet(u"")
        self.pbCadastralActions_ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.pbCadastralActions_ButtonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.pbCadastralActions_ButtonFrame)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(6, 0, 0, 0)
        self.pbCadasters = QPushButton(self.pbCadastralActions_ButtonFrame)
        self.pbCadasters.setObjectName(u"pbCadasters")
        self.pbCadasters.setMinimumSize(QSize(0, 24))
        icon13 = QIcon()
        icon13.addFile(u"icons/Icons_hele/map.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbCadasters.setIcon(icon13)
        self.pbCadasters.setIconSize(QSize(20, 20))

        self.verticalLayout_64.addWidget(self.pbCadasters)


        self.verticalLayout_65.addWidget(self.pbCadastralActions_ButtonFrame, 0, Qt.AlignTop)

        self.pbCadastraActions_SliderFrame = QFrame(self.pbCadastralActions_MainFrame)
        self.pbCadastraActions_SliderFrame.setObjectName(u"pbCadastraActions_SliderFrame")
        self.pbCadastraActions_SliderFrame.setMaximumSize(QSize(16777215, 0))
        self.pbCadastraActions_SliderFrame.setStyleSheet(u"")
        self.pbCadastraActions_SliderFrame.setFrameShape(QFrame.StyledPanel)
        self.pbCadastraActions_SliderFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.pbCadastraActions_SliderFrame)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(12, 6, 0, 6)
        self.pbSyncMailabl = QPushButton(self.pbCadastraActions_SliderFrame)
        self.pbSyncMailabl.setObjectName(u"pbSyncMailabl")
        self.pbSyncMailabl.setMinimumSize(QSize(0, 24))
        icon14 = QIcon()
        icon14.addFile(u"icons/Icons_hele/cloud-lightning.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbSyncMailabl.setIcon(icon14)
        self.pbSyncMailabl.setIconSize(QSize(20, 20))

        self.verticalLayout_72.addWidget(self.pbSyncMailabl)

        self.pbRefresh = QPushButton(self.pbCadastraActions_SliderFrame)
        self.pbRefresh.setObjectName(u"pbRefresh")
        self.pbRefresh.setMinimumSize(QSize(0, 24))
        icon15 = QIcon()
        icon15.addFile(u"icons/Icons_hele/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbRefresh.setIcon(icon15)
        self.pbRefresh.setIconSize(QSize(20, 20))

        self.verticalLayout_72.addWidget(self.pbRefresh)

        self.pbRemove = QPushButton(self.pbCadastraActions_SliderFrame)
        self.pbRemove.setObjectName(u"pbRemove")
        self.pbRemove.setMinimumSize(QSize(0, 24))
        icon16 = QIcon()
        icon16.addFile(u"icons/Icons_hele/minus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbRemove.setIcon(icon16)
        self.pbRemove.setIconSize(QSize(20, 20))

        self.verticalLayout_72.addWidget(self.pbRemove)

        self.pbExpand = QPushButton(self.pbCadastraActions_SliderFrame)
        self.pbExpand.setObjectName(u"pbExpand")
        self.pbExpand.setMinimumSize(QSize(0, 24))
        icon17 = QIcon()
        icon17.addFile(u"icons/Icons_hele/plus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbExpand.setIcon(icon17)
        self.pbExpand.setIconSize(QSize(20, 20))

        self.verticalLayout_72.addWidget(self.pbExpand)


        self.verticalLayout_65.addWidget(self.pbCadastraActions_SliderFrame, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.pbCadastralActions_MainFrame)


        self.verticalLayout_74.addWidget(self.pbSettings_SliderFrame, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.LeftFooter_frame)


        self.verticalLayout_142.addWidget(self.leftMenuSubMain)


        self.verticalLayout_75.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout_6.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QWidget(MailablDialogBase)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.swWorkSpace = QStackedWidget(self.centerMenuSubContainer)
        self.swWorkSpace.setObjectName(u"swWorkSpace")
        self.swWorkSpace.setStyleSheet(u"")
        self.Servituudid = QWidget()
        self.Servituudid.setObjectName(u"Servituudid")
        self.Servituudid.setStyleSheet(u"")
        self.verticalLayout_34 = QVBoxLayout(self.Servituudid)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 10, 0, 10)
        self.ServituutPageName = QWidget(self.Servituudid)
        self.ServituutPageName.setObjectName(u"ServituutPageName")
        self.verticalLayout_50 = QVBoxLayout(self.ServituutPageName)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 10, 0, 10)
        self.ServituuPageNameLabel = QLabel(self.ServituutPageName)
        self.ServituuPageNameLabel.setObjectName(u"ServituuPageNameLabel")
        font = QFont()
        font.setPointSize(13)
        self.ServituuPageNameLabel.setFont(font)
        self.ServituuPageNameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.ServituuPageNameLabel)


        self.verticalLayout_34.addWidget(self.ServituutPageName, 0, Qt.AlignTop)

        self.ServituutMainFrame = QWidget(self.Servituudid)
        self.ServituutMainFrame.setObjectName(u"ServituutMainFrame")
        self.ServituutMainFrame.setStyleSheet(u"")
        self.verticalLayout_36 = QVBoxLayout(self.ServituutMainFrame)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_5)

        self.label_7 = QLabel(self.ServituutMainFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgb(31, 35, 42);")

        self.verticalLayout_36.addWidget(self.label_7)

        self.label = QLabel(self.ServituutMainFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: #272c35;")

        self.verticalLayout_36.addWidget(self.label)

        self.label_8 = QLabel(self.ServituutMainFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: rgb(44, 49, 60);")

        self.verticalLayout_36.addWidget(self.label_8)

        self.label_9 = QLabel(self.ServituutMainFrame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: rgb(52, 59, 71);")

        self.verticalLayout_36.addWidget(self.label_9)

        self.label_4 = QLabel(self.ServituutMainFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: #404957;")

        self.verticalLayout_36.addWidget(self.label_4)

        self.label_24 = QLabel(self.ServituutMainFrame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"background-color: #626e84;")

        self.verticalLayout_36.addWidget(self.label_24)

        self.label_17 = QLabel(self.ServituutMainFrame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"background-color: rgb(131, 142, 162);")

        self.verticalLayout_36.addWidget(self.label_17)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_6)


        self.verticalLayout_34.addWidget(self.ServituutMainFrame)

        self.ServituutPageFooter = QWidget(self.Servituudid)
        self.ServituutPageFooter.setObjectName(u"ServituutPageFooter")
        self.horizontalLayout_14 = QHBoxLayout(self.ServituutPageFooter)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_25 = QLabel(self.ServituutPageFooter)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_14.addWidget(self.label_25)


        self.verticalLayout_34.addWidget(self.ServituutPageFooter, 0, Qt.AlignBottom)

        self.swWorkSpace.addWidget(self.Servituudid)
        self.Cadastralmoves = QWidget()
        self.Cadastralmoves.setObjectName(u"Cadastralmoves")
        self.verticalLayout_5 = QVBoxLayout(self.Cadastralmoves)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.CadastralPageName = QWidget(self.Cadastralmoves)
        self.CadastralPageName.setObjectName(u"CadastralPageName")
        self.verticalLayout_49 = QVBoxLayout(self.CadastralPageName)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.CadastralMovesMainLabel = QLabel(self.CadastralPageName)
        self.CadastralMovesMainLabel.setObjectName(u"CadastralMovesMainLabel")
        self.CadastralMovesMainLabel.setFont(font)

        self.verticalLayout_49.addWidget(self.CadastralMovesMainLabel, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.CadastralPageName)

        self.swCadastral_sub_processes = QStackedWidget(self.Cadastralmoves)
        self.swCadastral_sub_processes.setObjectName(u"swCadastral_sub_processes")
        self.swCadastral_sub_processes.setStyleSheet(u"*{\n"
"background-color: transparent\n"
"}\n"
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
"    \n"
"	color: rgb(255, 255, 255);\n"
"	padding: 2px 8px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#FrDel_County_Heading,\n"
"#FrDel_State_Heading,\n"
"#FrDel_City_Heading,\n"
"#FrSync_County_Heading,\n"
"#FrSync_State_Heading,\n"
"#FrSync_City_Heading,\n"
"#FrSync_County,\n"
"#FrSync_State,\n"
"#FrSync_City,\n"
"#frame_10,#frame_8,\n"
" #frame_9,\n"
"#tblvResults_Confirm,\n"
"#tblvResults_streets_Confirm,\n"
"#Add_cadastrals,#Preview_frame,\n"
"#lwDelete_Conty_Names{\n"
"        border: 1px solid #2c313c;\n"
"        border-radius: 3px;\n"
"    }\n"
"\n"
"#lblDel_County,\n"
"#lblDel_State,\n"
"#lblDel_City,\n"
"#lblCounty,\n"
"#lblCity,\n"
"#lblState,\n"
"#lblSync_Cou"
                        "nty,\n"
"#lblSync_State,\n"
"#lblSync_City {\n"
"    border-bottom: 1px solid #2c313c; /* Set the bottom border width to 1px */\n"
"    border-radius: 1px;\n"
"    width: 50%; /* Set the width of the border to 50% of the element's width */\n"
"}\n"
"\n"
"/* Apply a bottom border with a solid line */\n"
"#leSync_UseNameInputFor_Layer  {\n"
"  border-bottom: 1px solid rgb(255, 255, 255); /* Replace #000 with the desired color */\n"
"}\n"
"\n"
"")
        self.swAdd_cadastrals = QWidget()
        self.swAdd_cadastrals.setObjectName(u"swAdd_cadastrals")
        self.swAdd_cadastrals.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.swAdd_cadastrals)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Add_cadastrals = QFrame(self.swAdd_cadastrals)
        self.Add_cadastrals.setObjectName(u"Add_cadastrals")
        self.Add_cadastrals.setMinimumSize(QSize(0, 600))
        self.Add_cadastrals.setStyleSheet(u"*\n"
"{\n"
"background-color: transparent\n"
"}\n"
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
"    \n"
"	color: rgb(255, 255, 255);\n"
"	padding: 2px 8px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QListWidget{\n"
"background-color: rgb(52, 59, 71)\n"
"}\n"
"/***\n"
"QTableView{\n"
"background-color: rgb(52, 59, 71)\n"
"}\n"
"***/\n"
"QLineEdit{\n"
"background-color: rgb(52, 59, 71)\n"
"}")
        self.Add_cadastrals.setFrameShape(QFrame.StyledPanel)
        self.Add_cadastrals.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Add_cadastrals)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.wCadastrals_selector = QWidget(self.Add_cadastrals)
        self.wCadastrals_selector.setObjectName(u"wCadastrals_selector")
        self.wCadastrals_selector.setStyleSheet(u"")
        self.verticalLayout_54 = QVBoxLayout(self.wCadastrals_selector)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.wOlAndmed_LabelHolder = QFrame(self.wCadastrals_selector)
        self.wOlAndmed_LabelHolder.setObjectName(u"wOlAndmed_LabelHolder")
        self.wOlAndmed_LabelHolder.setFrameShape(QFrame.StyledPanel)
        self.wOlAndmed_LabelHolder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.wOlAndmed_LabelHolder)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 3, 6, 3)
        self.label_29 = QLabel(self.wOlAndmed_LabelHolder)
        self.label_29.setObjectName(u"label_29")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_29.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_29)

        self.lblCount = QLabel(self.wOlAndmed_LabelHolder)
        self.lblCount.setObjectName(u"lblCount")
        self.lblCount.setFont(font1)

        self.horizontalLayout_3.addWidget(self.lblCount)

        self.label_11 = QLabel(self.wOlAndmed_LabelHolder)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.leSearch_Add = QLineEdit(self.wOlAndmed_LabelHolder)
        self.leSearch_Add.setObjectName(u"leSearch_Add")
        self.leSearch_Add.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.leSearch_Add)

        self.pbSearch_Add = QPushButton(self.wOlAndmed_LabelHolder)
        self.pbSearch_Add.setObjectName(u"pbSearch_Add")
        icon18 = QIcon()
        icon18.addFile(u"icons/Icons_hele/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbSearch_Add.setIcon(icon18)
        self.pbSearch_Add.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.pbSearch_Add)

        self.pbCooseFromMap_Add = QPushButton(self.wOlAndmed_LabelHolder)
        self.pbCooseFromMap_Add.setObjectName(u"pbCooseFromMap_Add")
        icon19 = QIcon()
        icon19.addFile(u"icons/Icons_hele/mouse-pointer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbCooseFromMap_Add.setIcon(icon19)
        self.pbCooseFromMap_Add.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.pbCooseFromMap_Add)


        self.verticalLayout_54.addWidget(self.wOlAndmed_LabelHolder)

        self.Frame_Selector_MainFrame = QFrame(self.wCadastrals_selector)
        self.Frame_Selector_MainFrame.setObjectName(u"Frame_Selector_MainFrame")
        self.Frame_Selector_MainFrame.setStyleSheet(u"")
        self.Frame_Selector_MainFrame.setFrameShape(QFrame.StyledPanel)
        self.Frame_Selector_MainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.Frame_Selector_MainFrame)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Frame_Selector_County = QFrame(self.Frame_Selector_MainFrame)
        self.Frame_Selector_County.setObjectName(u"Frame_Selector_County")
        self.Frame_Selector_County.setStyleSheet(u"")
        self.Frame_Selector_County.setFrameShape(QFrame.StyledPanel)
        self.Frame_Selector_County.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.Frame_Selector_County)
        self.verticalLayout_53.setSpacing(6)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(3, 6, 3, 0)
        self.frame_10 = QFrame(self.Frame_Selector_County)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 46))
        self.frame_10.setMaximumSize(QSize(16777215, 46))
        self.frame_10.setStyleSheet(u"   #frame_10 {\n"
"\n"
"        border: 1px solid #2c313c;\n"
"        border-radius: 3px;\n"
"		\n"
"    }\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(3, 3, 3, 3)
        self.Frame_Tools_County = QFrame(self.frame_10)
        self.Frame_Tools_County.setObjectName(u"Frame_Tools_County")
        self.Frame_Tools_County.setMinimumSize(QSize(0, 25))
        self.Frame_Tools_County.setStyleSheet(u"")
        self.Frame_Tools_County.setFrameShape(QFrame.StyledPanel)
        self.Frame_Tools_County.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Frame_Tools_County)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 0, 6, 0)
        self.lblCounty = QLabel(self.Frame_Tools_County)
        self.lblCounty.setObjectName(u"lblCounty")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.lblCounty.setFont(font2)

        self.horizontalLayout_4.addWidget(self.lblCounty, 0, Qt.AlignTop)

        self.pbDone_County = QPushButton(self.Frame_Tools_County)
        self.pbDone_County.setObjectName(u"pbDone_County")

        self.horizontalLayout_4.addWidget(self.pbDone_County, 0, Qt.AlignRight)


        self.verticalLayout_28.addWidget(self.Frame_Tools_County, 0, Qt.AlignTop)

        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_28.addWidget(self.label_12)


        self.verticalLayout_53.addWidget(self.frame_10)

        self.listWidget_county = QListWidget(self.Frame_Selector_County)
        self.listWidget_county.setObjectName(u"listWidget_county")
        self.listWidget_county.setStyleSheet(u"")

        self.verticalLayout_53.addWidget(self.listWidget_county)


        self.horizontalLayout_13.addWidget(self.Frame_Selector_County)

        self.Frame_Selector_State = QFrame(self.Frame_Selector_MainFrame)
        self.Frame_Selector_State.setObjectName(u"Frame_Selector_State")
        self.Frame_Selector_State.setStyleSheet(u"")
        self.Frame_Selector_State.setFrameShape(QFrame.StyledPanel)
        self.Frame_Selector_State.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.Frame_Selector_State)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(3, 6, 3, 0)
        self.frame_8 = QFrame(self.Frame_Selector_State)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 46))
        self.frame_8.setMaximumSize(QSize(16777215, 46))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_8)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(3, 3, 3, 3)
        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_11)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 6, 0)
        self.lblState = QLabel(self.frame_11)
        self.lblState.setObjectName(u"lblState")
        self.lblState.setFont(font2)

        self.horizontalLayout.addWidget(self.lblState)

        self.pbDone_State = QPushButton(self.frame_11)
        self.pbDone_State.setObjectName(u"pbDone_State")
        self.pbDone_State.setIconSize(QSize(14, 14))
        self.pbDone_State.setFlat(False)

        self.horizontalLayout.addWidget(self.pbDone_State, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.cbChooseAll_States = QCheckBox(self.frame_8)
        self.cbChooseAll_States.setObjectName(u"cbChooseAll_States")

        self.verticalLayout_26.addWidget(self.cbChooseAll_States)


        self.verticalLayout_33.addWidget(self.frame_8)

        self.listWidget_State = QListWidget(self.Frame_Selector_State)
        self.listWidget_State.setObjectName(u"listWidget_State")
        self.listWidget_State.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.listWidget_State)


        self.horizontalLayout_13.addWidget(self.Frame_Selector_State)

        self.Frame_Selector_City = QFrame(self.Frame_Selector_MainFrame)
        self.Frame_Selector_City.setObjectName(u"Frame_Selector_City")
        self.Frame_Selector_City.setStyleSheet(u"")
        self.Frame_Selector_City.setFrameShape(QFrame.StyledPanel)
        self.Frame_Selector_City.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.Frame_Selector_City)
        self.verticalLayout_52.setSpacing(6)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(3, 6, 3, 0)
        self.frame_9 = QFrame(self.Frame_Selector_City)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 46))
        self.frame_9.setMaximumSize(QSize(16777215, 46))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_9)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(3, 3, 3, 3)
        self.Frame_Tools_City = QFrame(self.frame_9)
        self.Frame_Tools_City.setObjectName(u"Frame_Tools_City")
        self.Frame_Tools_City.setMinimumSize(QSize(0, 25))
        self.Frame_Tools_City.setStyleSheet(u"")
        self.Frame_Tools_City.setFrameShape(QFrame.StyledPanel)
        self.Frame_Tools_City.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.Frame_Tools_City)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(6, 0, 6, 0)
        self.lblCity = QLabel(self.Frame_Tools_City)
        self.lblCity.setObjectName(u"lblCity")
        self.lblCity.setFont(font2)

        self.horizontalLayout_28.addWidget(self.lblCity, 0, Qt.AlignTop)

        self.pbDoneCity = QPushButton(self.Frame_Tools_City)
        self.pbDoneCity.setObjectName(u"pbDoneCity")
        self.pbDoneCity.setIconSize(QSize(14, 14))

        self.horizontalLayout_28.addWidget(self.pbDoneCity, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.Frame_Tools_City, 0, Qt.AlignTop)

        self.cbChooseAll_Cities = QCheckBox(self.frame_9)
        self.cbChooseAll_Cities.setObjectName(u"cbChooseAll_Cities")

        self.verticalLayout_27.addWidget(self.cbChooseAll_Cities)


        self.verticalLayout_52.addWidget(self.frame_9)

        self.listWidget_City = QListWidget(self.Frame_Selector_City)
        self.listWidget_City.setObjectName(u"listWidget_City")
        self.listWidget_City.setStyleSheet(u"")

        self.verticalLayout_52.addWidget(self.listWidget_City)


        self.horizontalLayout_13.addWidget(self.Frame_Selector_City)


        self.verticalLayout_54.addWidget(self.Frame_Selector_MainFrame)


        self.verticalLayout_3.addWidget(self.wCadastrals_selector)

        self.Preview_frame = QFrame(self.Add_cadastrals)
        self.Preview_frame.setObjectName(u"Preview_frame")
        self.Preview_frame.setStyleSheet(u"")
        self.Preview_frame.setFrameShape(QFrame.StyledPanel)
        self.Preview_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Preview_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_Propertie_list = QTabWidget(self.Preview_frame)
        self.tabWidget_Propertie_list.setObjectName(u"tabWidget_Propertie_list")
        self.tabKinnistud = QWidget()
        self.tabKinnistud.setObjectName(u"tabKinnistud")
        self.tabKinnistud.setStyleSheet(u"#tabKinnistud\n"
"{\n"
"	background-color: transparent\n"
"}")
        self.verticalLayout_29 = QVBoxLayout(self.tabKinnistud)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.Preview_frame_2 = QFrame(self.tabKinnistud)
        self.Preview_frame_2.setObjectName(u"Preview_frame_2")
        self.Preview_frame_2.setFrameShape(QFrame.StyledPanel)
        self.Preview_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.Preview_frame_2)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.Preview_frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(6, 0, 0, 0)
        self.cbChooseAllAdd_properties = QCheckBox(self.frame_17)
        self.cbChooseAllAdd_properties.setObjectName(u"cbChooseAllAdd_properties")
        self.cbChooseAllAdd_properties.setIconSize(QSize(16, 16))

        self.horizontalLayout_18.addWidget(self.cbChooseAllAdd_properties)

        self.cbOnPropertiesTab_Include_streets = QCheckBox(self.frame_17)
        self.cbOnPropertiesTab_Include_streets.setObjectName(u"cbOnPropertiesTab_Include_streets")

        self.horizontalLayout_18.addWidget(self.cbOnPropertiesTab_Include_streets)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_14)


        self.verticalLayout_30.addWidget(self.frame_17)

        self.frame_12 = QFrame(self.Preview_frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.tblvResults_Confirm = QTableView(self.frame_12)
        self.tblvResults_Confirm.setObjectName(u"tblvResults_Confirm")

        self.horizontalLayout_11.addWidget(self.tblvResults_Confirm)


        self.verticalLayout_30.addWidget(self.frame_12)


        self.verticalLayout_29.addWidget(self.Preview_frame_2)

        self.tabWidget_Propertie_list.addTab(self.tabKinnistud, "")
        self.tabTranspordimaad = QWidget()
        self.tabTranspordimaad.setObjectName(u"tabTranspordimaad")
        self.verticalLayout_31 = QVBoxLayout(self.tabTranspordimaad)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.Preview_frame_3 = QFrame(self.tabTranspordimaad)
        self.Preview_frame_3.setObjectName(u"Preview_frame_3")
        self.Preview_frame_3.setFrameShape(QFrame.StyledPanel)
        self.Preview_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.Preview_frame_3)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.Preview_frame_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(6, 0, 0, 0)
        self.cbChooseAllAdd__street_properties = QCheckBox(self.frame_18)
        self.cbChooseAllAdd__street_properties.setObjectName(u"cbChooseAllAdd__street_properties")

        self.horizontalLayout_32.addWidget(self.cbChooseAllAdd__street_properties)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_15)

        self.pbConfirm_streets_action = QPushButton(self.frame_18)
        self.pbConfirm_streets_action.setObjectName(u"pbConfirm_streets_action")

        self.horizontalLayout_32.addWidget(self.pbConfirm_streets_action)


        self.verticalLayout_32.addWidget(self.frame_18)

        self.tblvResults_streets_Confirm = QTableView(self.Preview_frame_3)
        self.tblvResults_streets_Confirm.setObjectName(u"tblvResults_streets_Confirm")

        self.verticalLayout_32.addWidget(self.tblvResults_streets_Confirm)

        self.frame_13 = QFrame(self.Preview_frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(3, 3, 3, 3)
        self.horizontalSpacer_8 = QSpacerItem(658, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.pbCancel_streets_reset = QPushButton(self.frame_13)
        self.pbCancel_streets_reset.setObjectName(u"pbCancel_streets_reset")

        self.horizontalLayout_12.addWidget(self.pbCancel_streets_reset)


        self.verticalLayout_32.addWidget(self.frame_13)


        self.verticalLayout_31.addWidget(self.Preview_frame_3)

        self.tabWidget_Propertie_list.addTab(self.tabTranspordimaad, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_143 = QVBoxLayout(self.tab)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.tblNew = QTableView(self.tab)
        self.tblNew.setObjectName(u"tblNew")

        self.verticalLayout_143.addWidget(self.tblNew)

        self.tabWidget_Propertie_list.addTab(self.tab, "")

        self.verticalLayout_4.addWidget(self.tabWidget_Propertie_list)

        self.frame_3 = QFrame(self.Preview_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalSpacer_10 = QSpacerItem(658, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.pbConfirm_action = QPushButton(self.frame_3)
        self.pbConfirm_action.setObjectName(u"pbConfirm_action")
        icon20 = QIcon()
        icon20.addFile(u"icons/Icons_hele/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pbConfirm_action.setIcon(icon20)
        self.pbConfirm_action.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.pbConfirm_action)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.Preview_frame)


        self.verticalLayout_14.addWidget(self.Add_cadastrals)

        self.swCadastral_sub_processes.addWidget(self.swAdd_cadastrals)
        self.swRemove_cadastrals = QWidget()
        self.swRemove_cadastrals.setObjectName(u"swRemove_cadastrals")
        self.swRemove_cadastrals.setStyleSheet(u"QgsCheckableCombobox{\n"
"\n"
"background-color: rgb(52, 59, 71)\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.swRemove_cadastrals)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.wdDel_Cadastrals_Main = QWidget(self.swRemove_cadastrals)
        self.wdDel_Cadastrals_Main.setObjectName(u"wdDel_Cadastrals_Main")
        self.wdDel_Cadastrals_Main.setStyleSheet(u"*\n"
"{\n"
"	background-color:transparent;\n"
"}\n"
"#QProgressBar\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
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
"    \n"
"	color: rgb(255, 255, 255);\n"
"	padding: 2px 8px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QgsCheckableComboBox{\n"
"\n"
"background-color: rgb(52, 59, 71)\n"
"}\n"
"\n"
"QComboBox{\n"
"\n"
"background-color: rgb(52, 59, 71)\n"
"}\n"
"QListWidget{\n"
"background-color: rgb(52, 59, 71)\n"
"}\n"
"/***\n"
"QTableView{\n"
"background-color: rgb(52, 59, 71)\n"
"}\n"
"***/\n"
"QLineEdit{\n"
"background-color: rgb(52, 59, 71)\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.wdDel_Cadastrals_Main)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.wDel_cadastrals_Top = QWidget(self.wdDel_Cadastrals_Main)
        self.wDel_cadastrals_Top.setObjectName(u"wDel_cadastrals_Top")
        self.wDel_cadastrals_Top.setStyleSheet(u"")
        self.verticalLayout_70 = QVBoxLayout(self.wDel_cadastrals_Top)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frDel_Overview_Main = QFrame(self.wDel_cadastrals_Top)
        self.frDel_Overview_Main.setObjectName(u"frDel_Overview_Main")
        self.frDel_Overview_Main.setFrameShape(QFrame.StyledPanel)
        self.frDel_Overview_Main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frDel_Overview_Main)
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(6, 3, 6, 3)
        self.lblDel_Main_txt = QLabel(self.frDel_Overview_Main)
        self.lblDel_Main_txt.setObjectName(u"lblDel_Main_txt")
        self.lblDel_Main_txt.setFont(font1)

        self.horizontalLayout_9.addWidget(self.lblDel_Main_txt)

        self.lblDel_Amount = QLabel(self.frDel_Overview_Main)
        self.lblDel_Amount.setObjectName(u"lblDel_Amount")
        self.lblDel_Amount.setFont(font1)

        self.horizontalLayout_9.addWidget(self.lblDel_Amount)

        self.lblDel_sub_txt = QLabel(self.frDel_Overview_Main)
        self.lblDel_sub_txt.setObjectName(u"lblDel_sub_txt")
        self.lblDel_sub_txt.setFont(font1)

        self.horizontalLayout_9.addWidget(self.lblDel_sub_txt)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_16)

        self.lblDel_Aditiona_txt = QLineEdit(self.frDel_Overview_Main)
        self.lblDel_Aditiona_txt.setObjectName(u"lblDel_Aditiona_txt")
        self.lblDel_Aditiona_txt.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.lblDel_Aditiona_txt)


        self.verticalLayout_70.addWidget(self.frDel_Overview_Main)

        self.FrDel_Selector_MainFrame = QFrame(self.wDel_cadastrals_Top)
        self.FrDel_Selector_MainFrame.setObjectName(u"FrDel_Selector_MainFrame")
        self.FrDel_Selector_MainFrame.setStyleSheet(u"")
        self.FrDel_Selector_MainFrame.setFrameShape(QFrame.StyledPanel)
        self.FrDel_Selector_MainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.FrDel_Selector_MainFrame)
        self.horizontalLayout_16.setSpacing(2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.FrDel_Couty = QFrame(self.FrDel_Selector_MainFrame)
        self.FrDel_Couty.setObjectName(u"FrDel_Couty")
        self.FrDel_Couty.setStyleSheet(u"")
        self.FrDel_Couty.setFrameShape(QFrame.StyledPanel)
        self.FrDel_Couty.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.FrDel_Couty)
        self.verticalLayout_104.setSpacing(6)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(3, 6, 3, 0)
        self.FrDel_County_Heading = QFrame(self.FrDel_Couty)
        self.FrDel_County_Heading.setObjectName(u"FrDel_County_Heading")
        self.FrDel_County_Heading.setMinimumSize(QSize(0, 46))
        self.FrDel_County_Heading.setMaximumSize(QSize(16777215, 46))
        self.FrDel_County_Heading.setStyleSheet(u"   #frame_10 {\n"
"\n"
"        border: 1px solid #2c313c;\n"
"        border-radius: 3px;\n"
"		\n"
"    }\n"
"")
        self.FrDel_County_Heading.setFrameShape(QFrame.StyledPanel)
        self.FrDel_County_Heading.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.FrDel_County_Heading)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(3, 3, 3, 3)
        self.FrDel_County_tools = QFrame(self.FrDel_County_Heading)
        self.FrDel_County_tools.setObjectName(u"FrDel_County_tools")
        self.FrDel_County_tools.setMinimumSize(QSize(0, 25))
        self.FrDel_County_tools.setStyleSheet(u"")
        self.FrDel_County_tools.setFrameShape(QFrame.StyledPanel)
        self.FrDel_County_tools.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.FrDel_County_tools)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(6, 0, 6, 0)
        self.lblDel_County = QLabel(self.FrDel_County_tools)
        self.lblDel_County.setObjectName(u"lblDel_County")
        self.lblDel_County.setFont(font2)

        self.horizontalLayout_39.addWidget(self.lblDel_County, 0, Qt.AlignTop)

        self.pbDel_County = QPushButton(self.FrDel_County_tools)
        self.pbDel_County.setObjectName(u"pbDel_County")

        self.horizontalLayout_39.addWidget(self.pbDel_County, 0, Qt.AlignRight)


        self.verticalLayout_105.addWidget(self.FrDel_County_tools, 0, Qt.AlignTop)

        self.lblDel_Count_comment = QLabel(self.FrDel_County_Heading)
        self.lblDel_Count_comment.setObjectName(u"lblDel_Count_comment")

        self.verticalLayout_105.addWidget(self.lblDel_Count_comment)


        self.verticalLayout_104.addWidget(self.FrDel_County_Heading)

        self.lwDelete_County_Names = QListWidget(self.FrDel_Couty)
        self.lwDelete_County_Names.setObjectName(u"lwDelete_County_Names")
        self.lwDelete_County_Names.setStyleSheet(u"")

        self.verticalLayout_104.addWidget(self.lwDelete_County_Names)


        self.horizontalLayout_16.addWidget(self.FrDel_Couty)

        self.FrDel_State = QFrame(self.FrDel_Selector_MainFrame)
        self.FrDel_State.setObjectName(u"FrDel_State")
        self.FrDel_State.setStyleSheet(u"")
        self.FrDel_State.setFrameShape(QFrame.StyledPanel)
        self.FrDel_State.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.FrDel_State)
        self.verticalLayout_106.setSpacing(6)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(3, 6, 3, 0)
        self.FrDel_State_Heading = QFrame(self.FrDel_State)
        self.FrDel_State_Heading.setObjectName(u"FrDel_State_Heading")
        self.FrDel_State_Heading.setMinimumSize(QSize(0, 46))
        self.FrDel_State_Heading.setMaximumSize(QSize(16777215, 46))
        self.FrDel_State_Heading.setFrameShape(QFrame.StyledPanel)
        self.FrDel_State_Heading.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.FrDel_State_Heading)
        self.verticalLayout_107.setSpacing(6)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(3, 3, 3, 3)
        self.FrDel_State_tools = QFrame(self.FrDel_State_Heading)
        self.FrDel_State_tools.setObjectName(u"FrDel_State_tools")
        self.FrDel_State_tools.setFrameShape(QFrame.StyledPanel)
        self.FrDel_State_tools.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.FrDel_State_tools)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(6, 0, 6, 0)
        self.lblDel_State = QLabel(self.FrDel_State_tools)
        self.lblDel_State.setObjectName(u"lblDel_State")
        self.lblDel_State.setFont(font2)

        self.horizontalLayout_40.addWidget(self.lblDel_State)

        self.pbDel_State = QPushButton(self.FrDel_State_tools)
        self.pbDel_State.setObjectName(u"pbDel_State")
        self.pbDel_State.setIconSize(QSize(14, 14))
        self.pbDel_State.setFlat(False)

        self.horizontalLayout_40.addWidget(self.pbDel_State, 0, Qt.AlignRight)


        self.verticalLayout_107.addWidget(self.FrDel_State_tools, 0, Qt.AlignTop)

        self.cbDel_ChooseAll_States = QCheckBox(self.FrDel_State_Heading)
        self.cbDel_ChooseAll_States.setObjectName(u"cbDel_ChooseAll_States")

        self.verticalLayout_107.addWidget(self.cbDel_ChooseAll_States)


        self.verticalLayout_106.addWidget(self.FrDel_State_Heading)

        self.lwDel_State_Names = QListWidget(self.FrDel_State)
        self.lwDel_State_Names.setObjectName(u"lwDel_State_Names")
        self.lwDel_State_Names.setStyleSheet(u"")

        self.verticalLayout_106.addWidget(self.lwDel_State_Names)


        self.horizontalLayout_16.addWidget(self.FrDel_State)

        self.FrDel_City = QFrame(self.FrDel_Selector_MainFrame)
        self.FrDel_City.setObjectName(u"FrDel_City")
        self.FrDel_City.setStyleSheet(u"")
        self.FrDel_City.setFrameShape(QFrame.StyledPanel)
        self.FrDel_City.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.FrDel_City)
        self.verticalLayout_108.setSpacing(6)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(3, 6, 3, 0)
        self.FrDel_City_Heading = QFrame(self.FrDel_City)
        self.FrDel_City_Heading.setObjectName(u"FrDel_City_Heading")
        self.FrDel_City_Heading.setMinimumSize(QSize(0, 46))
        self.FrDel_City_Heading.setMaximumSize(QSize(16777215, 46))
        self.FrDel_City_Heading.setFrameShape(QFrame.StyledPanel)
        self.FrDel_City_Heading.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.FrDel_City_Heading)
        self.verticalLayout_109.setSpacing(6)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(3, 3, 3, 3)
        self.FrDel_City_tools = QFrame(self.FrDel_City_Heading)
        self.FrDel_City_tools.setObjectName(u"FrDel_City_tools")
        self.FrDel_City_tools.setMinimumSize(QSize(0, 25))
        self.FrDel_City_tools.setStyleSheet(u"")
        self.FrDel_City_tools.setFrameShape(QFrame.StyledPanel)
        self.FrDel_City_tools.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.FrDel_City_tools)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(6, 0, 6, 0)
        self.lblDel_City = QLabel(self.FrDel_City_tools)
        self.lblDel_City.setObjectName(u"lblDel_City")
        self.lblDel_City.setFont(font2)

        self.horizontalLayout_41.addWidget(self.lblDel_City, 0, Qt.AlignTop)

        self.pbDel_City = QPushButton(self.FrDel_City_tools)
        self.pbDel_City.setObjectName(u"pbDel_City")
        self.pbDel_City.setIconSize(QSize(14, 14))

        self.horizontalLayout_41.addWidget(self.pbDel_City, 0, Qt.AlignRight)


        self.verticalLayout_109.addWidget(self.FrDel_City_tools, 0, Qt.AlignTop)

        self.cbDel_ChooseAll_Cities = QCheckBox(self.FrDel_City_Heading)
        self.cbDel_ChooseAll_Cities.setObjectName(u"cbDel_ChooseAll_Cities")

        self.verticalLayout_109.addWidget(self.cbDel_ChooseAll_Cities)


        self.verticalLayout_108.addWidget(self.FrDel_City_Heading)

        self.lwDelete_Cities_Names = QListWidget(self.FrDel_City)
        self.lwDelete_Cities_Names.setObjectName(u"lwDelete_Cities_Names")
        self.lwDelete_Cities_Names.setStyleSheet(u"")

        self.verticalLayout_108.addWidget(self.lwDelete_Cities_Names)


        self.horizontalLayout_16.addWidget(self.FrDel_City)


        self.verticalLayout_70.addWidget(self.FrDel_Selector_MainFrame)


        self.verticalLayout_21.addWidget(self.wDel_cadastrals_Top)

        self.frDel_Main_Selected_Data_Overview = QFrame(self.wdDel_Cadastrals_Main)
        self.frDel_Main_Selected_Data_Overview.setObjectName(u"frDel_Main_Selected_Data_Overview")
        self.frDel_Main_Selected_Data_Overview.setFrameShape(QFrame.StyledPanel)
        self.frDel_Main_Selected_Data_Overview.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frDel_Main_Selected_Data_Overview)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.tabW_Delete_list = QTabWidget(self.frDel_Main_Selected_Data_Overview)
        self.tabW_Delete_list.setObjectName(u"tabW_Delete_list")
        self.tabDel_data_properties = QWidget()
        self.tabDel_data_properties.setObjectName(u"tabDel_data_properties")
        self.tabDel_data_properties.setStyleSheet(u"#tabKinnistud\n"
"{\n"
"	background-color: transparent\n"
"}")
        self.verticalLayout_110 = QVBoxLayout(self.tabDel_data_properties)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.frDel_data_properties_heading = QFrame(self.tabDel_data_properties)
        self.frDel_data_properties_heading.setObjectName(u"frDel_data_properties_heading")
        self.frDel_data_properties_heading.setFrameShape(QFrame.StyledPanel)
        self.frDel_data_properties_heading.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frDel_data_properties_heading)
        self.horizontalLayout_43.setSpacing(10)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(6, 0, 0, 0)
        self.cbDel_ChooseAll_Data_properties = QCheckBox(self.frDel_data_properties_heading)
        self.cbDel_ChooseAll_Data_properties.setObjectName(u"cbDel_ChooseAll_Data_properties")
        self.cbDel_ChooseAll_Data_properties.setIconSize(QSize(16, 16))

        self.horizontalLayout_43.addWidget(self.cbDel_ChooseAll_Data_properties)

        self.cbDel_ChooseAll_Data_include_Allroads = QCheckBox(self.frDel_data_properties_heading)
        self.cbDel_ChooseAll_Data_include_Allroads.setObjectName(u"cbDel_ChooseAll_Data_include_Allroads")

        self.horizontalLayout_43.addWidget(self.cbDel_ChooseAll_Data_include_Allroads)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_17)

        self.pbDel_PreConfirm = QPushButton(self.frDel_data_properties_heading)
        self.pbDel_PreConfirm.setObjectName(u"pbDel_PreConfirm")
        self.pbDel_PreConfirm.setIcon(icon20)

        self.horizontalLayout_43.addWidget(self.pbDel_PreConfirm)


        self.verticalLayout_110.addWidget(self.frDel_data_properties_heading)

        self.tbl_Delete_properties = QTableView(self.tabDel_data_properties)
        self.tbl_Delete_properties.setObjectName(u"tbl_Delete_properties")

        self.verticalLayout_110.addWidget(self.tbl_Delete_properties)

        self.tabW_Delete_list.addTab(self.tabDel_data_properties, "")
        self.tabDel_data_tranposrt = QWidget()
        self.tabDel_data_tranposrt.setObjectName(u"tabDel_data_tranposrt")
        self.verticalLayout_112 = QVBoxLayout(self.tabDel_data_tranposrt)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.frDel_data_transport_heading = QFrame(self.tabDel_data_tranposrt)
        self.frDel_data_transport_heading.setObjectName(u"frDel_data_transport_heading")
        self.frDel_data_transport_heading.setFrameShape(QFrame.StyledPanel)
        self.frDel_data_transport_heading.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frDel_data_transport_heading)
        self.horizontalLayout_45.setSpacing(10)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(6, 0, 0, 0)
        self.cbDel_ChooseAll_Data_transport = QCheckBox(self.frDel_data_transport_heading)
        self.cbDel_ChooseAll_Data_transport.setObjectName(u"cbDel_ChooseAll_Data_transport")

        self.horizontalLayout_45.addWidget(self.cbDel_ChooseAll_Data_transport)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_18)


        self.verticalLayout_112.addWidget(self.frDel_data_transport_heading)

        self.tbl_Delete_streets = QTableView(self.tabDel_data_tranposrt)
        self.tbl_Delete_streets.setObjectName(u"tbl_Delete_streets")

        self.verticalLayout_112.addWidget(self.tbl_Delete_streets)

        self.tabW_Delete_list.addTab(self.tabDel_data_tranposrt, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_144 = QVBoxLayout(self.tab_2)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.tblvAllDeletable = QTableView(self.tab_2)
        self.tblvAllDeletable.setObjectName(u"tblvAllDeletable")

        self.verticalLayout_144.addWidget(self.tblvAllDeletable)

        self.tabW_Delete_list.addTab(self.tab_2, "")

        self.verticalLayout_114.addWidget(self.tabW_Delete_list)


        self.verticalLayout_21.addWidget(self.frDel_Main_Selected_Data_Overview)

        self.fr_Del_bottom = QFrame(self.wdDel_Cadastrals_Main)
        self.fr_Del_bottom.setObjectName(u"fr_Del_bottom")
        self.fr_Del_bottom.setFrameShape(QFrame.StyledPanel)
        self.fr_Del_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.fr_Del_bottom)
        self.horizontalLayout_44.setSpacing(6)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(219, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_11)


        self.verticalLayout_21.addWidget(self.fr_Del_bottom)


        self.verticalLayout_15.addWidget(self.wdDel_Cadastrals_Main)

        self.swCadastral_sub_processes.addWidget(self.swRemove_cadastrals)
        self.Sync_Cadastrals = QWidget()
        self.Sync_Cadastrals.setObjectName(u"Sync_Cadastrals")
        self.Sync_Cadastrals.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(52, 59, 71)\n"
"}\n"
"\n"
"#lblSync_General_aditional{\n"
"background-color: rgb(52, 59, 71)\n"
"}\n"
"\n"
"*\n"
"{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"#QProgressBar\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 1px 8px;\n"
"    border-radius: 6px;\n"
"	background-color:#40414f;\n"
"	border: 0.5px solid #565869;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #8e8ea0;\n"
"	padding: 1px 8px;\n"
"    border-radius: 8px;\n"
"	border: 0.5px solid #acacbe;\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 2px 8px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QgsCheckableComboBox{\n"
"background-color: rgb(52, 59, 71)\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(52, 59, 71)\n"
"}\n"
"QListWidget{\n"
"background-color: rgb(52, 59, 71)\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(52, 59, 71)\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.Sync_Cadastrals)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frSync_Tools = QFrame(self.Sync_Cadastrals)
        self.frSync_Tools.setObjectName(u"frSync_Tools")
        sizePolicy1.setHeightForWidth(self.frSync_Tools.sizePolicy().hasHeightForWidth())
        self.frSync_Tools.setSizePolicy(sizePolicy1)
        self.frSync_Tools.setMinimumSize(QSize(0, 280))
        self.frSync_Tools.setMaximumSize(QSize(16777215, 0))
        self.frSync_Tools.setFrameShape(QFrame.StyledPanel)
        self.frSync_Tools.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frSync_Tools)
        self.verticalLayout_140.setSpacing(10)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(10, 0, 10, 0)
        self.frame_5 = QFrame(self.frSync_Tools)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 200))
        self.frame_5.setMaximumSize(QSize(16777215, 120))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_150 = QVBoxLayout(self.frame_5)
        self.verticalLayout_150.setSpacing(0)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.textEdit_2 = QTextEdit(self.frame_5)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 150))
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_150.addWidget(self.textEdit_2, 0, Qt.AlignTop)


        self.verticalLayout_140.addWidget(self.frame_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_140.addItem(self.verticalSpacer_4)

        self.frSync_Tols_lblFor_layerName = QFrame(self.frSync_Tools)
        self.frSync_Tols_lblFor_layerName.setObjectName(u"frSync_Tols_lblFor_layerName")
        self.frSync_Tols_lblFor_layerName.setFrameShape(QFrame.StyledPanel)
        self.frSync_Tols_lblFor_layerName.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frSync_Tols_lblFor_layerName)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 10, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_13)

        self.LblSync_NamOfFutureLayer = QLabel(self.frSync_Tols_lblFor_layerName)
        self.LblSync_NamOfFutureLayer.setObjectName(u"LblSync_NamOfFutureLayer")
        self.LblSync_NamOfFutureLayer.setFont(font2)

        self.horizontalLayout_55.addWidget(self.LblSync_NamOfFutureLayer)

        self.leText_For_Sync_GreateLayerName = QLineEdit(self.frSync_Tols_lblFor_layerName)
        self.leText_For_Sync_GreateLayerName.setObjectName(u"leText_For_Sync_GreateLayerName")
        self.leText_For_Sync_GreateLayerName.setMinimumSize(QSize(200, 0))
        self.leText_For_Sync_GreateLayerName.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setItalic(True)
        self.leText_For_Sync_GreateLayerName.setFont(font3)
        self.leText_For_Sync_GreateLayerName.setInputMethodHints(Qt.ImhNoAutoUppercase)
        self.leText_For_Sync_GreateLayerName.setMaxLength(25)
        self.leText_For_Sync_GreateLayerName.setCursorPosition(0)

        self.horizontalLayout_55.addWidget(self.leText_For_Sync_GreateLayerName)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_27)


        self.verticalLayout_140.addWidget(self.frSync_Tols_lblFor_layerName)

        self.fr_pbSync_holder = QFrame(self.frSync_Tools)
        self.fr_pbSync_holder.setObjectName(u"fr_pbSync_holder")
        self.fr_pbSync_holder.setFrameShape(QFrame.StyledPanel)
        self.fr_pbSync_holder.setFrameShadow(QFrame.Raised)
        self.verticalLayout_146 = QVBoxLayout(self.fr_pbSync_holder)
        self.verticalLayout_146.setSpacing(0)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.verticalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.pbSync_start_sync = QPushButton(self.fr_pbSync_holder)
        self.pbSync_start_sync.setObjectName(u"pbSync_start_sync")
        self.pbSync_start_sync.setMinimumSize(QSize(100, 20))
        self.pbSync_start_sync.setMaximumSize(QSize(100, 20))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setItalic(False)
        self.pbSync_start_sync.setFont(font4)

        self.verticalLayout_146.addWidget(self.pbSync_start_sync, 0, Qt.AlignHCenter)


        self.verticalLayout_140.addWidget(self.fr_pbSync_holder)


        self.verticalLayout_16.addWidget(self.frSync_Tools, 0, Qt.AlignTop)

        self.frSync_Overview_Main = QFrame(self.Sync_Cadastrals)
        self.frSync_Overview_Main.setObjectName(u"frSync_Overview_Main")
        sizePolicy1.setHeightForWidth(self.frSync_Overview_Main.sizePolicy().hasHeightForWidth())
        self.frSync_Overview_Main.setSizePolicy(sizePolicy1)
        self.frSync_Overview_Main.setMinimumSize(QSize(0, 112))
        self.frSync_Overview_Main.setMaximumSize(QSize(16777215, 112))
        self.frSync_Overview_Main.setStyleSheet(u"\n"
"\n"
"#frame_10,#frame_8, #frame_9,#tblvResults_Confirm,#tblvResults_streets_Confirm,#Add_cadastrals,#Preview_frame,#lwDelete_Conty_Names\n"
"{\n"
"\n"
"        border: 1px solid #2c313c;\n"
"        border-radius: 3px;\n"
"		\n"
"    }\n"
"\n"
"#lblCounty, #lblCity, #lblState {\n"
"    border-bottom: 1px solid #2c313c; /* Set the bottom border width to 1px */\n"
"    border-radius: 1px;\n"
"    width: 50%; /* Set the width of the border to 50% of the element's width */\n"
"}\n"
"\n"
"/* Apply a bottom border with a solid line */\n"
"#leSync_UseNameInputFor_Layer  {\n"
"  border-bottom: 1px solid rgb(255, 255, 255); /* Replace #000 with the desired color */\n"
"}\n"
"\n"
"")
        self.frSync_Overview_Main.setFrameShape(QFrame.StyledPanel)
        self.frSync_Overview_Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.frSync_Overview_Main)
        self.verticalLayout_148.setSpacing(4)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.verticalLayout_148.setContentsMargins(10, 0, 10, 0)
        self.frSync_Overview_general = QFrame(self.frSync_Overview_Main)
        self.frSync_Overview_general.setObjectName(u"frSync_Overview_general")
        self.frSync_Overview_general.setFrameShape(QFrame.StyledPanel)
        self.frSync_Overview_general.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frSync_Overview_general)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.lblSync_General_aditional = QLabel(self.frSync_Overview_general)
        self.lblSync_General_aditional.setObjectName(u"lblSync_General_aditional")
        self.lblSync_General_aditional.setMinimumSize(QSize(200, 0))
        self.lblSync_General_aditional.setMaximumSize(QSize(200, 16777215))
        self.lblSync_General_aditional.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_31.addWidget(self.lblSync_General_aditional)

        self.lblSync_General = QLabel(self.frSync_Overview_general)
        self.lblSync_General.setObjectName(u"lblSync_General")
        sizePolicy1.setHeightForWidth(self.lblSync_General.sizePolicy().hasHeightForWidth())
        self.lblSync_General.setSizePolicy(sizePolicy1)
        self.lblSync_General.setFont(font2)

        self.horizontalLayout_31.addWidget(self.lblSync_General)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_28)


        self.verticalLayout_148.addWidget(self.frSync_Overview_general)

        self.frSync_Overview_County = QFrame(self.frSync_Overview_Main)
        self.frSync_Overview_County.setObjectName(u"frSync_Overview_County")
        sizePolicy1.setHeightForWidth(self.frSync_Overview_County.sizePolicy().hasHeightForWidth())
        self.frSync_Overview_County.setSizePolicy(sizePolicy1)
        self.frSync_Overview_County.setMinimumSize(QSize(0, 20))
        self.frSync_Overview_County.setMaximumSize(QSize(16777215, 20))
        self.frSync_Overview_County.setFrameShape(QFrame.StyledPanel)
        self.frSync_Overview_County.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frSync_Overview_County)
        self.horizontalLayout_22.setSpacing(6)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.lblFor_pBar_Sync_County = QLabel(self.frSync_Overview_County)
        self.lblFor_pBar_Sync_County.setObjectName(u"lblFor_pBar_Sync_County")
        self.lblFor_pBar_Sync_County.setMinimumSize(QSize(120, 0))
        self.lblFor_pBar_Sync_County.setFont(font2)

        self.horizontalLayout_22.addWidget(self.lblFor_pBar_Sync_County)

        self.b = QFrame(self.frSync_Overview_County)
        self.b.setObjectName(u"b")
        self.b.setFrameShape(QFrame.StyledPanel)
        self.b.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.b)

        self.pBar_Sync_County = QProgressBar(self.frSync_Overview_County)
        self.pBar_Sync_County.setObjectName(u"pBar_Sync_County")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pBar_Sync_County.sizePolicy().hasHeightForWidth())
        self.pBar_Sync_County.setSizePolicy(sizePolicy3)
        self.pBar_Sync_County.setMinimumSize(QSize(250, 15))
        self.pBar_Sync_County.setMaximumSize(QSize(250, 15))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(True)
        self.pBar_Sync_County.setFont(font5)
        self.pBar_Sync_County.setValue(0)

        self.horizontalLayout_22.addWidget(self.pBar_Sync_County)


        self.verticalLayout_148.addWidget(self.frSync_Overview_County)

        self.frSync_Overview_selectedCityProperties = QFrame(self.frSync_Overview_Main)
        self.frSync_Overview_selectedCityProperties.setObjectName(u"frSync_Overview_selectedCityProperties")
        sizePolicy1.setHeightForWidth(self.frSync_Overview_selectedCityProperties.sizePolicy().hasHeightForWidth())
        self.frSync_Overview_selectedCityProperties.setSizePolicy(sizePolicy1)
        self.frSync_Overview_selectedCityProperties.setMinimumSize(QSize(0, 20))
        self.frSync_Overview_selectedCityProperties.setMaximumSize(QSize(16777215, 20))
        self.frSync_Overview_selectedCityProperties.setFrameShape(QFrame.StyledPanel)
        self.frSync_Overview_selectedCityProperties.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frSync_Overview_selectedCityProperties)
        self.horizontalLayout_50.setSpacing(6)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.lblFor_pBar_State_list = QLabel(self.frSync_Overview_selectedCityProperties)
        self.lblFor_pBar_State_list.setObjectName(u"lblFor_pBar_State_list")
        self.lblFor_pBar_State_list.setMinimumSize(QSize(120, 0))
        self.lblFor_pBar_State_list.setFont(font2)

        self.horizontalLayout_50.addWidget(self.lblFor_pBar_State_list)

        self.c = QFrame(self.frSync_Overview_selectedCityProperties)
        self.c.setObjectName(u"c")
        self.c.setFrameShape(QFrame.StyledPanel)
        self.c.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_50.addWidget(self.c)

        self.pBar_State_list = QProgressBar(self.frSync_Overview_selectedCityProperties)
        self.pBar_State_list.setObjectName(u"pBar_State_list")
        sizePolicy3.setHeightForWidth(self.pBar_State_list.sizePolicy().hasHeightForWidth())
        self.pBar_State_list.setSizePolicy(sizePolicy3)
        self.pBar_State_list.setMinimumSize(QSize(250, 15))
        self.pBar_State_list.setMaximumSize(QSize(250, 15))
        self.pBar_State_list.setFont(font5)
        self.pBar_State_list.setValue(0)

        self.horizontalLayout_50.addWidget(self.pBar_State_list)


        self.verticalLayout_148.addWidget(self.frSync_Overview_selectedCityProperties)

        self.frSync_Overview_CityList = QFrame(self.frSync_Overview_Main)
        self.frSync_Overview_CityList.setObjectName(u"frSync_Overview_CityList")
        sizePolicy1.setHeightForWidth(self.frSync_Overview_CityList.sizePolicy().hasHeightForWidth())
        self.frSync_Overview_CityList.setSizePolicy(sizePolicy1)
        self.frSync_Overview_CityList.setMinimumSize(QSize(0, 20))
        self.frSync_Overview_CityList.setMaximumSize(QSize(16777215, 20))
        self.frSync_Overview_CityList.setFrameShape(QFrame.StyledPanel)
        self.frSync_Overview_CityList.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frSync_Overview_CityList)
        self.horizontalLayout_49.setSpacing(6)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.lblFor_pBar_City_list = QLabel(self.frSync_Overview_CityList)
        self.lblFor_pBar_City_list.setObjectName(u"lblFor_pBar_City_list")
        self.lblFor_pBar_City_list.setMinimumSize(QSize(120, 0))
        self.lblFor_pBar_City_list.setFont(font2)

        self.horizontalLayout_49.addWidget(self.lblFor_pBar_City_list)

        self.a = QFrame(self.frSync_Overview_CityList)
        self.a.setObjectName(u"a")
        self.a.setFrameShape(QFrame.StyledPanel)
        self.a.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_49.addWidget(self.a)

        self.pBar_City_list = QProgressBar(self.frSync_Overview_CityList)
        self.pBar_City_list.setObjectName(u"pBar_City_list")
        sizePolicy3.setHeightForWidth(self.pBar_City_list.sizePolicy().hasHeightForWidth())
        self.pBar_City_list.setSizePolicy(sizePolicy3)
        self.pBar_City_list.setMinimumSize(QSize(250, 15))
        self.pBar_City_list.setMaximumSize(QSize(250, 15))
        self.pBar_City_list.setFont(font5)
        self.pBar_City_list.setValue(0)

        self.horizontalLayout_49.addWidget(self.pBar_City_list)


        self.verticalLayout_148.addWidget(self.frSync_Overview_CityList)

        self.frSync_Overview_StateList = QFrame(self.frSync_Overview_Main)
        self.frSync_Overview_StateList.setObjectName(u"frSync_Overview_StateList")
        sizePolicy1.setHeightForWidth(self.frSync_Overview_StateList.sizePolicy().hasHeightForWidth())
        self.frSync_Overview_StateList.setSizePolicy(sizePolicy1)
        self.frSync_Overview_StateList.setMinimumSize(QSize(0, 20))
        self.frSync_Overview_StateList.setMaximumSize(QSize(16777215, 20))
        self.frSync_Overview_StateList.setFrameShape(QFrame.StyledPanel)
        self.frSync_Overview_StateList.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frSync_Overview_StateList)
        self.horizontalLayout_48.setSpacing(6)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.lblFor_pBar_CityItems = QLabel(self.frSync_Overview_StateList)
        self.lblFor_pBar_CityItems.setObjectName(u"lblFor_pBar_CityItems")
        self.lblFor_pBar_CityItems.setMinimumSize(QSize(120, 0))
        self.lblFor_pBar_CityItems.setFont(font2)

        self.horizontalLayout_48.addWidget(self.lblFor_pBar_CityItems)

        self.d = QFrame(self.frSync_Overview_StateList)
        self.d.setObjectName(u"d")
        self.d.setFrameShape(QFrame.StyledPanel)
        self.d.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_48.addWidget(self.d)

        self.pBar_CityItems = QProgressBar(self.frSync_Overview_StateList)
        self.pBar_CityItems.setObjectName(u"pBar_CityItems")
        sizePolicy3.setHeightForWidth(self.pBar_CityItems.sizePolicy().hasHeightForWidth())
        self.pBar_CityItems.setSizePolicy(sizePolicy3)
        self.pBar_CityItems.setMinimumSize(QSize(250, 15))
        self.pBar_CityItems.setMaximumSize(QSize(250, 15))
        self.pBar_CityItems.setFont(font5)
        self.pBar_CityItems.setValue(0)

        self.horizontalLayout_48.addWidget(self.pBar_CityItems)


        self.verticalLayout_148.addWidget(self.frSync_Overview_StateList)


        self.verticalLayout_16.addWidget(self.frSync_Overview_Main, 0, Qt.AlignTop)

        self.frSync_Cadastrals_Main = QWidget(self.Sync_Cadastrals)
        self.frSync_Cadastrals_Main.setObjectName(u"frSync_Cadastrals_Main")
        self.frSync_Cadastrals_Main.setStyleSheet(u"")
        self.verticalLayout_23 = QVBoxLayout(self.frSync_Cadastrals_Main)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.Sync_cadastrals_Top = QWidget(self.frSync_Cadastrals_Main)
        self.Sync_cadastrals_Top.setObjectName(u"Sync_cadastrals_Top")
        self.Sync_cadastrals_Top.setStyleSheet(u"#a, #b,#c,#d{\n"
"    border-bottom: 1px solid #e0e0e0; /* Darker white color, adjust as needed */\n"
"    padding-bottom: 5px; /* Adjust padding as needed */\n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.Sync_cadastrals_Top)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frSync_General = QFrame(self.Sync_cadastrals_Top)
        self.frSync_General.setObjectName(u"frSync_General")
        self.frSync_General.setFrameShape(QFrame.StyledPanel)
        self.frSync_General.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frSync_General)
        self.verticalLayout_77.setSpacing(10)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(10, 0, 0, 0)

        self.verticalLayout_22.addWidget(self.frSync_General)

        self.frSync_Selector_MainFrame = QFrame(self.Sync_cadastrals_Top)
        self.frSync_Selector_MainFrame.setObjectName(u"frSync_Selector_MainFrame")
        self.frSync_Selector_MainFrame.setStyleSheet(u"")
        self.frSync_Selector_MainFrame.setFrameShape(QFrame.StyledPanel)
        self.frSync_Selector_MainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frSync_Selector_MainFrame)
        self.horizontalLayout_30.setSpacing(2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frSync_County = QFrame(self.frSync_Selector_MainFrame)
        self.frSync_County.setObjectName(u"frSync_County")
        self.frSync_County.setStyleSheet(u"")
        self.frSync_County.setFrameShape(QFrame.StyledPanel)
        self.frSync_County.setFrameShadow(QFrame.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.frSync_County)
        self.verticalLayout_141.setSpacing(6)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(3, 6, 3, 0)
        self.FrSync_County_Heading = QFrame(self.frSync_County)
        self.FrSync_County_Heading.setObjectName(u"FrSync_County_Heading")
        self.FrSync_County_Heading.setMinimumSize(QSize(0, 25))
        self.FrSync_County_Heading.setMaximumSize(QSize(16777215, 40))
        self.FrSync_County_Heading.setStyleSheet(u"   #frame_10 {\n"
"\n"
"        border: 1px solid #2c313c;\n"
"        border-radius: 3px;\n"
"		\n"
"    }\n"
"")
        self.FrSync_County_Heading.setFrameShape(QFrame.StyledPanel)
        self.FrSync_County_Heading.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.FrSync_County_Heading)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(-1, -1, -1, 0)
        self.lblSync_County = QLabel(self.FrSync_County_Heading)
        self.lblSync_County.setObjectName(u"lblSync_County")
        sizePolicy3.setHeightForWidth(self.lblSync_County.sizePolicy().hasHeightForWidth())
        self.lblSync_County.setSizePolicy(sizePolicy3)
        self.lblSync_County.setMinimumSize(QSize(0, 0))
        self.lblSync_County.setMaximumSize(QSize(16777215, 16777215))
        self.lblSync_County.setFont(font2)

        self.horizontalLayout_51.addWidget(self.lblSync_County)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_31)


        self.verticalLayout_141.addWidget(self.FrSync_County_Heading)

        self.lwSync_County_Names = QListWidget(self.frSync_County)
        self.lwSync_County_Names.setObjectName(u"lwSync_County_Names")
        self.lwSync_County_Names.setStyleSheet(u"")
        self.lwSync_County_Names.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lwSync_County_Names.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_141.addWidget(self.lwSync_County_Names)


        self.horizontalLayout_30.addWidget(self.frSync_County)

        self.frSync_State = QFrame(self.frSync_Selector_MainFrame)
        self.frSync_State.setObjectName(u"frSync_State")
        self.frSync_State.setStyleSheet(u"")
        self.frSync_State.setFrameShape(QFrame.StyledPanel)
        self.frSync_State.setFrameShadow(QFrame.Raised)
        self.verticalLayout_147 = QVBoxLayout(self.frSync_State)
        self.verticalLayout_147.setSpacing(6)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.verticalLayout_147.setContentsMargins(3, 6, 3, 0)
        self.FrSync_State_Heading = QFrame(self.frSync_State)
        self.FrSync_State_Heading.setObjectName(u"FrSync_State_Heading")
        self.FrSync_State_Heading.setMinimumSize(QSize(0, 25))
        self.FrSync_State_Heading.setMaximumSize(QSize(16777215, 40))
        self.FrSync_State_Heading.setFrameShape(QFrame.StyledPanel)
        self.FrSync_State_Heading.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.FrSync_State_Heading)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(-1, -1, -1, 0)
        self.lblSync_State = QLabel(self.FrSync_State_Heading)
        self.lblSync_State.setObjectName(u"lblSync_State")
        sizePolicy3.setHeightForWidth(self.lblSync_State.sizePolicy().hasHeightForWidth())
        self.lblSync_State.setSizePolicy(sizePolicy3)
        self.lblSync_State.setFont(font2)

        self.horizontalLayout_52.addWidget(self.lblSync_State)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_30)


        self.verticalLayout_147.addWidget(self.FrSync_State_Heading)

        self.lwSync_State_Names = QListWidget(self.frSync_State)
        self.lwSync_State_Names.setObjectName(u"lwSync_State_Names")
        self.lwSync_State_Names.setStyleSheet(u"")
        self.lwSync_State_Names.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_147.addWidget(self.lwSync_State_Names)


        self.horizontalLayout_30.addWidget(self.frSync_State)

        self.frSync_City = QFrame(self.frSync_Selector_MainFrame)
        self.frSync_City.setObjectName(u"frSync_City")
        self.frSync_City.setStyleSheet(u"")
        self.frSync_City.setFrameShape(QFrame.StyledPanel)
        self.frSync_City.setFrameShadow(QFrame.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.frSync_City)
        self.verticalLayout_149.setSpacing(6)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(3, 6, 3, 0)
        self.FrSync_City_Heading = QFrame(self.frSync_City)
        self.FrSync_City_Heading.setObjectName(u"FrSync_City_Heading")
        self.FrSync_City_Heading.setMinimumSize(QSize(0, 25))
        self.FrSync_City_Heading.setMaximumSize(QSize(16777215, 40))
        self.FrSync_City_Heading.setFrameShape(QFrame.StyledPanel)
        self.FrSync_City_Heading.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.FrSync_City_Heading)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(9, -1, -1, 0)
        self.lblSync_City = QLabel(self.FrSync_City_Heading)
        self.lblSync_City.setObjectName(u"lblSync_City")
        sizePolicy3.setHeightForWidth(self.lblSync_City.sizePolicy().hasHeightForWidth())
        self.lblSync_City.setSizePolicy(sizePolicy3)
        self.lblSync_City.setFont(font2)

        self.horizontalLayout_54.addWidget(self.lblSync_City, 0, Qt.AlignLeft)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_29)


        self.verticalLayout_149.addWidget(self.FrSync_City_Heading)

        self.lwSync_City_Names = QListWidget(self.frSync_City)
        self.lwSync_City_Names.setObjectName(u"lwSync_City_Names")
        self.lwSync_City_Names.setStyleSheet(u"")
        self.lwSync_City_Names.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_149.addWidget(self.lwSync_City_Names)


        self.horizontalLayout_30.addWidget(self.frSync_City)


        self.verticalLayout_22.addWidget(self.frSync_Selector_MainFrame)


        self.verticalLayout_23.addWidget(self.Sync_cadastrals_Top)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_2)

        self.Sync_Main_Selected_Data_Overview = QFrame(self.frSync_Cadastrals_Main)
        self.Sync_Main_Selected_Data_Overview.setObjectName(u"Sync_Main_Selected_Data_Overview")
        self.Sync_Main_Selected_Data_Overview.setMaximumSize(QSize(16777215, 100))
        self.Sync_Main_Selected_Data_Overview.setFrameShape(QFrame.StyledPanel)
        self.Sync_Main_Selected_Data_Overview.setFrameShadow(QFrame.Raised)
        self.verticalLayout_151 = QVBoxLayout(self.Sync_Main_Selected_Data_Overview)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.tbl_Sync_properties = QTableView(self.Sync_Main_Selected_Data_Overview)
        self.tbl_Sync_properties.setObjectName(u"tbl_Sync_properties")

        self.verticalLayout_151.addWidget(self.tbl_Sync_properties)


        self.verticalLayout_23.addWidget(self.Sync_Main_Selected_Data_Overview)


        self.verticalLayout_16.addWidget(self.frSync_Cadastrals_Main)

        self.Sync_Del_bottom = QFrame(self.Sync_Cadastrals)
        self.Sync_Del_bottom.setObjectName(u"Sync_Del_bottom")
        self.Sync_Del_bottom.setFrameShape(QFrame.StyledPanel)
        self.Sync_Del_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.Sync_Del_bottom)
        self.horizontalLayout_53.setSpacing(6)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_12 = QSpacerItem(219, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_12)

        self.pbSync_Cancel = QPushButton(self.Sync_Del_bottom)
        self.pbSync_Cancel.setObjectName(u"pbSync_Cancel")

        self.horizontalLayout_53.addWidget(self.pbSync_Cancel)


        self.verticalLayout_16.addWidget(self.Sync_Del_bottom)

        self.swCadastral_sub_processes.addWidget(self.Sync_Cadastrals)
        self.Update_Cadastrals = QWidget()
        self.Update_Cadastrals.setObjectName(u"Update_Cadastrals")
        self.verticalLayout_152 = QVBoxLayout(self.Update_Cadastrals)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.Loomisel_label = QLabel(self.Update_Cadastrals)
        self.Loomisel_label.setObjectName(u"Loomisel_label")
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        self.Loomisel_label.setFont(font6)

        self.verticalLayout_152.addWidget(self.Loomisel_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.swCadastral_sub_processes.addWidget(self.Update_Cadastrals)
        self.swCadastral_FrontPage = QWidget()
        self.swCadastral_FrontPage.setObjectName(u"swCadastral_FrontPage")
        self.verticalLayout_157 = QVBoxLayout(self.swCadastral_FrontPage)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.Loomisel_label_2 = QLabel(self.swCadastral_FrontPage)
        self.Loomisel_label_2.setObjectName(u"Loomisel_label_2")
        self.Loomisel_label_2.setFont(font6)

        self.verticalLayout_157.addWidget(self.Loomisel_label_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.textEdit_3 = QTextEdit(self.swCadastral_FrontPage)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.verticalLayout_157.addWidget(self.textEdit_3)

        self.swCadastral_sub_processes.addWidget(self.swCadastral_FrontPage)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.swCadastral_sub_processes.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.swCadastral_sub_processes)

        self.widget_19 = QWidget(self.Cadastralmoves)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setStyleSheet(u"*{\n"
"	border: transparent;\n"
"	background-color: transparent;\n"
"    background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #dadee4;\n"
"}")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_37.setSpacing(10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(3, 0, 3, 0)

        self.verticalLayout_5.addWidget(self.widget_19)

        self.swWorkSpace.addWidget(self.Cadastralmoves)
        self.Lepingud = QWidget()
        self.Lepingud.setObjectName(u"Lepingud")
        self.verticalLayout_39 = QVBoxLayout(self.Lepingud)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 10, 0, 10)
        self.ContractsPageName = QWidget(self.Lepingud)
        self.ContractsPageName.setObjectName(u"ContractsPageName")
        self.ContractsPageName.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.ContractsPageName)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 10, 0, 10)
        self.label_18 = QLabel(self.ContractsPageName)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_18, 0, Qt.AlignTop)


        self.verticalLayout_39.addWidget(self.ContractsPageName, 0, Qt.AlignTop)

        self.ContractMainFrame = QFrame(self.Lepingud)
        self.ContractMainFrame.setObjectName(u"ContractMainFrame")
        self.ContractMainFrame.setStyleSheet(u"")
        self.ContractMainFrame.setFrameShape(QFrame.StyledPanel)
        self.ContractMainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.ContractMainFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Buttons = QFrame(self.ContractMainFrame)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setStyleSheet(u"")
        self.Buttons.setFrameShape(QFrame.StyledPanel)
        self.Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.Buttons)
        self.horizontalLayout_10.setSpacing(12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(6, 6, 6, -1)
        self.pbContracts_Connect_properties = QPushButton(self.Buttons)
        self.pbContracts_Connect_properties.setObjectName(u"pbContracts_Connect_properties")

        self.horizontalLayout_10.addWidget(self.pbContracts_Connect_properties)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.pbRefresh_tblMailabl_contracts = QPushButton(self.Buttons)
        self.pbRefresh_tblMailabl_contracts.setObjectName(u"pbRefresh_tblMailabl_contracts")
        self.pbRefresh_tblMailabl_contracts.setIcon(icon15)

        self.horizontalLayout_10.addWidget(self.pbRefresh_tblMailabl_contracts)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_22)

        self.label_5 = QLabel(self.Buttons)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)


        self.verticalLayout_8.addWidget(self.Buttons)

        self.ContractInfoFrame = QFrame(self.ContractMainFrame)
        self.ContractInfoFrame.setObjectName(u"ContractInfoFrame")
        self.ContractInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.ContractInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.ContractInfoFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ContractView = QTableView(self.ContractInfoFrame)
        self.ContractView.setObjectName(u"ContractView")
        self.ContractView.setStyleSheet(u"background-color: rgb(52, 59, 71);")

        self.verticalLayout.addWidget(self.ContractView)


        self.verticalLayout_8.addWidget(self.ContractInfoFrame)


        self.verticalLayout_39.addWidget(self.ContractMainFrame)

        self.ContractsPageFooter = QWidget(self.Lepingud)
        self.ContractsPageFooter.setObjectName(u"ContractsPageFooter")
        self.ContractsPageFooter.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        self.verticalLayout_37 = QVBoxLayout(self.ContractsPageFooter)
        self.verticalLayout_37.setSpacing(5)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 10, 0, 10)
        self.label_19 = QLabel(self.ContractsPageFooter)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_37.addWidget(self.label_19)

        self.label_3 = QLabel(self.ContractsPageFooter)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_37.addWidget(self.label_3)


        self.verticalLayout_39.addWidget(self.ContractsPageFooter, 0, Qt.AlignBottom)

        self.swWorkSpace.addWidget(self.Lepingud)
        self.Help = QWidget()
        self.Help.setObjectName(u"Help")
        self.verticalLayout_40 = QVBoxLayout(self.Help)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 10, 0, 10)
        self.HelpPageName = QWidget(self.Help)
        self.HelpPageName.setObjectName(u"HelpPageName")
        self.verticalLayout_41 = QVBoxLayout(self.HelpPageName)
        self.verticalLayout_41.setSpacing(5)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 10, 0, 10)
        self.label_20 = QLabel(self.HelpPageName)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.label_20)


        self.verticalLayout_40.addWidget(self.HelpPageName, 0, Qt.AlignTop)

        self.HelpMainFrame = QWidget(self.Help)
        self.HelpMainFrame.setObjectName(u"HelpMainFrame")
        self.verticalLayout_42 = QVBoxLayout(self.HelpMainFrame)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.HelpMainFrame)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_42.addWidget(self.textEdit)


        self.verticalLayout_40.addWidget(self.HelpMainFrame)

        self.HelpPageFooter = QWidget(self.Help)
        self.HelpPageFooter.setObjectName(u"HelpPageFooter")
        self.verticalLayout_43 = QVBoxLayout(self.HelpPageFooter)
        self.verticalLayout_43.setSpacing(5)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.HelpPageFooter)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_43.addWidget(self.label_21)


        self.verticalLayout_40.addWidget(self.HelpPageFooter, 0, Qt.AlignBottom)

        self.swWorkSpace.addWidget(self.Help)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_12 = QVBoxLayout(self.settings)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.SettingsPageName = QWidget(self.settings)
        self.SettingsPageName.setObjectName(u"SettingsPageName")
        self.SettingsPageName.setStyleSheet(u"")
        self.verticalLayout_35 = QVBoxLayout(self.SettingsPageName)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_15 = QLabel(self.SettingsPageName)
        self.label_15.setObjectName(u"label_15")
        font7 = QFont()
        font7.setPointSize(13)
        font7.setBold(False)
        font7.setItalic(False)
        self.label_15.setFont(font7)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_15)


        self.verticalLayout_12.addWidget(self.SettingsPageName)

        self.SettingsPageMainFrame = QWidget(self.settings)
        self.SettingsPageMainFrame.setObjectName(u"SettingsPageMainFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.SettingsPageMainFrame.sizePolicy().hasHeightForWidth())
        self.SettingsPageMainFrame.setSizePolicy(sizePolicy4)
        self.SettingsPageMainFrame.setStyleSheet(u"/*\u00fcle\u00fcldine taust ja toonid*/\n"
"\n"
"\n"
"\n"
"#lblnewCadastrals_input_layer_label, \n"
"#lblcurrent_main_layer_label, \n"
"#lbNuserName, \n"
"#lblUserRoles, \n"
"#lblNUserSurename, \n"
"#lblPreferences,\n"
"#lblSHPNewItems,\n"
"#lblSHPNewItems_2,\n"
"#lblnewCadastrals_input_layer_label_2, \n"
"#lblcurrent_main_layer_label_2\n"
"{\n"
"\n"
"	background-color:#40414f;\n"
"	color:#ececf1;\n"
"	border: 1px solid #565869;\n"
"	border-radius: 3px;\n"
"	padding: 1px\n"
"}\n"
"\n"
"/* Apply a bottom border with a solid line */\n"
"#qwSU_Mailabl_Users,#qwSU_Mailabl_Projects, #qwSU_Layers  {\n"
"  border-bottom: 1px solid rgb(255, 255, 255); /* Replace #000 with the desired color */\n"
"}\n"
"\n"
"")
        self.verticalLayout_139 = QVBoxLayout(self.SettingsPageMainFrame)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.qwSU_Mailabl_Users = QWidget(self.SettingsPageMainFrame)
        self.qwSU_Mailabl_Users.setObjectName(u"qwSU_Mailabl_Users")
        self.qwSU_Mailabl_Users.setStyleSheet(u"")
        self.verticalLayout_45 = QVBoxLayout(self.qwSU_Mailabl_Users)
        self.verticalLayout_45.setSpacing(8)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(5, 5, 5, 5)
        self.frame_25 = QFrame(self.qwSU_Mailabl_Users)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lblHEadingUserData = QLabel(self.frame_25)
        self.lblHEadingUserData.setObjectName(u"lblHEadingUserData")
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setUnderline(False)
        self.lblHEadingUserData.setFont(font8)

        self.horizontalLayout_17.addWidget(self.lblHEadingUserData)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_25)

        self.pbUserSettings = QPushButton(self.frame_25)
        self.pbUserSettings.setObjectName(u"pbUserSettings")
        self.pbUserSettings.setIcon(icon9)
        self.pbUserSettings.setIconSize(QSize(16, 16))

        self.horizontalLayout_17.addWidget(self.pbUserSettings)


        self.verticalLayout_45.addWidget(self.frame_25)

        self.frame_23 = QFrame(self.qwSU_Mailabl_Users)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_46.setSpacing(10)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(15, 0, 0, 0)
        self.lbNUserPreferences = QLabel(self.frame_23)
        self.lbNUserPreferences.setObjectName(u"lbNUserPreferences")
        self.lbNUserPreferences.setFont(font2)

        self.horizontalLayout_46.addWidget(self.lbNUserPreferences)

        self.lblPreferences = QLabel(self.frame_23)
        self.lblPreferences.setObjectName(u"lblPreferences")
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(False)
        self.lblPreferences.setFont(font9)

        self.horizontalLayout_46.addWidget(self.lblPreferences)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_4)


        self.verticalLayout_45.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.qwSU_Mailabl_Users)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_47.setSpacing(10)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(15, 0, 0, 0)
        self.lblUserFirstName = QLabel(self.frame_24)
        self.lblUserFirstName.setObjectName(u"lblUserFirstName")
        self.lblUserFirstName.setFont(font2)

        self.horizontalLayout_47.addWidget(self.lblUserFirstName)

        self.lblNUserSurename = QLabel(self.frame_24)
        self.lblNUserSurename.setObjectName(u"lblNUserSurename")
        self.lblNUserSurename.setFont(font9)

        self.horizontalLayout_47.addWidget(self.lblNUserSurename)

        self.lbNuserName = QLabel(self.frame_24)
        self.lbNuserName.setObjectName(u"lbNuserName")
        self.lbNuserName.setFont(font9)

        self.horizontalLayout_47.addWidget(self.lbNuserName)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_3)


        self.verticalLayout_45.addWidget(self.frame_24)

        self.frame_6 = QFrame(self.qwSU_Mailabl_Users)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_42.setSpacing(10)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(15, 0, 0, 0)
        self.lbNUserRoles = QLabel(self.frame_6)
        self.lbNUserRoles.setObjectName(u"lbNUserRoles")
        self.lbNUserRoles.setFont(font2)

        self.horizontalLayout_42.addWidget(self.lbNUserRoles)

        self.lblUserRoles = QLabel(self.frame_6)
        self.lblUserRoles.setObjectName(u"lblUserRoles")
        self.lblUserRoles.setFont(font9)

        self.horizontalLayout_42.addWidget(self.lblUserRoles)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_24)


        self.verticalLayout_45.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.qwSU_Mailabl_Users)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_36.setSpacing(10)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(15, 0, 0, 0)
        self.label_27 = QLabel(self.frame_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.horizontalLayout_36.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.horizontalLayout_36.addWidget(self.label_28)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_23)


        self.verticalLayout_45.addWidget(self.frame_4)


        self.verticalLayout_139.addWidget(self.qwSU_Mailabl_Users)

        self.qwSU_Layers = QWidget(self.SettingsPageMainFrame)
        self.qwSU_Layers.setObjectName(u"qwSU_Layers")
        self.qwSU_Layers.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.qwSU_Layers)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_26 = QFrame(self.qwSU_Layers)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_26)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font8)

        self.horizontalLayout_19.addWidget(self.label_30)

        self.horizontalSpacer_7 = QSpacerItem(494, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_7)

        self.pbLayerSettings = QPushButton(self.frame_26)
        self.pbLayerSettings.setObjectName(u"pbLayerSettings")
        self.pbLayerSettings.setIcon(icon9)
        self.pbLayerSettings.setIconSize(QSize(16, 16))

        self.horizontalLayout_19.addWidget(self.pbLayerSettings)


        self.verticalLayout_2.addWidget(self.frame_26)

        self.frame_14 = QFrame(self.qwSU_Layers)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(15, 0, 0, 0)
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.horizontalLayout_15.addWidget(self.label_16)

        self.lblSHPNewItems = QLabel(self.frame_14)
        self.lblSHPNewItems.setObjectName(u"lblSHPNewItems")

        self.horizontalLayout_15.addWidget(self.lblSHPNewItems)

        self.horizontalSpacer_2 = QSpacerItem(309, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.qwSU_Layers)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(15, 0, 0, 0)
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.horizontalLayout_29.addWidget(self.label_6)

        self.lblcurrent_main_layer_label = QLabel(self.frame_15)
        self.lblcurrent_main_layer_label.setObjectName(u"lblcurrent_main_layer_label")
        self.lblcurrent_main_layer_label.setFont(font9)

        self.horizontalLayout_29.addWidget(self.lblcurrent_main_layer_label)

        self.horizontalSpacer_5 = QSpacerItem(370, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.qwSU_Layers)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lblnewCadastrals_input_layer_label = QLabel(self.frame_16)
        self.lblnewCadastrals_input_layer_label.setObjectName(u"lblnewCadastrals_input_layer_label")
        self.lblnewCadastrals_input_layer_label.setFont(font9)

        self.horizontalLayout_2.addWidget(self.lblnewCadastrals_input_layer_label)

        self.horizontalSpacer_6 = QSpacerItem(304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.frame_16)


        self.verticalLayout_139.addWidget(self.qwSU_Layers)

        self.qwSU_Mailabl_Projects = QWidget(self.SettingsPageMainFrame)
        self.qwSU_Mailabl_Projects.setObjectName(u"qwSU_Mailabl_Projects")
        self.qwSU_Mailabl_Projects.setStyleSheet(u"")
        self.verticalLayout_46 = QVBoxLayout(self.qwSU_Mailabl_Projects)
        self.verticalLayout_46.setSpacing(8)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(5, 5, 5, 5)
        self.frame_27 = QFrame(self.qwSU_Mailabl_Projects)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_27)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font8)

        self.horizontalLayout_20.addWidget(self.label_31)

        self.horizontalSpacer_19 = QSpacerItem(567, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_19)

        self.pbSettings_Setup_Projects = QPushButton(self.frame_27)
        self.pbSettings_Setup_Projects.setObjectName(u"pbSettings_Setup_Projects")
        self.pbSettings_Setup_Projects.setIcon(icon9)
        self.pbSettings_Setup_Projects.setIconSize(QSize(16, 16))

        self.horizontalLayout_20.addWidget(self.pbSettings_Setup_Projects)


        self.verticalLayout_46.addWidget(self.frame_27)

        self.frame_19 = QFrame(self.qwSU_Mailabl_Projects)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(15, 0, 0, 0)
        self.label_22 = QLabel(self.frame_19)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.horizontalLayout_33.addWidget(self.label_22)

        self.lblLayerProjects_Properties = QLabel(self.frame_19)
        self.lblLayerProjects_Properties.setObjectName(u"lblLayerProjects_Properties")

        self.horizontalLayout_33.addWidget(self.lblLayerProjects_Properties)

        self.horizontalSpacer_20 = QSpacerItem(309, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_20)


        self.verticalLayout_46.addWidget(self.frame_19)

        self.frame_21 = QFrame(self.qwSU_Mailabl_Projects)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_34.setSpacing(10)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(15, 0, 0, 0)
        self.label_14 = QLabel(self.frame_21)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.horizontalLayout_34.addWidget(self.label_14)

        self.lblLayerProjects_Vector = QLabel(self.frame_21)
        self.lblLayerProjects_Vector.setObjectName(u"lblLayerProjects_Vector")
        self.lblLayerProjects_Vector.setFont(font9)

        self.horizontalLayout_34.addWidget(self.lblLayerProjects_Vector)

        self.horizontalSpacer_21 = QSpacerItem(370, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_21)


        self.verticalLayout_46.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.qwSU_Mailabl_Projects)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(15, 0, 0, 0)

        self.verticalLayout_46.addWidget(self.frame_22)


        self.verticalLayout_139.addWidget(self.qwSU_Mailabl_Projects)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_139.addItem(self.verticalSpacer)


        self.verticalLayout_12.addWidget(self.SettingsPageMainFrame)

        self.swWorkSpace.addWidget(self.settings)
        self.Homepage = QWidget()
        self.Homepage.setObjectName(u"Homepage")
        self.verticalLayout_13 = QVBoxLayout(self.Homepage)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 10, 0, 10)
        self.HomePageName = QFrame(self.Homepage)
        self.HomePageName.setObjectName(u"HomePageName")
        self.HomePageName.setFrameShape(QFrame.StyledPanel)
        self.HomePageName.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.HomePageName)
        self.verticalLayout_56.setSpacing(5)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 10, 0, 10)
        self.label_10 = QLabel(self.HomePageName)
        self.label_10.setObjectName(u"label_10")
        font10 = QFont()
        font10.setPointSize(13)
        font10.setBold(False)
        self.label_10.setFont(font10)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_56.addWidget(self.label_10)


        self.verticalLayout_13.addWidget(self.HomePageName, 0, Qt.AlignTop)

        self.Intro_Help = QFrame(self.Homepage)
        self.Intro_Help.setObjectName(u"Intro_Help")
        self.Intro_Help.setFrameShape(QFrame.StyledPanel)
        self.Intro_Help.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.Intro_Help)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.teWelcomeContent = QTextBrowser(self.Intro_Help)
        self.teWelcomeContent.setObjectName(u"teWelcomeContent")
        self.teWelcomeContent.setFont(font1)

        self.verticalLayout_44.addWidget(self.teWelcomeContent)


        self.verticalLayout_13.addWidget(self.Intro_Help)

        self.UC_Main_Frame = QFrame(self.Homepage)
        self.UC_Main_Frame.setObjectName(u"UC_Main_Frame")
        sizePolicy3.setHeightForWidth(self.UC_Main_Frame.sizePolicy().hasHeightForWidth())
        self.UC_Main_Frame.setSizePolicy(sizePolicy3)
        self.UC_Main_Frame.setMinimumSize(QSize(250, 400))
        self.UC_Main_Frame.setMaximumSize(QSize(250, 400))
        self.UC_Main_Frame.setStyleSheet(u"*{\n"
" background-color: #272c35;\n"
"}\n"
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
"    color: #343541;\n"
"	padding: 2px 8px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.UC_Main_Frame.setFrameShape(QFrame.StyledPanel)
        self.UC_Main_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.UC_Main_Frame)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.UC_Headig_frame = QFrame(self.UC_Main_Frame)
        self.UC_Headig_frame.setObjectName(u"UC_Headig_frame")
        self.UC_Headig_frame.setFrameShape(QFrame.StyledPanel)
        self.UC_Headig_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.UC_Headig_frame)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.leUC_Heading = QLabel(self.UC_Headig_frame)
        self.leUC_Heading.setObjectName(u"leUC_Heading")
        font11 = QFont()
        font11.setPointSize(12)
        self.leUC_Heading.setFont(font11)

        self.verticalLayout_80.addWidget(self.leUC_Heading, 0, Qt.AlignHCenter)


        self.verticalLayout_38.addWidget(self.UC_Headig_frame)

        self.UC_Password_Frame = QFrame(self.UC_Main_Frame)
        self.UC_Password_Frame.setObjectName(u"UC_Password_Frame")
        self.UC_Password_Frame.setFrameShape(QFrame.StyledPanel)
        self.UC_Password_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.UC_Password_Frame)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.leUsername = QLineEdit(self.UC_Password_Frame)
        self.leUsername.setObjectName(u"leUsername")
        self.leUsername.setMinimumSize(QSize(200, 40))
        self.leUsername.setMaximumSize(QSize(200, 40))
        self.leUsername.setFont(font1)
        self.leUsername.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom: 7px ")

        self.verticalLayout_81.addWidget(self.leUsername)

        self.lePassword = QLineEdit(self.UC_Password_Frame)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setMinimumSize(QSize(200, 40))
        self.lePassword.setMaximumSize(QSize(200, 40))
        self.lePassword.setFont(font1)
        self.lePassword.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom: 7px ")

        self.verticalLayout_81.addWidget(self.lePassword)


        self.verticalLayout_38.addWidget(self.UC_Password_Frame, 0, Qt.AlignHCenter)

        self.UC_Buttton_Frame = QFrame(self.UC_Main_Frame)
        self.UC_Buttton_Frame.setObjectName(u"UC_Buttton_Frame")
        self.UC_Buttton_Frame.setFrameShape(QFrame.StyledPanel)
        self.UC_Buttton_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.UC_Buttton_Frame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.pbUC_Save = QPushButton(self.UC_Buttton_Frame)
        self.pbUC_Save.setObjectName(u"pbUC_Save")
        self.pbUC_Save.setFont(font1)

        self.horizontalLayout_24.addWidget(self.pbUC_Save)


        self.verticalLayout_38.addWidget(self.UC_Buttton_Frame, 0, Qt.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_7)

        self.pbUC_Cancel = QPushButton(self.UC_Main_Frame)
        self.pbUC_Cancel.setObjectName(u"pbUC_Cancel")
        self.pbUC_Cancel.setFont(font1)

        self.verticalLayout_38.addWidget(self.pbUC_Cancel, 0, Qt.AlignHCenter)

        self.testing = QFrame(self.UC_Main_Frame)
        self.testing.setObjectName(u"testing")
        self.testing.setFrameShape(QFrame.StyledPanel)
        self.testing.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.testing)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.lblLoadVersion = QLabel(self.testing)
        self.lblLoadVersion.setObjectName(u"lblLoadVersion")
        self.lblLoadVersion.setFont(font1)

        self.verticalLayout_82.addWidget(self.lblLoadVersion, 0, Qt.AlignRight)


        self.verticalLayout_38.addWidget(self.testing)


        self.verticalLayout_13.addWidget(self.UC_Main_Frame, 0, Qt.AlignHCenter)

        self.swWorkSpace.addWidget(self.Homepage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.swWorkSpace.addWidget(self.page)
        self.projects = QWidget()
        self.projects.setObjectName(u"projects")
        self.projects.setStyleSheet(u"")
        self.verticalLayout_85 = QVBoxLayout(self.projects)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(6, 6, 6, 6)
        self.fr_headingLable_projects = QWidget(self.projects)
        self.fr_headingLable_projects.setObjectName(u"fr_headingLable_projects")
        self.fr_headingLable_projects.setStyleSheet(u"")
        self.verticalLayout_83 = QVBoxLayout(self.fr_headingLable_projects)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 10, 0, 10)
        self.lbl_heading_Projects = QLabel(self.fr_headingLable_projects)
        self.lbl_heading_Projects.setObjectName(u"lbl_heading_Projects")
        self.lbl_heading_Projects.setFont(font)
        self.lbl_heading_Projects.setAlignment(Qt.AlignCenter)

        self.verticalLayout_83.addWidget(self.lbl_heading_Projects)


        self.verticalLayout_85.addWidget(self.fr_headingLable_projects)

        self.ProjectsMainFrame = QFrame(self.projects)
        self.ProjectsMainFrame.setObjectName(u"ProjectsMainFrame")
        self.ProjectsMainFrame.setStyleSheet(u"")
        self.ProjectsMainFrame.setFrameShape(QFrame.StyledPanel)
        self.ProjectsMainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.ProjectsMainFrame)
        self.verticalLayout_84.setSpacing(10)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.frProjects_Tools = QFrame(self.ProjectsMainFrame)
        self.frProjects_Tools.setObjectName(u"frProjects_Tools")
        self.frProjects_Tools.setStyleSheet(u"*{\n"
" background-color: #272c35;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 1px 8px;\n"
"    border-radius: 6px;\n"
"	background-color:#40414f;\n"
"	padding: 3px 8px;\n"
"	border: 0.5px solid #565869;\n"
"    border-radius: 6px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #8e8ea0;\n"
"	padding: 1px 8px;\n"
"    border-radius: 8px;\n"
"	border: 0.5px solid #acacbe;\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 3px 8px;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.frProjects_Tools.setFrameShape(QFrame.StyledPanel)
        self.frProjects_Tools.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frProjects_Tools)
        self.horizontalLayout_26.setSpacing(20)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.Toggleframe = QFrame(self.frProjects_Tools)
        self.Toggleframe.setObjectName(u"Toggleframe")
        self.Toggleframe.setStyleSheet(u"")
        self.Toggleframe.setFrameShape(QFrame.StyledPanel)
        self.Toggleframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.Toggleframe)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(10, 0, 0, 0)
        self.pbProjects_Connect_properties = QPushButton(self.Toggleframe)
        self.pbProjects_Connect_properties.setObjectName(u"pbProjects_Connect_properties")
        self.pbProjects_Connect_properties.setFont(font9)

        self.horizontalLayout_25.addWidget(self.pbProjects_Connect_properties)


        self.horizontalLayout_26.addWidget(self.Toggleframe)

        self.cmbProjectState = QComboBox(self.frProjects_Tools)
        self.cmbProjectState.addItem("")
        self.cmbProjectState.addItem("")
        self.cmbProjectState.addItem("")
        self.cmbProjectState.addItem("")
        self.cmbProjectState.addItem("")
        self.cmbProjectState.addItem("")
        self.cmbProjectState.setObjectName(u"cmbProjectState")
        self.cmbProjectState.setMinimumSize(QSize(100, 0))
        self.cmbProjectState.setFont(font1)

        self.horizontalLayout_26.addWidget(self.cmbProjectState)

        self.pbRefresh_tblMailabl_projects = QPushButton(self.frProjects_Tools)
        self.pbRefresh_tblMailabl_projects.setObjectName(u"pbRefresh_tblMailabl_projects")
        self.pbRefresh_tblMailabl_projects.setIcon(icon15)
        self.pbRefresh_tblMailabl_projects.setIconSize(QSize(16, 16))

        self.horizontalLayout_26.addWidget(self.pbRefresh_tblMailabl_projects)

        self.pushButton = QPushButton(self.frProjects_Tools)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_26.addWidget(self.pushButton)

        self.Project_Seachframe = QFrame(self.frProjects_Tools)
        self.Project_Seachframe.setObjectName(u"Project_Seachframe")
        self.Project_Seachframe.setStyleSheet(u"#le_searchProjects{\n"
"\n"
"	background-color:#40414f;\n"
"	color:#ececf1;\n"
"	border: 1px solid #565869;\n"
"	border-radius: 3px;\n"
"	padding: 1px\n"
"}")
        self.Project_Seachframe.setFrameShape(QFrame.StyledPanel)
        self.Project_Seachframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.Project_Seachframe)
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 10, 0)
        self.le_searchProjects = QLineEdit(self.Project_Seachframe)
        self.le_searchProjects.setObjectName(u"le_searchProjects")

        self.horizontalLayout_27.addWidget(self.le_searchProjects)


        self.horizontalLayout_26.addWidget(self.Project_Seachframe)


        self.verticalLayout_84.addWidget(self.frProjects_Tools)

        self.frProjects_Checkbox_holder = QFrame(self.ProjectsMainFrame)
        self.frProjects_Checkbox_holder.setObjectName(u"frProjects_Checkbox_holder")
        self.frProjects_Checkbox_holder.setFrameShape(QFrame.StyledPanel)
        self.frProjects_Checkbox_holder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frProjects_Checkbox_holder)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_26)


        self.verticalLayout_84.addWidget(self.frProjects_Checkbox_holder)

        self.tblMailabl_projects = QTableView(self.ProjectsMainFrame)
        self.tblMailabl_projects.setObjectName(u"tblMailabl_projects")
        self.tblMailabl_projects.setStyleSheet(u"background-color: rgb(52, 59, 71);")

        self.verticalLayout_84.addWidget(self.tblMailabl_projects)

        self.frame = QFrame(self.ProjectsMainFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.frame)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(6, 0, 6, 0)

        self.verticalLayout_86.addWidget(self.widget_12)


        self.verticalLayout_84.addWidget(self.frame)


        self.verticalLayout_85.addWidget(self.ProjectsMainFrame)

        self.swWorkSpace.addWidget(self.projects)
        self.RemoveProperties = QWidget()
        self.RemoveProperties.setObjectName(u"RemoveProperties")
        self.verticalLayout_88 = QVBoxLayout(self.RemoveProperties)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.Prygikast = QFrame(self.RemoveProperties)
        self.Prygikast.setObjectName(u"Prygikast")
        self.Prygikast.setStyleSheet(u"background-color: rgb(131, 142, 162);")
        self.Prygikast.setFrameShape(QFrame.StyledPanel)
        self.Prygikast.setFrameShadow(QFrame.Raised)
        self.lePrNewName = QLineEdit(self.Prygikast)
        self.lePrNewName.setObjectName(u"lePrNewName")
        self.lePrNewName.setGeometry(QRect(-80, 70, 295, 16))
        self.lePrNewName.setStyleSheet(u"background-color: rgb(131, 142, 162);\n"
"color: rgb(44, 49, 60);")
        self.label_32 = QLabel(self.Prygikast)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 100, 58, 16))
        self.lePrID = QLineEdit(self.Prygikast)
        self.lePrID.setObjectName(u"lePrID")
        self.lePrID.setGeometry(QRect(-320, 140, 661, 16))
        self.lePrID.setStyleSheet(u"background-color: rgb(131, 142, 162);\n"
"color: rgb(31, 35, 42);")
        self.label_26 = QLabel(self.Prygikast)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(30, 90, 717, 13))
        self.pbShowOnMap = QPushButton(self.Prygikast)
        self.pbShowOnMap.setObjectName(u"pbShowOnMap")
        self.pbShowOnMap.setGeometry(QRect(-180, 120, 353, 20))
        self.pbShowOnMap.setFont(font1)
        self.testView = QTableView(self.Prygikast)
        self.testView.setObjectName(u"testView")
        self.testView.setGeometry(QRect(70, 240, 371, 192))

        self.verticalLayout_88.addWidget(self.Prygikast)

        self.swWorkSpace.addWidget(self.RemoveProperties)

        self.verticalLayout_11.addWidget(self.swWorkSpace)

        self.Genrealprogresbar = QFrame(self.centerMenuSubContainer)
        self.Genrealprogresbar.setObjectName(u"Genrealprogresbar")
        self.Genrealprogresbar.setMinimumSize(QSize(0, 5))
        self.Genrealprogresbar.setMaximumSize(QSize(16777215, 5))
        self.Genrealprogresbar.setStyleSheet(u"")
        self.Genrealprogresbar.setFrameShape(QFrame.StyledPanel)
        self.Genrealprogresbar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.Genrealprogresbar)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.ProgresBar_general = QProgressBar(self.Genrealprogresbar)
        self.ProgresBar_general.setObjectName(u"ProgresBar_general")
        self.ProgresBar_general.setMaximum(100)
        self.ProgresBar_general.setValue(0)

        self.verticalLayout_25.addWidget(self.ProgresBar_general)


        self.verticalLayout_11.addWidget(self.Genrealprogresbar)


        self.verticalLayout_10.addWidget(self.centerMenuSubContainer)


        self.horizontalLayout_6.addWidget(self.centerMenuContainer)

        self.rightMenuContainer = QWidget(MailablDialogBase)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.rightMenuContainer.sizePolicy().hasHeightForWidth())
        self.rightMenuContainer.setSizePolicy(sizePolicy5)
        self.rightMenuContainer.setMinimumSize(QSize(250, 0))
        font12 = QFont()
        font12.setFamilies([u"MV Boli"])
        self.rightMenuContainer.setFont(font12)
        self.rightMenuContainer.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.mbsc_Top = QFrame(self.rightMenuSubContainer)
        self.mbsc_Top.setObjectName(u"mbsc_Top")
        sizePolicy4.setHeightForWidth(self.mbsc_Top.sizePolicy().hasHeightForWidth())
        self.mbsc_Top.setSizePolicy(sizePolicy4)
        self.mbsc_Top.setFrameShape(QFrame.StyledPanel)
        self.mbsc_Top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.mbsc_Top)
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 10, 0, 0)
        self.frame_7 = QFrame(self.mbsc_Top)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy4.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy4)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_7)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.pbMailabl = QPushButton(self.frame_7)
        self.pbMailabl.setObjectName(u"pbMailabl")
        sizePolicy3.setHeightForWidth(self.pbMailabl.sizePolicy().hasHeightForWidth())
        self.pbMailabl.setSizePolicy(sizePolicy3)
        icon21 = QIcon()
        icon21.addFile(u"icon - square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbMailabl.setIcon(icon21)
        self.pbMailabl.setIconSize(QSize(18, 18))

        self.verticalLayout_55.addWidget(self.pbMailabl, 0, Qt.AlignRight)

        self.helpMenuToggle = QPushButton(self.frame_7)
        self.helpMenuToggle.setObjectName(u"helpMenuToggle")
        self.helpMenuToggle.setStyleSheet(u"* {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"	margin-right:10\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    image: none;\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u"icons/Icons_hele/toggle-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpMenuToggle.setIcon(icon22)
        self.helpMenuToggle.setIconSize(QSize(20, 20))

        self.verticalLayout_55.addWidget(self.helpMenuToggle)


        self.horizontalLayout_38.addWidget(self.frame_7)


        self.verticalLayout_18.addWidget(self.mbsc_Top)

        self.helpMenu = QFrame(self.rightMenuSubContainer)
        self.helpMenu.setObjectName(u"helpMenu")
        sizePolicy4.setHeightForWidth(self.helpMenu.sizePolicy().hasHeightForWidth())
        self.helpMenu.setSizePolicy(sizePolicy4)
        self.helpMenu.setStyleSheet(u"")
        self.helpMenu.setFrameShape(QFrame.StyledPanel)
        self.helpMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.helpMenu)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.sw_HM = QStackedWidget(self.helpMenu)
        self.sw_HM.setObjectName(u"sw_HM")
        font13 = QFont()
        font13.setPointSize(11)
        font13.setBold(True)
        self.sw_HM.setFont(font13)
        self.sw_HM.setStyleSheet(u"")
        self.w_HM_Avaleht = QWidget()
        self.w_HM_Avaleht.setObjectName(u"w_HM_Avaleht")
        self.w_HM_Avaleht.setMinimumSize(QSize(0, 400))
        self.verticalLayout_6 = QVBoxLayout(self.w_HM_Avaleht)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.f_w_HM_Avaleht_Pealkiri = QFrame(self.w_HM_Avaleht)
        self.f_w_HM_Avaleht_Pealkiri.setObjectName(u"f_w_HM_Avaleht_Pealkiri")
        self.f_w_HM_Avaleht_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_w_HM_Avaleht_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.f_w_HM_Avaleht_Pealkiri)
        self.verticalLayout_113.setSpacing(5)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(6, 5, 5, 5)
        self.lb_HM_Avaleht_Pealkiri = QLabel(self.f_w_HM_Avaleht_Pealkiri)
        self.lb_HM_Avaleht_Pealkiri.setObjectName(u"lb_HM_Avaleht_Pealkiri")
        self.lb_HM_Avaleht_Pealkiri.setFont(font13)

        self.verticalLayout_113.addWidget(self.lb_HM_Avaleht_Pealkiri)


        self.verticalLayout_6.addWidget(self.f_w_HM_Avaleht_Pealkiri, 0, Qt.AlignTop)

        self.f_HM_Avaleht_Sisu = QFrame(self.w_HM_Avaleht)
        self.f_HM_Avaleht_Sisu.setObjectName(u"f_HM_Avaleht_Sisu")
        self.f_HM_Avaleht_Sisu.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Avaleht_Sisu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_130 = QVBoxLayout(self.f_HM_Avaleht_Sisu)
        self.verticalLayout_130.setSpacing(5)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Avaleht_Sisu = QTextEdit(self.f_HM_Avaleht_Sisu)
        self.te_HM_Avaleht_Sisu.setObjectName(u"te_HM_Avaleht_Sisu")
        self.te_HM_Avaleht_Sisu.setReadOnly(True)

        self.verticalLayout_130.addWidget(self.te_HM_Avaleht_Sisu)


        self.verticalLayout_6.addWidget(self.f_HM_Avaleht_Sisu)

        self.sw_HM.addWidget(self.w_HM_Avaleht)
        self.w_HM_Lepingud = QWidget()
        self.w_HM_Lepingud.setObjectName(u"w_HM_Lepingud")
        self.verticalLayout_51 = QVBoxLayout(self.w_HM_Lepingud)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Lepingud_Pealkiri = QFrame(self.w_HM_Lepingud)
        self.f_HM_Lepingud_Pealkiri.setObjectName(u"f_HM_Lepingud_Pealkiri")
        self.f_HM_Lepingud_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Lepingud_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.f_HM_Lepingud_Pealkiri)
        self.verticalLayout_48.setSpacing(5)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(6, 0, 0, 0)
        self.lb_HM_LepingudPealkiri = QLabel(self.f_HM_Lepingud_Pealkiri)
        self.lb_HM_LepingudPealkiri.setObjectName(u"lb_HM_LepingudPealkiri")
        self.lb_HM_LepingudPealkiri.setFont(font13)

        self.verticalLayout_48.addWidget(self.lb_HM_LepingudPealkiri)


        self.verticalLayout_51.addWidget(self.f_HM_Lepingud_Pealkiri)

        self.sw_HM.addWidget(self.w_HM_Lepingud)
        self.w_HM_Teostusjoonised = QWidget()
        self.w_HM_Teostusjoonised.setObjectName(u"w_HM_Teostusjoonised")
        self.verticalLayout_57 = QVBoxLayout(self.w_HM_Teostusjoonised)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Teostusjoonised_Pealkiri = QFrame(self.w_HM_Teostusjoonised)
        self.f_HM_Teostusjoonised_Pealkiri.setObjectName(u"f_HM_Teostusjoonised_Pealkiri")
        self.f_HM_Teostusjoonised_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Teostusjoonised_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.f_HM_Teostusjoonised_Pealkiri)
        self.verticalLayout_111.setSpacing(5)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(6, 0, 0, 0)
        self.lb_HM_Teostusjoonised_Pealkiri = QLabel(self.f_HM_Teostusjoonised_Pealkiri)
        self.lb_HM_Teostusjoonised_Pealkiri.setObjectName(u"lb_HM_Teostusjoonised_Pealkiri")
        self.lb_HM_Teostusjoonised_Pealkiri.setFont(font13)

        self.verticalLayout_111.addWidget(self.lb_HM_Teostusjoonised_Pealkiri)


        self.verticalLayout_57.addWidget(self.f_HM_Teostusjoonised_Pealkiri)

        self.sw_HM.addWidget(self.w_HM_Teostusjoonised)
        self.w_HM_Toimingud_kinnistutega = QWidget()
        self.w_HM_Toimingud_kinnistutega.setObjectName(u"w_HM_Toimingud_kinnistutega")
        self.verticalLayout_62 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingu_kinnistutega_Pea = QFrame(self.w_HM_Toimingud_kinnistutega)
        self.f_HM_Toimingu_kinnistutega_Pea.setObjectName(u"f_HM_Toimingu_kinnistutega_Pea")
        self.f_HM_Toimingu_kinnistutega_Pea.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingu_kinnistutega_Pea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.f_HM_Toimingu_kinnistutega_Pea)
        self.verticalLayout_61.setSpacing(5)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Pealkiri = QFrame(self.f_HM_Toimingu_kinnistutega_Pea)
        self.f_HM_Toimingud_kinnistutega_Pealkiri.setObjectName(u"f_HM_Toimingud_kinnistutega_Pealkiri")
        self.f_HM_Toimingud_kinnistutega_Pealkiri.setFont(font13)
        self.f_HM_Toimingud_kinnistutega_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Pealkiri)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(5, 5, 0, 5)
        self.lb_f_HM_Toimingud_kinnistutega_Pealkiri = QLabel(self.f_HM_Toimingud_kinnistutega_Pealkiri)
        self.lb_f_HM_Toimingud_kinnistutega_Pealkiri.setObjectName(u"lb_f_HM_Toimingud_kinnistutega_Pealkiri")
        self.lb_f_HM_Toimingud_kinnistutega_Pealkiri.setFont(font13)

        self.verticalLayout_66.addWidget(self.lb_f_HM_Toimingud_kinnistutega_Pealkiri)


        self.verticalLayout_61.addWidget(self.f_HM_Toimingud_kinnistutega_Pealkiri)

        self.f_HM_Toimingud_kinnistutega_Sisu = QFrame(self.f_HM_Toimingu_kinnistutega_Pea)
        self.f_HM_Toimingud_kinnistutega_Sisu.setObjectName(u"f_HM_Toimingud_kinnistutega_Sisu")
        self.f_HM_Toimingud_kinnistutega_Sisu.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Sisu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Sisu)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(10, 5, 0, 0)
        self.sw_HM_Toimingud_kinnistutega = QStackedWidget(self.f_HM_Toimingud_kinnistutega_Sisu)
        self.sw_HM_Toimingud_kinnistutega.setObjectName(u"sw_HM_Toimingud_kinnistutega")
        self.sw_HM_Toimingud_kinnistutega.setStyleSheet(u"")
        self.w_HM_Toimingud_kinnistutega_Laiendamine = QWidget()
        self.w_HM_Toimingud_kinnistutega_Laiendamine.setObjectName(u"w_HM_Toimingud_kinnistutega_Laiendamine")
        self.w_HM_Toimingud_kinnistutega_Laiendamine.setStyleSheet(u"")
        self.verticalLayout_68 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Laiendamine)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri = QFrame(self.w_HM_Toimingud_kinnistutega_Laiendamine)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri.setObjectName(u"f_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri.setStyleSheet(u"")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri)
        self.verticalLayout_69.setSpacing(5)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(6, 5, 0, 5)
        self.lb_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri = QLabel(self.f_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri)
        self.lb_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri.setObjectName(u"lb_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri")
        font14 = QFont()
        font14.setFamilies([u"MS Shell Dlg 2"])
        font14.setPointSize(10)
        font14.setBold(False)
        font14.setItalic(False)
        self.lb_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri.setFont(font14)
        self.lb_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_69.addWidget(self.lb_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri)


        self.verticalLayout_68.addWidget(self.f_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri)

        self.f_HM_Toimingud_kinnistutega_Laiendamine_raam = QFrame(self.w_HM_Toimingud_kinnistutega_Laiendamine)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_raam.setObjectName(u"f_HM_Toimingud_kinnistutega_Laiendamine_raam")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_raam.setStyleSheet(u"")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_raam.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_raam.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Laiendamine_raam)
        self.verticalLayout_87.setSpacing(5)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(6, 5, 5, 5)
        self.sw_HM_Toimingud_kinnistutega_Laiendamine = QStackedWidget(self.f_HM_Toimingud_kinnistutega_Laiendamine_raam)
        self.sw_HM_Toimingud_kinnistutega_Laiendamine.setObjectName(u"sw_HM_Toimingud_kinnistutega_Laiendamine")
        self.sw_HM_Toimingud_kinnistutega_Laiendamine.setStyleSheet(u"")
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Yldine = QWidget()
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Yldine.setObjectName(u"w_HM_Toimingud_kinnistutega_Laiendamine_Yldine")
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Yldine.setStyleSheet(u"")
        self.verticalLayout_89 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Laiendamine_Yldine)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Yldine = QFrame(self.w_HM_Toimingud_kinnistutega_Laiendamine_Yldine)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Yldine.setObjectName(u"f_HM_Toimingud_kinnistutega_Laiendamine_Yldine")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Yldine.setStyleSheet(u"")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Yldine.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Yldine.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Laiendamine_Yldine)
        self.verticalLayout_90.setSpacing(5)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Yldine = QTextEdit(self.f_HM_Toimingud_kinnistutega_Laiendamine_Yldine)
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Yldine.setObjectName(u"te_HM_Toimingud_kinnistutega_Laiendamine_Yldine")
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Yldine.setStyleSheet(u"")
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Yldine.setReadOnly(True)

        self.verticalLayout_90.addWidget(self.te_HM_Toimingud_kinnistutega_Laiendamine_Yldine)


        self.verticalLayout_89.addWidget(self.f_HM_Toimingud_kinnistutega_Laiendamine_Yldine)

        self.sw_HM_Toimingud_kinnistutega_Laiendamine.addWidget(self.w_HM_Toimingud_kinnistutega_Laiendamine_Yldine)
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Maakond = QWidget()
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Maakond.setObjectName(u"w_HM_Toimingud_kinnistutega_Laiendamine_Maakond")
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Maakond.setStyleSheet(u"")
        self.verticalLayout_91 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Laiendamine_Maakond)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Maakond = QFrame(self.w_HM_Toimingud_kinnistutega_Laiendamine_Maakond)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Maakond.setObjectName(u"f_HM_Toimingud_kinnistutega_Laiendamine_Maakond")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Maakond.setStyleSheet(u"")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Maakond.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Maakond.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Laiendamine_Maakond)
        self.verticalLayout_92.setSpacing(5)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Maakond = QTextEdit(self.f_HM_Toimingud_kinnistutega_Laiendamine_Maakond)
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Maakond.setObjectName(u"te_HM_Toimingud_kinnistutega_Laiendamine_Maakond")
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Maakond.setStyleSheet(u"")
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Maakond.setReadOnly(True)

        self.verticalLayout_92.addWidget(self.te_HM_Toimingud_kinnistutega_Laiendamine_Maakond)


        self.verticalLayout_91.addWidget(self.f_HM_Toimingud_kinnistutega_Laiendamine_Maakond)

        self.sw_HM_Toimingud_kinnistutega_Laiendamine.addWidget(self.w_HM_Toimingud_kinnistutega_Laiendamine_Maakond)
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus = QWidget()
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus.setObjectName(u"w_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus")
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus.setStyleSheet(u"")
        self.verticalLayout_93 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus = QFrame(self.w_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus.setObjectName(u"f_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus.setStyleSheet(u"")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus)
        self.verticalLayout_94.setSpacing(5)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(6, 5, 5, 5)
        self.te_Laiente_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus = QTextEdit(self.f_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus)
        self.te_Laiente_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus.setObjectName(u"te_Laiente_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus")
        self.te_Laiente_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus.setStyleSheet(u"")
        self.te_Laiente_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus.setReadOnly(True)

        self.verticalLayout_94.addWidget(self.te_Laiente_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus)


        self.verticalLayout_93.addWidget(self.f_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus)

        self.sw_HM_Toimingud_kinnistutega_Laiendamine.addWidget(self.w_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus)
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla = QWidget()
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla.setObjectName(u"w_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla")
        self.w_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla.setStyleSheet(u"")
        self.verticalLayout_95 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla = QFrame(self.w_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla.setObjectName(u"f_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla.setStyleSheet(u"")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla)
        self.verticalLayout_96.setSpacing(5)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla = QTextEdit(self.f_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla)
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla.setObjectName(u"te_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla")
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla.setStyleSheet(u"")
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla.setReadOnly(True)

        self.verticalLayout_96.addWidget(self.te_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla)


        self.verticalLayout_95.addWidget(self.f_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla)

        self.sw_HM_Toimingud_kinnistutega_Laiendamine.addWidget(self.w_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla)
        self.w_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud = QWidget()
        self.w_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud.setObjectName(u"w_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud")
        self.verticalLayout_120 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud = QFrame(self.w_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud.setObjectName(u"f_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud")
        self.f_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud)
        self.verticalLayout_115.setSpacing(5)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud = QTextEdit(self.f_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud)
        self.te_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud.setObjectName(u"te_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud")
        self.te_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud.setReadOnly(True)

        self.verticalLayout_115.addWidget(self.te_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud)


        self.verticalLayout_120.addWidget(self.f_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud)

        self.sw_HM_Toimingud_kinnistutega_Laiendamine.addWidget(self.w_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud)

        self.verticalLayout_87.addWidget(self.sw_HM_Toimingud_kinnistutega_Laiendamine)


        self.verticalLayout_68.addWidget(self.f_HM_Toimingud_kinnistutega_Laiendamine_raam)

        self.sw_HM_Toimingud_kinnistutega.addWidget(self.w_HM_Toimingud_kinnistutega_Laiendamine)
        self.w_HM_Toimingud_kinnistutega_Kitsendamine = QWidget()
        self.w_HM_Toimingud_kinnistutega_Kitsendamine.setObjectName(u"w_HM_Toimingud_kinnistutega_Kitsendamine")
        self.w_HM_Toimingud_kinnistutega_Kitsendamine.setStyleSheet(u"")
        self.verticalLayout_97 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Kitsendamine)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri = QFrame(self.w_HM_Toimingud_kinnistutega_Kitsendamine)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri.setObjectName(u"f_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri")
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri.setStyleSheet(u"")
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri)
        self.verticalLayout_98.setSpacing(5)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(6, 5, 5, 5)
        self.lb_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri = QLabel(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri)
        self.lb_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri.setObjectName(u"lb_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri")
        self.lb_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri.setFont(font14)
        self.lb_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_98.addWidget(self.lb_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri)


        self.verticalLayout_97.addWidget(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri)

        self.f_HM_Toimingud_kinnistutega_Kitsendamine_raam = QFrame(self.w_HM_Toimingud_kinnistutega_Kitsendamine)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_raam.setObjectName(u"f_HM_Toimingud_kinnistutega_Kitsendamine_raam")
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_raam.setStyleSheet(u"")
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_raam.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_raam.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Kitsendamine_raam)
        self.verticalLayout_99.setSpacing(5)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(6, 5, 5, 5)
        self.sw_HM_Toimingud_kinnistutega_Kitsendamine = QStackedWidget(self.f_HM_Toimingud_kinnistutega_Kitsendamine_raam)
        self.sw_HM_Toimingud_kinnistutega_Kitsendamine.setObjectName(u"sw_HM_Toimingud_kinnistutega_Kitsendamine")
        self.sw_HM_Toimingud_kinnistutega_Kitsendamine.setStyleSheet(u"")
        self.w_HM_Toimingud_kinnistutega_Kitsendamine_Yldine = QWidget()
        self.w_HM_Toimingud_kinnistutega_Kitsendamine_Yldine.setObjectName(u"w_HM_Toimingud_kinnistutega_Kitsendamine_Yldine")
        self.w_HM_Toimingud_kinnistutega_Kitsendamine_Yldine.setStyleSheet(u"")
        self.verticalLayout_100 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Yldine)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Yldine = QFrame(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Yldine)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Yldine.setObjectName(u"f_HM_Toimingud_kinnistutega_Kitsendamine_Yldine")
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Yldine.setStyleSheet(u"")
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Yldine.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Yldine.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Yldine)
        self.verticalLayout_101.setSpacing(5)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Yldine = QTextEdit(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Yldine)
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Yldine.setObjectName(u"te_HM_Toimingud_kinnistutega_Kitsendamine_Yldine")
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Yldine.setStyleSheet(u"")
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Yldine.setReadOnly(True)

        self.verticalLayout_101.addWidget(self.te_HM_Toimingud_kinnistutega_Kitsendamine_Yldine)


        self.verticalLayout_100.addWidget(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Yldine)

        self.sw_HM_Toimingud_kinnistutega_Kitsendamine.addWidget(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Yldine)
        self.w_HM_Toimingud_kinnistutega_Kitsendamine_Maakond = QWidget()
        self.w_HM_Toimingud_kinnistutega_Kitsendamine_Maakond.setObjectName(u"w_HM_Toimingud_kinnistutega_Kitsendamine_Maakond")
        self.w_HM_Toimingud_kinnistutega_Kitsendamine_Maakond.setStyleSheet(u"")
        self.verticalLayout_102 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Maakond)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Maakond = QFrame(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Maakond)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Maakond.setObjectName(u"f_HM_Toimingud_kinnistutega_Kitsendamine_Maakond")
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Maakond.setStyleSheet(u"")
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Maakond.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Maakond.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Maakond)
        self.verticalLayout_103.setSpacing(5)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Maakond = QTextEdit(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Maakond)
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Maakond.setObjectName(u"te_HM_Toimingud_kinnistutega_Kitsendamine_Maakond")
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Maakond.setStyleSheet(u"")
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Maakond.setReadOnly(True)

        self.verticalLayout_103.addWidget(self.te_HM_Toimingud_kinnistutega_Kitsendamine_Maakond)


        self.verticalLayout_102.addWidget(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Maakond)

        self.sw_HM_Toimingud_kinnistutega_Kitsendamine.addWidget(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Maakond)
        self.w_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus = QWidget()
        self.w_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus.setObjectName(u"w_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus")
        self.verticalLayout_136 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus = QFrame(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus.setObjectName(u"f_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus")
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus)
        self.verticalLayout_135.setSpacing(5)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus = QTextEdit(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus)
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus.setObjectName(u"te_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus")
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus.setReadOnly(True)

        self.verticalLayout_135.addWidget(self.te_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus)


        self.verticalLayout_136.addWidget(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus)

        self.sw_HM_Toimingud_kinnistutega_Kitsendamine.addWidget(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus)
        self.w_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla = QWidget()
        self.w_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla.setObjectName(u"w_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla")
        self.verticalLayout_138 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla)
        self.verticalLayout_138.setSpacing(0)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla = QFrame(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla.setObjectName(u"f_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla")
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla.setFrameShadow(QFrame.Raised)
        self.verticalLayout_137 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla)
        self.verticalLayout_137.setSpacing(5)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla = QTextEdit(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla)
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla.setObjectName(u"te_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla")
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla.setReadOnly(True)

        self.verticalLayout_137.addWidget(self.te_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla)


        self.verticalLayout_138.addWidget(self.f_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla)

        self.sw_HM_Toimingud_kinnistutega_Kitsendamine.addWidget(self.w_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla)

        self.verticalLayout_99.addWidget(self.sw_HM_Toimingud_kinnistutega_Kitsendamine)


        self.verticalLayout_97.addWidget(self.f_HM_Toimingud_kinnistutega_Kitsendamine_raam)

        self.sw_HM_Toimingud_kinnistutega.addWidget(self.w_HM_Toimingud_kinnistutega_Kitsendamine)
        self.w_HM_Toimingud_kinnistutega_Yldine_kirjeldus = QWidget()
        self.w_HM_Toimingud_kinnistutega_Yldine_kirjeldus.setObjectName(u"w_HM_Toimingud_kinnistutega_Yldine_kirjeldus")
        self.verticalLayout_24 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Yldine_kirjeldus)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lb_HM_Toimingud_kinnistutega_Yldine_kirjeldus = QLabel(self.w_HM_Toimingud_kinnistutega_Yldine_kirjeldus)
        self.lb_HM_Toimingud_kinnistutega_Yldine_kirjeldus.setObjectName(u"lb_HM_Toimingud_kinnistutega_Yldine_kirjeldus")
        self.lb_HM_Toimingud_kinnistutega_Yldine_kirjeldus.setFont(font9)

        self.verticalLayout_24.addWidget(self.lb_HM_Toimingud_kinnistutega_Yldine_kirjeldus)

        self.te_HM_Toimingud_kinnistutega_Yldine_kirjeldus = QTextEdit(self.w_HM_Toimingud_kinnistutega_Yldine_kirjeldus)
        self.te_HM_Toimingud_kinnistutega_Yldine_kirjeldus.setObjectName(u"te_HM_Toimingud_kinnistutega_Yldine_kirjeldus")
        self.te_HM_Toimingud_kinnistutega_Yldine_kirjeldus.setReadOnly(True)

        self.verticalLayout_24.addWidget(self.te_HM_Toimingud_kinnistutega_Yldine_kirjeldus)

        self.sw_HM_Toimingud_kinnistutega.addWidget(self.w_HM_Toimingud_kinnistutega_Yldine_kirjeldus)
        self.w_HM_Toimingud_kinnistutega_Aluskaardi_koostamine = QWidget()
        self.w_HM_Toimingud_kinnistutega_Aluskaardi_koostamine.setObjectName(u"w_HM_Toimingud_kinnistutega_Aluskaardi_koostamine")
        self.verticalLayout_153 = QVBoxLayout(self.w_HM_Toimingud_kinnistutega_Aluskaardi_koostamine)
        self.verticalLayout_153.setSpacing(0)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.verticalLayout_153.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri = QFrame(self.w_HM_Toimingud_kinnistutega_Aluskaardi_koostamine)
        self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri.setObjectName(u"f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri")
        self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri)
        self.verticalLayout_154.setSpacing(5)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(6, 5, 5, 5)
        self.lb_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri = QLabel(self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri)
        self.lb_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri.setObjectName(u"lb_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri")
        self.lb_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri.setFont(font9)

        self.verticalLayout_154.addWidget(self.lb_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri)


        self.verticalLayout_153.addWidget(self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri)

        self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu = QFrame(self.w_HM_Toimingud_kinnistutega_Aluskaardi_koostamine)
        self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu.setObjectName(u"f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu")
        self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu)
        self.verticalLayout_155.setSpacing(5)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.verticalLayout_155.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu = QTextEdit(self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu)
        self.te_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu.setObjectName(u"te_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu")
        self.te_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu.setReadOnly(True)

        self.verticalLayout_155.addWidget(self.te_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu)


        self.verticalLayout_153.addWidget(self.f_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu)

        self.sw_HM_Toimingud_kinnistutega.addWidget(self.w_HM_Toimingud_kinnistutega_Aluskaardi_koostamine)

        self.verticalLayout_67.addWidget(self.sw_HM_Toimingud_kinnistutega)


        self.verticalLayout_61.addWidget(self.f_HM_Toimingud_kinnistutega_Sisu)


        self.verticalLayout_62.addWidget(self.f_HM_Toimingu_kinnistutega_Pea)

        self.sw_HM.addWidget(self.w_HM_Toimingud_kinnistutega)
        self.w_HM_Satted = QWidget()
        self.w_HM_Satted.setObjectName(u"w_HM_Satted")
        self.verticalLayout_60 = QVBoxLayout(self.w_HM_Satted)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Satted_Pealkiri = QFrame(self.w_HM_Satted)
        self.f_HM_Satted_Pealkiri.setObjectName(u"f_HM_Satted_Pealkiri")
        self.f_HM_Satted_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Satted_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.f_HM_Satted_Pealkiri)
        self.verticalLayout_47.setSpacing(5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(6, 5, 5, 5)
        self.lb_HM_Satted_Pealkiri = QLabel(self.f_HM_Satted_Pealkiri)
        self.lb_HM_Satted_Pealkiri.setObjectName(u"lb_HM_Satted_Pealkiri")
        self.lb_HM_Satted_Pealkiri.setFont(font13)

        self.verticalLayout_47.addWidget(self.lb_HM_Satted_Pealkiri)


        self.verticalLayout_60.addWidget(self.f_HM_Satted_Pealkiri)

        self.f_HM_Satted_Sisu = QFrame(self.w_HM_Satted)
        self.f_HM_Satted_Sisu.setObjectName(u"f_HM_Satted_Sisu")
        self.f_HM_Satted_Sisu.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Satted_Sisu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.f_HM_Satted_Sisu)
        self.verticalLayout_59.setSpacing(5)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Satted_Sisu = QTextEdit(self.f_HM_Satted_Sisu)
        self.te_HM_Satted_Sisu.setObjectName(u"te_HM_Satted_Sisu")
        self.te_HM_Satted_Sisu.setReadOnly(True)

        self.verticalLayout_59.addWidget(self.te_HM_Satted_Sisu)


        self.verticalLayout_60.addWidget(self.f_HM_Satted_Sisu)

        self.sw_HM.addWidget(self.w_HM_Satted)
        self.w_HM_Servituudid = QWidget()
        self.w_HM_Servituudid.setObjectName(u"w_HM_Servituudid")
        self.verticalLayout_122 = QVBoxLayout(self.w_HM_Servituudid)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.f_HM_Servituudid_Pealkiri = QFrame(self.w_HM_Servituudid)
        self.f_HM_Servituudid_Pealkiri.setObjectName(u"f_HM_Servituudid_Pealkiri")
        self.f_HM_Servituudid_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Servituudid_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.f_HM_Servituudid_Pealkiri)
        self.verticalLayout_116.setSpacing(5)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(6, 5, 5, 5)
        self.lb_HM_Servituudid_Pealkiri = QLabel(self.f_HM_Servituudid_Pealkiri)
        self.lb_HM_Servituudid_Pealkiri.setObjectName(u"lb_HM_Servituudid_Pealkiri")
        self.lb_HM_Servituudid_Pealkiri.setFont(font13)

        self.verticalLayout_116.addWidget(self.lb_HM_Servituudid_Pealkiri)


        self.verticalLayout_122.addWidget(self.f_HM_Servituudid_Pealkiri)

        self.sw_HM.addWidget(self.w_HM_Servituudid)
        self.w_HM_Teemakaardid = QWidget()
        self.w_HM_Teemakaardid.setObjectName(u"w_HM_Teemakaardid")
        self.verticalLayout_117 = QVBoxLayout(self.w_HM_Teemakaardid)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Teemakaardid_Pealkiri = QFrame(self.w_HM_Teemakaardid)
        self.f_HM_Teemakaardid_Pealkiri.setObjectName(u"f_HM_Teemakaardid_Pealkiri")
        self.f_HM_Teemakaardid_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Teemakaardid_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.f_HM_Teemakaardid_Pealkiri)
        self.verticalLayout_123.setSpacing(5)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(6, 5, 5, 5)
        self.lb_HM_Teemakaardid_Pealkiri = QLabel(self.f_HM_Teemakaardid_Pealkiri)
        self.lb_HM_Teemakaardid_Pealkiri.setObjectName(u"lb_HM_Teemakaardid_Pealkiri")
        self.lb_HM_Teemakaardid_Pealkiri.setFont(font13)

        self.verticalLayout_123.addWidget(self.lb_HM_Teemakaardid_Pealkiri)


        self.verticalLayout_117.addWidget(self.f_HM_Teemakaardid_Pealkiri)

        self.sw_HM.addWidget(self.w_HM_Teemakaardid)
        self.w_HM_Andmete_laadimine = QWidget()
        self.w_HM_Andmete_laadimine.setObjectName(u"w_HM_Andmete_laadimine")
        self.verticalLayout_126 = QVBoxLayout(self.w_HM_Andmete_laadimine)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Andmete_laadimine_Pea = QFrame(self.w_HM_Andmete_laadimine)
        self.f_HM_Andmete_laadimine_Pea.setObjectName(u"f_HM_Andmete_laadimine_Pea")
        self.f_HM_Andmete_laadimine_Pea.setStyleSheet(u"")
        self.f_HM_Andmete_laadimine_Pea.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Andmete_laadimine_Pea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.f_HM_Andmete_laadimine_Pea)
        self.verticalLayout_125.setSpacing(5)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(6, 5, 5, 5)
        self.lb_HM_Andmete_laadimine_Pealkiri = QLabel(self.f_HM_Andmete_laadimine_Pea)
        self.lb_HM_Andmete_laadimine_Pealkiri.setObjectName(u"lb_HM_Andmete_laadimine_Pealkiri")
        font15 = QFont()
        font15.setPointSize(11)
        font15.setBold(True)
        font15.setStrikeOut(False)
        font15.setKerning(True)
        self.lb_HM_Andmete_laadimine_Pealkiri.setFont(font15)

        self.verticalLayout_125.addWidget(self.lb_HM_Andmete_laadimine_Pealkiri)

        self.f_HM_Andmete_laadimine_Pealkiri = QFrame(self.f_HM_Andmete_laadimine_Pea)
        self.f_HM_Andmete_laadimine_Pealkiri.setObjectName(u"f_HM_Andmete_laadimine_Pealkiri")
        self.f_HM_Andmete_laadimine_Pealkiri.setStyleSheet(u"")
        self.f_HM_Andmete_laadimine_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Andmete_laadimine_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.f_HM_Andmete_laadimine_Pealkiri)
        self.verticalLayout_121.setSpacing(5)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(6, 5, 5, 5)
        self.sw_HM_Andmete_laadimine = QStackedWidget(self.f_HM_Andmete_laadimine_Pealkiri)
        self.sw_HM_Andmete_laadimine.setObjectName(u"sw_HM_Andmete_laadimine")
        self.sw_HM_Andmete_laadimine.setStyleSheet(u"")
        self.w_HM_Andmete_laadimine_Yldine = QWidget()
        self.w_HM_Andmete_laadimine_Yldine.setObjectName(u"w_HM_Andmete_laadimine_Yldine")
        self.verticalLayout_127 = QVBoxLayout(self.w_HM_Andmete_laadimine_Yldine)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Andmete_laadimine_Yldine = QFrame(self.w_HM_Andmete_laadimine_Yldine)
        self.f_HM_Andmete_laadimine_Yldine.setObjectName(u"f_HM_Andmete_laadimine_Yldine")
        self.f_HM_Andmete_laadimine_Yldine.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Andmete_laadimine_Yldine.setFrameShadow(QFrame.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.f_HM_Andmete_laadimine_Yldine)
        self.verticalLayout_128.setSpacing(5)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(6, 5, 5, 5)
        self.frame_2 = QFrame(self.f_HM_Andmete_laadimine_Yldine)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_156 = QVBoxLayout(self.frame_2)
        self.verticalLayout_156.setSpacing(0)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.lbl_HM_Andmete_Laadimine_Yldine = QLabel(self.frame_2)
        self.lbl_HM_Andmete_Laadimine_Yldine.setObjectName(u"lbl_HM_Andmete_Laadimine_Yldine")

        self.verticalLayout_156.addWidget(self.lbl_HM_Andmete_Laadimine_Yldine)


        self.verticalLayout_128.addWidget(self.frame_2)

        self.te_HM_Andmete_laadimine_Yldine = QTextEdit(self.f_HM_Andmete_laadimine_Yldine)
        self.te_HM_Andmete_laadimine_Yldine.setObjectName(u"te_HM_Andmete_laadimine_Yldine")
        self.te_HM_Andmete_laadimine_Yldine.setReadOnly(True)

        self.verticalLayout_128.addWidget(self.te_HM_Andmete_laadimine_Yldine)


        self.verticalLayout_127.addWidget(self.f_HM_Andmete_laadimine_Yldine)

        self.sw_HM_Andmete_laadimine.addWidget(self.w_HM_Andmete_laadimine_Yldine)
        self.w_HM_Andmete_laadimine_Algandmete_laadimine = QWidget()
        self.w_HM_Andmete_laadimine_Algandmete_laadimine.setObjectName(u"w_HM_Andmete_laadimine_Algandmete_laadimine")
        self.verticalLayout_132 = QVBoxLayout(self.w_HM_Andmete_laadimine_Algandmete_laadimine)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.f_HM_Andmete_laadimine_Algandmete_laadimine = QFrame(self.w_HM_Andmete_laadimine_Algandmete_laadimine)
        self.f_HM_Andmete_laadimine_Algandmete_laadimine.setObjectName(u"f_HM_Andmete_laadimine_Algandmete_laadimine")
        self.f_HM_Andmete_laadimine_Algandmete_laadimine.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Andmete_laadimine_Algandmete_laadimine.setFrameShadow(QFrame.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.f_HM_Andmete_laadimine_Algandmete_laadimine)
        self.verticalLayout_131.setSpacing(5)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Andmete_laadimine_Algandmete_laadimine = QTextEdit(self.f_HM_Andmete_laadimine_Algandmete_laadimine)
        self.te_HM_Andmete_laadimine_Algandmete_laadimine.setObjectName(u"te_HM_Andmete_laadimine_Algandmete_laadimine")
        self.te_HM_Andmete_laadimine_Algandmete_laadimine.setReadOnly(True)

        self.verticalLayout_131.addWidget(self.te_HM_Andmete_laadimine_Algandmete_laadimine)


        self.verticalLayout_132.addWidget(self.f_HM_Andmete_laadimine_Algandmete_laadimine)

        self.sw_HM_Andmete_laadimine.addWidget(self.w_HM_Andmete_laadimine_Algandmete_laadimine)
        self.w_HM_Andmete_laadimine_MaaAmetisse = QWidget()
        self.w_HM_Andmete_laadimine_MaaAmetisse.setObjectName(u"w_HM_Andmete_laadimine_MaaAmetisse")
        self.verticalLayout_134 = QVBoxLayout(self.w_HM_Andmete_laadimine_MaaAmetisse)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.f_HM_Andmete_laadimine_MaaAmetisse = QFrame(self.w_HM_Andmete_laadimine_MaaAmetisse)
        self.f_HM_Andmete_laadimine_MaaAmetisse.setObjectName(u"f_HM_Andmete_laadimine_MaaAmetisse")
        self.f_HM_Andmete_laadimine_MaaAmetisse.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Andmete_laadimine_MaaAmetisse.setFrameShadow(QFrame.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.f_HM_Andmete_laadimine_MaaAmetisse)
        self.verticalLayout_133.setSpacing(5)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Andmete_laadimine_MaaAmetisse = QTextEdit(self.f_HM_Andmete_laadimine_MaaAmetisse)
        self.te_HM_Andmete_laadimine_MaaAmetisse.setObjectName(u"te_HM_Andmete_laadimine_MaaAmetisse")
        self.te_HM_Andmete_laadimine_MaaAmetisse.setReadOnly(True)

        self.verticalLayout_133.addWidget(self.te_HM_Andmete_laadimine_MaaAmetisse)


        self.verticalLayout_134.addWidget(self.f_HM_Andmete_laadimine_MaaAmetisse)

        self.sw_HM_Andmete_laadimine.addWidget(self.w_HM_Andmete_laadimine_MaaAmetisse)

        self.verticalLayout_121.addWidget(self.sw_HM_Andmete_laadimine)


        self.verticalLayout_125.addWidget(self.f_HM_Andmete_laadimine_Pealkiri)

        self.f_HM_Andmete_laadimine_Sisu = QFrame(self.f_HM_Andmete_laadimine_Pea)
        self.f_HM_Andmete_laadimine_Sisu.setObjectName(u"f_HM_Andmete_laadimine_Sisu")
        self.f_HM_Andmete_laadimine_Sisu.setStyleSheet(u"")
        self.f_HM_Andmete_laadimine_Sisu.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Andmete_laadimine_Sisu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.f_HM_Andmete_laadimine_Sisu)
        self.verticalLayout_124.setSpacing(5)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(6, 5, 5, 5)

        self.verticalLayout_125.addWidget(self.f_HM_Andmete_laadimine_Sisu)


        self.verticalLayout_126.addWidget(self.f_HM_Andmete_laadimine_Pea)

        self.sw_HM.addWidget(self.w_HM_Andmete_laadimine)
        self.w_HM_Projektid = QWidget()
        self.w_HM_Projektid.setObjectName(u"w_HM_Projektid")
        self.verticalLayout_119 = QVBoxLayout(self.w_HM_Projektid)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.f_HM_Projektid_Pealkiri = QFrame(self.w_HM_Projektid)
        self.f_HM_Projektid_Pealkiri.setObjectName(u"f_HM_Projektid_Pealkiri")
        self.f_HM_Projektid_Pealkiri.setStyleSheet(u"")
        self.f_HM_Projektid_Pealkiri.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Projektid_Pealkiri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_118 = QVBoxLayout(self.f_HM_Projektid_Pealkiri)
        self.verticalLayout_118.setSpacing(5)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(6, 5, 5, 5)
        self.lb_HM_Projektid_Pealkiri = QLabel(self.f_HM_Projektid_Pealkiri)
        self.lb_HM_Projektid_Pealkiri.setObjectName(u"lb_HM_Projektid_Pealkiri")
        self.lb_HM_Projektid_Pealkiri.setFont(font13)

        self.verticalLayout_118.addWidget(self.lb_HM_Projektid_Pealkiri, 0, Qt.AlignTop)


        self.verticalLayout_119.addWidget(self.f_HM_Projektid_Pealkiri)

        self.f_HM_Projektid_Sisu = QFrame(self.w_HM_Projektid)
        self.f_HM_Projektid_Sisu.setObjectName(u"f_HM_Projektid_Sisu")
        self.f_HM_Projektid_Sisu.setStyleSheet(u"")
        self.f_HM_Projektid_Sisu.setFrameShape(QFrame.StyledPanel)
        self.f_HM_Projektid_Sisu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_129 = QVBoxLayout(self.f_HM_Projektid_Sisu)
        self.verticalLayout_129.setSpacing(5)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(6, 5, 5, 5)
        self.te_HM_Projektid_Sisu = QTextEdit(self.f_HM_Projektid_Sisu)
        self.te_HM_Projektid_Sisu.setObjectName(u"te_HM_Projektid_Sisu")
        self.te_HM_Projektid_Sisu.setStyleSheet(u"")
        self.te_HM_Projektid_Sisu.setReadOnly(True)

        self.verticalLayout_129.addWidget(self.te_HM_Projektid_Sisu)


        self.verticalLayout_119.addWidget(self.f_HM_Projektid_Sisu)

        self.sw_HM.addWidget(self.w_HM_Projektid)

        self.verticalLayout_19.addWidget(self.sw_HM)


        self.verticalLayout_18.addWidget(self.helpMenu)

        self.mbsc_Bottom = QFrame(self.rightMenuSubContainer)
        self.mbsc_Bottom.setObjectName(u"mbsc_Bottom")
        sizePolicy4.setHeightForWidth(self.mbsc_Bottom.sizePolicy().hasHeightForWidth())
        self.mbsc_Bottom.setSizePolicy(sizePolicy4)
        self.mbsc_Bottom.setMinimumSize(QSize(0, 40))
        self.mbsc_Bottom.setFrameShape(QFrame.StyledPanel)
        self.mbsc_Bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.mbsc_Bottom)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 10, 10)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_8)

        self.lbVersionNumber = QLabel(self.mbsc_Bottom)
        self.lbVersionNumber.setObjectName(u"lbVersionNumber")
        self.lbVersionNumber.setFont(font1)
        self.lbVersionNumber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_20.addWidget(self.lbVersionNumber)


        self.verticalLayout_18.addWidget(self.mbsc_Bottom)


        self.verticalLayout_17.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_6.addWidget(self.rightMenuContainer)


        self.retranslateUi(MailablDialogBase)

        self.swWorkSpace.setCurrentIndex(5)
        self.swCadastral_sub_processes.setCurrentIndex(0)
        self.tabWidget_Propertie_list.setCurrentIndex(0)
        self.tabW_Delete_list.setCurrentIndex(0)
        self.sw_HM.setCurrentIndex(8)
        self.sw_HM_Toimingud_kinnistutega.setCurrentIndex(0)
        self.sw_HM_Toimingud_kinnistutega_Laiendamine.setCurrentIndex(4)
        self.sw_HM_Toimingud_kinnistutega_Kitsendamine.setCurrentIndex(3)
        self.sw_HM_Andmete_laadimine.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MailablDialogBase)
    # setupUi

    def retranslateUi(self, MailablDialogBase):
        MailablDialogBase.setWindowTitle(QCoreApplication.translate("MailablDialogBase", u"Mailabl plugin", None))
        self.pbMainMenu.setText("")
        self.pbHome.setText(QCoreApplication.translate("MailablDialogBase", u"Avaleht", None))
        self.pbProjects.setText(QCoreApplication.translate("MailablDialogBase", u"Projektid", None))
        self.pbContracts.setText(QCoreApplication.translate("MailablDialogBase", u"Lepingud", None))
        self.pbPreContacts.setText(QCoreApplication.translate("MailablDialogBase", u"Liitumislepingud", None))
        self.pbMainContract.setText(QCoreApplication.translate("MailablDialogBase", u"Teenuslepingud", None))
        self.pbSubstitutes.setText(QCoreApplication.translate("MailablDialogBase", u"Servituudid", None))
        self.pbMapThemes.setText(QCoreApplication.translate("MailablDialogBase", u"Teemakaardid", None))
        self.pbAddDrawings.setText(QCoreApplication.translate("MailablDialogBase", u"Teostusjoonised", None))
#if QT_CONFIG(tooltip)
        self.pbSettings.setToolTip(QCoreApplication.translate("MailablDialogBase", u"S\u00e4tted", None))
#endif // QT_CONFIG(tooltip)
        self.pbSettings.setText(QCoreApplication.translate("MailablDialogBase", u"S\u00e4tted", None))
        self.pbUpdateData.setText(QCoreApplication.translate("MailablDialogBase", u"Andmete laadimine", None))
        self.pbSettings_AddShapeFile.setText(QCoreApplication.translate("MailablDialogBase", u"Lae algandmed", None))
        self.pbAvaMaaAmet.setText(QCoreApplication.translate("MailablDialogBase", u"Maa-ametisse", None))
        self.pbCadasters.setText(QCoreApplication.translate("MailablDialogBase", u"Toimingud kinnistutega", None))
        self.pbSyncMailabl.setText(QCoreApplication.translate("MailablDialogBase", u"Mailabliga s\u00fcnkroniseerimine", None))
        self.pbRefresh.setText(QCoreApplication.translate("MailablDialogBase", u"Andmete v\u00e4rskendamine", None))
        self.pbRemove.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnistute eemaldamine", None))
        self.pbExpand.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnistute lisamine", None))
        self.ServituuPageNameLabel.setText(QCoreApplication.translate("MailablDialogBase", u"Toimingud servituutidega", None))
        self.label_7.setText(QCoreApplication.translate("MailablDialogBase", u"V\u00e4rv 1: #1f232a ", None))
        self.label.setText(QCoreApplication.translate("MailablDialogBase", u"V\u00e4rv_u_1 #272c35", None))
        self.label_8.setText(QCoreApplication.translate("MailablDialogBase", u"V\u00e4rv 2: #2c313c", None))
        self.label_9.setText(QCoreApplication.translate("MailablDialogBase", u"V\u00e4rv 3: #343b47", None))
        self.label_4.setText(QCoreApplication.translate("MailablDialogBase", u"V\u00e4r_u_2  #404957", None))
        self.label_24.setText(QCoreApplication.translate("MailablDialogBase", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MailablDialogBase", u"V\u00e4rv 4: #838ea2", None))
        self.label_25.setText(QCoreApplication.translate("MailablDialogBase", u"FOOTER", None))
        self.CadastralMovesMainLabel.setText(QCoreApplication.translate("MailablDialogBase", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MailablDialogBase", u"Lisamiseks on valmis", None))
        self.lblCount.setText("")
        self.label_11.setText(QCoreApplication.translate("MailablDialogBase", u"kinnistut.", None))
        self.pbSearch_Add.setText(QCoreApplication.translate("MailablDialogBase", u"Otsi", None))
        self.pbCooseFromMap_Add.setText(QCoreApplication.translate("MailablDialogBase", u"Vali kaardilt", None))
        self.lblCounty.setText(QCoreApplication.translate("MailablDialogBase", u"Maakond", None))
        self.pbDone_County.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnita", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("MailablDialogBase", u"Valida saab \u00fche maakonna korraga", None))
        self.lblState.setText(QCoreApplication.translate("MailablDialogBase", u"Omavalitsus", None))
        self.pbDone_State.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnita", None))
        self.cbChooseAll_States.setText(QCoreApplication.translate("MailablDialogBase", u"Vali k\u00f5ik", None))
        self.lblCity.setText(QCoreApplication.translate("MailablDialogBase", u"Linn/K\u00fcla", None))
        self.pbDoneCity.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnita", None))
        self.cbChooseAll_Cities.setText(QCoreApplication.translate("MailablDialogBase", u"Vali k\u00f5ik", None))
        self.cbChooseAllAdd_properties.setText(QCoreApplication.translate("MailablDialogBase", u"Vali k\u00f5ik", None))
        self.cbOnPropertiesTab_Include_streets.setText(QCoreApplication.translate("MailablDialogBase", u"Kaasa Teed/t\u00e4navad", None))
        self.tabWidget_Propertie_list.setTabText(self.tabWidget_Propertie_list.indexOf(self.tabKinnistud), QCoreApplication.translate("MailablDialogBase", u"Kinnistud", None))
        self.cbChooseAllAdd__street_properties.setText(QCoreApplication.translate("MailablDialogBase", u"Vali k\u00f5ik", None))
        self.pbConfirm_streets_action.setText(QCoreApplication.translate("MailablDialogBase", u"Lisa transpordimaad", None))
        self.pbCancel_streets_reset.setText(QCoreApplication.translate("MailablDialogBase", u"T\u00fchista valik", None))
        self.tabWidget_Propertie_list.setTabText(self.tabWidget_Propertie_list.indexOf(self.tabTranspordimaad), QCoreApplication.translate("MailablDialogBase", u"Teed/t\u00e4navad", None))
        self.tabWidget_Propertie_list.setTabText(self.tabWidget_Propertie_list.indexOf(self.tab), QCoreApplication.translate("MailablDialogBase", u"Lisatavad kinnistud", None))
        self.pbConfirm_action.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnita", None))
        self.lblDel_Main_txt.setText(QCoreApplication.translate("MailablDialogBase", u"Eemaldamiseks on valmis", None))
        self.lblDel_Amount.setText("")
        self.lblDel_sub_txt.setText(QCoreApplication.translate("MailablDialogBase", u"kinnistut.", None))
        self.lblDel_County.setText(QCoreApplication.translate("MailablDialogBase", u"Maakond", None))
        self.pbDel_County.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnita", None))
#if QT_CONFIG(tooltip)
        self.lblDel_Count_comment.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lblDel_Count_comment.setText(QCoreApplication.translate("MailablDialogBase", u"Valida saab \u00fche maakonna korraga", None))
        self.lblDel_State.setText(QCoreApplication.translate("MailablDialogBase", u"Omavalitsus", None))
        self.pbDel_State.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnita", None))
        self.cbDel_ChooseAll_States.setText(QCoreApplication.translate("MailablDialogBase", u"Vali k\u00f5ik", None))
        self.lblDel_City.setText(QCoreApplication.translate("MailablDialogBase", u"Linn/K\u00fcla", None))
        self.pbDel_City.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnita", None))
        self.cbDel_ChooseAll_Cities.setText(QCoreApplication.translate("MailablDialogBase", u"Vali k\u00f5ik", None))
        self.cbDel_ChooseAll_Data_properties.setText(QCoreApplication.translate("MailablDialogBase", u"Vali k\u00f5ik", None))
        self.cbDel_ChooseAll_Data_include_Allroads.setText(QCoreApplication.translate("MailablDialogBase", u"Kaasa Teed/t\u00e4navad", None))
        self.pbDel_PreConfirm.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnita", None))
        self.tabW_Delete_list.setTabText(self.tabW_Delete_list.indexOf(self.tabDel_data_properties), QCoreApplication.translate("MailablDialogBase", u"Kinnistud", None))
        self.cbDel_ChooseAll_Data_transport.setText(QCoreApplication.translate("MailablDialogBase", u"Vali k\u00f5ik", None))
        self.tabW_Delete_list.setTabText(self.tabW_Delete_list.indexOf(self.tabDel_data_tranposrt), QCoreApplication.translate("MailablDialogBase", u"Teed/t\u00e4navad", None))
        self.tabW_Delete_list.setTabText(self.tabW_Delete_list.indexOf(self.tab_2), QCoreApplication.translate("MailablDialogBase", u"Page", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; text-decoration: underline;\">Aluskaart koostatakse Mailablis olevate kinnistute andmebaasi p\u00f5hjal.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\""
                        ">Mailablisse esitatakse p\u00e4ring andmete kohta. Kinnistud leitakse katastri\u00fcksus SHP_KATASTRIYKSUS kihilt ja imporditakse uuele loodavale kinnistute aluskaardi kihile, mida kasutaja saab kasutada aluskaardina oma toimingutes.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">NB! \u00c4ra kasuta QGIS enne aluskihi l\u00f5plikku moodustumist ning programmi taask\u00e4ivitamist!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p></body></html>", None))
        self.LblSync_NamOfFutureLayer.setText(QCoreApplication.translate("MailablDialogBase", u"Kihi nimetus:", None))
        self.leText_For_Sync_GreateLayerName.setInputMask("")
        self.leText_For_Sync_GreateLayerName.setText("")
        self.leText_For_Sync_GreateLayerName.setPlaceholderText(QCoreApplication.translate("MailablDialogBase", u"3-25 t\u00e4hem\u00e4rki", None))
        self.pbSync_start_sync.setText(QCoreApplication.translate("MailablDialogBase", u"Alusta", None))
        self.lblSync_General_aditional.setText(QCoreApplication.translate("MailablDialogBase", u"aaa", None))
        self.lblSync_General.setText(QCoreApplication.translate("MailablDialogBase", u"TextLabel", None))
        self.lblFor_pBar_Sync_County.setText(QCoreApplication.translate("MailablDialogBase", u"TextLabel", None))
        self.lblFor_pBar_State_list.setText(QCoreApplication.translate("MailablDialogBase", u"TextLabel", None))
        self.lblFor_pBar_City_list.setText(QCoreApplication.translate("MailablDialogBase", u"TextLabel", None))
        self.lblFor_pBar_CityItems.setText(QCoreApplication.translate("MailablDialogBase", u"TextLabel", None))
        self.lblSync_County.setText(QCoreApplication.translate("MailablDialogBase", u"Maakond", None))
        self.lblSync_State.setText(QCoreApplication.translate("MailablDialogBase", u"Omavalitsus", None))
        self.lblSync_City.setText(QCoreApplication.translate("MailablDialogBase", u"Linn/K\u00fcla", None))
        self.pbSync_Cancel.setText(QCoreApplication.translate("MailablDialogBase", u"T\u00fchista toiming", None))
        self.Loomisel_label.setText(QCoreApplication.translate("MailablDialogBase", u"See lehek\u00fclg on alles loomisel", None))
        self.Loomisel_label_2.setText(QCoreApplication.translate("MailablDialogBase", u"See lehek\u00fclg on alles loomisel", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Katastri andmed on oluline osa &quot;Mailabl plugina&quot; korralikust toimimisest.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  	</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">QGIS-is saad kihi aluskaardi omadusi muuta kasutades kihi &quot;Propreties&quot; v\u00f5i &quot;Omadused&quot; ja Alamsektsiooni &quot;Feature S\u00fcmbology&quot;.<span style=\" font-size:8pt;\">  </span></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />Laadides aluskaardi Mailabli mooduli kaudu oleme teinud juba selles osas ise valiku, millise kujundusega aluskiht v\u00f5iks sulle ideaalselt sobida. Soovikorral saad seda ise alati muuta</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kui aluskaart on alla laetud saad teha j\u00e4rgnevaid toiminguid:<br />Olles mailabli Esmakasutaja saad luua endale nii aluskaardi kui lisada kinnistud koheselt ka Mailablisse.<br />Kui aluskaardiga on midagi juhtund saad alati Mailabli kinnistud uuesti s\u00fcnkroonida. Selleks kasuta &quot;S\u00fcnkrooni kinnistud&quot; valikut!</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> Veel m\u00f5tteid:<br /></span><span style=\" font-size:10pt;\">Milliseid toiminguid kinnistutega teha saab?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1. Kinnistute lisamine andmebaasidesse</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">	a. Mailablist</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">	b.Qgisist</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br />2. Olemasolevate kinnistute uuendamine</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">3.Kinnistute eemaldamine andmebaasidest:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">	a. Mailablist</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">	b.Qgisist</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MailablDialogBase", u"Toimingud Lepingutega ", None))
        self.pbContracts_Connect_properties.setText(QCoreApplication.translate("MailablDialogBase", u"Seosta leping kinnistuga", None))
        self.pbRefresh_tblMailabl_contracts.setText("")
        self.label_5.setText(QCoreApplication.translate("MailablDialogBase", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MailablDialogBase", u"Lepinguid kokku: xxx", None))
        self.label_3.setText(QCoreApplication.translate("MailablDialogBase", u"Kehtivad: xxx", None))
        self.label_20.setText(QCoreApplication.translate("MailablDialogBase", u"Help", None))
        self.textEdit.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Aluskihi struktuur peab vastama Maa-ameti katastri struktuurile.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-"
                        "block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Maa-ametist laaditakse pluginasse SHP-fail.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Katastri andmete uuendamise protsessi abil saab plugin v\u00e4rskendada olemasolevat katastriinformatsiooni - v\u00f5imaldab sisestada uusi katastreid, muuta olemasolevaid andmeid v\u00f5i kustutada/arhiveerida vanu andmeid vastavalt vajadusele.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"
                        "\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Selleks, et plugin saaks t\u00f6\u00f6tada, tuleb alguses importida Maa-ameti SHP-fail.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MailablDialogBase", u"FOOTER", None))
        self.label_15.setText(QCoreApplication.translate("MailablDialogBase", u"S\u00e4tted", None))
        self.lblHEadingUserData.setText(QCoreApplication.translate("MailablDialogBase", u"Kasutaja s\u00e4tted", None))
        self.pbUserSettings.setText("")
        self.lbNUserPreferences.setText(QCoreApplication.translate("MailablDialogBase", u"Eelistused:", None))
        self.lblPreferences.setText(QCoreApplication.translate("MailablDialogBase", u"Siia loome eelistuste seadistuse. Tausta v\u00e4rv jms", None))
        self.lblUserFirstName.setText(QCoreApplication.translate("MailablDialogBase", u"Kasutaja:", None))
        self.lblNUserSurename.setText(QCoreApplication.translate("MailablDialogBase", u"Perekonnanimi", None))
        self.lbNuserName.setText(QCoreApplication.translate("MailablDialogBase", u"Eesnimi", None))
        self.lbNUserRoles.setText(QCoreApplication.translate("MailablDialogBase", u"Mailabli rollid:", None))
        self.lblUserRoles.setText(QCoreApplication.translate("MailablDialogBase", u"rollid", None))
        self.label_27.setText(QCoreApplication.translate("MailablDialogBase", u"Minu eelistatud avaleht:", None))
        self.label_28.setText(QCoreApplication.translate("MailablDialogBase", u"Tulekul", None))
        self.label_30.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnistu andmete seadistus", None))
        self.pbLayerSettings.setText("")
        self.label_16.setText(QCoreApplication.translate("MailablDialogBase", u"Andmekiht, millelt imporditakse uued andmed:", None))
        self.lblSHPNewItems.setText("")
        self.label_6.setText(QCoreApplication.translate("MailablDialogBase", u"Olemasolevate katastriandmete kiht:", None))
        self.lblcurrent_main_layer_label.setText("")
        self.label_2.setText(QCoreApplication.translate("MailablDialogBase", u"Kiht, kuhu salvestatakse uued katastriandmed:", None))
        self.lblnewCadastrals_input_layer_label.setText("")
        self.label_31.setText(QCoreApplication.translate("MailablDialogBase", u"Projektid s\u00e4tted", None))
        self.pbSettings_Setup_Projects.setText("")
        self.label_22.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnistutega seotud projekti kiht", None))
        self.lblLayerProjects_Properties.setText("")
        self.label_14.setText(QCoreApplication.translate("MailablDialogBase", u"Projektide vektor kaardikiht", None))
        self.lblLayerProjects_Vector.setText("")
        self.label_10.setText(QCoreApplication.translate("MailablDialogBase", u"Avaleht logoga", None))
        self.teWelcomeContent.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Mis on Mailabl GIS plugin?</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Plugin, mis integreerib Mailabli t\u00f6\u00f6keskkonna geoinfos\u00fcs"
                        "teemi keskkonnaga ning muudab ettev\u00f5tte t\u00f6\u00f6lauad \u00fclevaatlikuks ja informatiivseks tervikpildiks.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Kinnistute andmete uuendamise protsessi abil v\u00e4rskendab plugin olemasolevat katastriinformatsiooni - v\u00f5imaldab sisestada uusi katastreid, muuta olemasolevaid andmeid v\u00f5i kustutada/arhiveerida vanu andmeid vastavalt vajadusele.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Kuidas toimub andmete integreerimine?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Integreerimiseks pakume kahte lahendust:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u00dchendus luuakse API liidese kaudu ning andmete lugemine ning t\u00f6\u00f6tlemine toimub meie teenusepakkuja juures kasutaja arvuti ressursse kasutades (<span style=\" font-style:italic;\">standard lahendus</spa"
                        "n>).</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kombineeritud variant - \u00fchendus luuakse samuti API liidese kaudu, aga andmete lugemine ning t\u00f6\u00f6tlemine toimub ettev\u00f5tte enda serverite teenusepakkujate peal (<span style=\" font-style:italic;\">t\u00e4psustamiseks p\u00f6\u00f6rdu arendaja poole</span>).</li></ol>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Kombineeritud variant majasiseste v\u00f5imalustega annab ettev\u00f5ttele suurema vabaduse ja kiiruse teemakaartide \u00fchenduse haldamiseks.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Soovitame eelistada kombineeritud varianti.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Oluline on, et ettev\u00f5tte kinnistute aluskaart oleks loodud Maa-ameti struktuuri alusel l\u00e4bi Mailabli pulgina. Selliselt tagatakse toimiv andme\u00fchendus k\u00f5ikides moodulites. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">NB! J\u00e4lgi infoaknaid, mis annavad info vajalike tegevuste kohta v\u00f5i on hoiatava informatsiooniga. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"><br /></span><span style=\" font-size:12pt; text-decoration: underline;\">NB! Tegemist on Mailabli beeta versiooniga, mis ei ole l\u00f5plik toode ja mille arendus s\u00f5ltub olulisel m\u00e4\u00e4ral kasutajate tagasisidest!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.leUC_Heading.setText(QCoreApplication.translate("MailablDialogBase", u"Logi sisse Mailabli kontoga", None))
        self.leUsername.setText("")
        self.leUsername.setPlaceholderText(QCoreApplication.translate("MailablDialogBase", u"Kasutajanimi", None))
        self.lePassword.setText("")
        self.lePassword.setPlaceholderText(QCoreApplication.translate("MailablDialogBase", u"Salas\u00f5na", None))
        self.pbUC_Save.setText(QCoreApplication.translate("MailablDialogBase", u"Logi sisse", None))
        self.pbUC_Cancel.setText(QCoreApplication.translate("MailablDialogBase", u"Katkesta", None))
        self.lblLoadVersion.setText("")
        self.lbl_heading_Projects.setText(QCoreApplication.translate("MailablDialogBase", u"Projektid", None))
#if QT_CONFIG(tooltip)
        self.pbProjects_Connect_properties.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pbProjects_Connect_properties.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pbProjects_Connect_properties.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pbProjects_Connect_properties.setText(QCoreApplication.translate("MailablDialogBase", u"Kinnistutega sidumine", None))
        self.cmbProjectState.setItemText(0, QCoreApplication.translate("MailablDialogBase", u"Avatud", None))
        self.cmbProjectState.setItemText(1, QCoreApplication.translate("MailablDialogBase", u"K\u00f5ik", None))
        self.cmbProjectState.setItemText(2, QCoreApplication.translate("MailablDialogBase", u"Suletud", None))
        self.cmbProjectState.setItemText(3, "")
        self.cmbProjectState.setItemText(4, "")
        self.cmbProjectState.setItemText(5, "")

        self.pbRefresh_tblMailabl_projects.setText("")
        self.pushButton.setText(QCoreApplication.translate("MailablDialogBase", u"N\u00e4htava ala projektide laadimine", None))
        self.le_searchProjects.setPlaceholderText(QCoreApplication.translate("MailablDialogBase", u"Otsing", None))
        self.label_32.setText(QCoreApplication.translate("MailablDialogBase", u"Uus nimetus", None))
        self.label_26.setText(QCoreApplication.translate("MailablDialogBase", u"Projekti ID", None))
        self.pbShowOnMap.setText(QCoreApplication.translate("MailablDialogBase", u"N\u00e4ita kaardil", None))
        self.ProgresBar_general.setFormat("")
        self.pbMailabl.setText(QCoreApplication.translate("MailablDialogBase", u" Mailabl.com", None))
        self.helpMenuToggle.setText("")
        self.lb_HM_Avaleht_Pealkiri.setText("")
        self.te_HM_Avaleht_Sisu.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.lb_HM_LepingudPealkiri.setText(QCoreApplication.translate("MailablDialogBase", u"Lepingud", None))
        self.lb_HM_Teostusjoonised_Pealkiri.setText(QCoreApplication.translate("MailablDialogBase", u"Teostusjoonised", None))
        self.lb_f_HM_Toimingud_kinnistutega_Pealkiri.setText(QCoreApplication.translate("MailablDialogBase", u"Toimingud kinnistutega", None))
        self.lb_HM_Toimingud_kinnistutega_Laiendamine_Pealkiri.setText(QCoreApplication.translate("MailablDialogBase", u"Laiendamine", None))
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Yldine.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Siia \u00fcldine jutt laiendamise kohta.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Mida \u00fcldse laiendamisega teha saab?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Piirkonna laiendamine?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Kinnistute lisamine ja eemaldamine?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Kaks varianti. Valik:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1. Tabelist</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2. Vali ala v\u00f5"
                        "i kinnistud kaardilt</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">J\u00e4tkamiseks vali m\u00f5ni maakond maakonna loetelust.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Maakond.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Maakond</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1. Vali maakond (valida saab \u00fche maakonna korraga).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; marg"
                        "in-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; text-decoration: underline;\">NB! Peale maakonna valiku tegemist n\u00e4ed valitud maakonna kinnistuid ka aluskaardil. Saad kinnistuid valida ka kaardil (nupp &quot;Vali kaardilt&quot;).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ff0000;\">V\u00f5i ...Maakonna tasandil olles kinnistuid kaardil veel valda ei saa!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2. Kinnita maakond (</span><span style=\" font-size:9pt; font-weight:600;\">&quot;Kinnita&quot;</span><span style=\" font-size:9pt;\"> nupp&quot;)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">3. Oota omavali"
                        "tsuste nimekirja laadimist.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.te_Laiente_HM_Toimingud_kinnistutega_Laiendamine_Omavalitsus.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Omavalitsus</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1. Vali valitud maakonna omavalitsuste nimekirjast soovitud omavalitsus. V\u00f5imalus on valida \u00fcks, mitu v\u00f5i k\u00f5ik omava"
                        "litsused (viimasel </span><span style=\" font-size:9pt; font-weight:600;\">&quot;Vali k\u00f5ik&quot;</span><span style=\" font-size:9pt;\"> nupp).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2. Kinnita valik nupuga &quot;Kinnita&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">NB! Peale valiku kinnitamist n\u00e4ed valitud omavalitsuse piire ka aluskaardil ja saad kinnistu v\u00f5i kinnistute valikuid seal teha (nupp &"
                        "quot;Vali kaardilt&quot;). Kaardil valituid kinnistuid n\u00e4ed plugina akna alumises tabelis. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; color:#ff0000;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.te_HM_Toimingud_kinnistutega_Laiendamine_Linn_Kyla.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Linn/K\u00fcla</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Kui j\u00e4tkad tabelis kinnistute valimist, siis:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:"
                        "0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1. tee linna v\u00f5i k\u00fcla valik. J\u00e4lle, on v\u00f5imalus valida \u00fcks, mitu v\u00f5i k\u00f5ik valitud omavalitsuse k\u00fclad v\u00f5i linnad (viimasel </span><span style=\" font-size:9pt; font-weight:600;\">&quot;Vali k\u00f5ik&quot;</span><span style=\" font-size:9pt;\"> nupp).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2. kinnita valik edasi suunava nupuga.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">3. oota kuni kinnistud on laetud ja n\u00e4htavad plugina akna alumises tabelis</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Jne</span></p></body></html>", None))
        self.te_HM_Toimingud_kinnistutega_Laiendamine_LaetudKinnistud.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Laetud kinnistute tabel</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Mida n\u00e4ed?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Jagunemine:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1. Kinnistud</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2. Teed/T\u00e4navad</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Mis teha saad?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:"
                        "0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Jne</span></p></body></html>", None))
        self.lb_HM_Toimingud_kinnistutega_Kitsendamine_Pealkiri.setText(QCoreApplication.translate("MailablDialogBase", u"Kitsendamine", None))
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Yldine.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Siia \u00fcldine jutt kitsendamise kohta.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Miks \u00fcldse ja mida kitsendamisega teha saab?</span></p></body></html>", None))
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Maakond.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Maakond</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Kirjuta sisu</span></p></body></html>", None))
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Omavalitsus.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Omavalitsus</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Kirjuta sisu</span></p></body></html>", None))
        self.te_HM_Toimingud_kinnistutega_Kitsendamine_Linn_Kyla.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Linn/K\u00fcla</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Kirjuta sisu</span></p></body></html>", None))
        self.lb_HM_Toimingud_kinnistutega_Yldine_kirjeldus.setText(QCoreApplication.translate("MailablDialogBase", u"\u00dcldine kirjeldus", None))
        self.te_HM_Toimingud_kinnistutega_Yldine_kirjeldus.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Milliseid toiminguid kinnistutega teha saab?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1. Kinnistute lisamine andmebaasidesse</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\"><span style=\" font-size:9pt;\">	a. Mailablist</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">	b.Qgisist</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br />2. Olemasolevate kinnistute uuendamine</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">3.Kinnistute eemaldamine andmebaasidest:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">	a. Mailabl"
                        "ist</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">	b.Qgisist</span></p></body></html>", None))
        self.lb_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Pealkiri.setText(QCoreApplication.translate("MailablDialogBase", u"Aluskaardi koostamine", None))
        self.te_HM_Toimingud_kinnistutega_Aluskaardi_koostamine_Sisu.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Selle toiminguga saab luua oma GIS projekti ja Mailablis olevate kinnistutega s\u00fcnkroonis aluskaardi.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Toiming on vajalik kui:</span></p>\n"
"<p style=\" margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1. kinnistute kiht on  &quot;katki l\u00e4inud&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2. Mailabli on kinnistud imporditud enne, kui QGIS kasutusele v\u00f5etakse </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">NB! Tegemist v\u00f5ib olla pikaajalise protsessiga, mis h\u00f5ivab arvuti ressursid ning t\u00f6\u00f6 on hea planeerida t\u00f6\u00f6v\u00e4lisele ajale!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; text-decoration: underline;\">Kiht luuakse esialgu </span><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">GeoPackage (.gpkg) vormingus.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">GeoPackage vorming on \u00fcks viis geograafiliste andmete salvestamiseks ja jagamiseks, ning see pakub \u00fchtset failiformaati erinevate geoinfos\u00fcsteemide ja rakenduste jaoks.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Loodavale kihile tuleb esmalt anda nimi. Nimi peab olema vahemikus 3-25 t\u00e4hem\u00e4rki. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Peale korrektse nime lisamist, kl\u00f5psa &quot;Alusta&quot; nupul. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">NB! \u00c4ra alusta tegevustega enne aluskihi l\u00f5plikku moodustumist!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin"
                        "-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Uus aluskaardi kiht lisatakse automaatselt Mailabl settings/Uued kinnistud ja uus kiht.</span></p></body></html>", None))
        self.lb_HM_Satted_Pealkiri.setText(QCoreApplication.translate("MailablDialogBase", u"S\u00e4tted", None))
        self.te_HM_Satted_Sisu.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">S\u00e4tete muutmine ja info valitud s\u00e4tete kohta</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Siin n\u00e4ed:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0"
                        "px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1. Kasutaja s\u00e4tteid</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2. Kinnistute andmete seadistust</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">3. Projektide s\u00e4tteid</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\""
                        ">Seadistuste muutmine:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Siiia t\u00e4psemalt, milda saab muuta kasutaja ja mida administraartor</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">NB! Peale muudatuste salvestamist peab plugina taask\u00e4ivitam"
                        "a.</span></p></body></html>", None))
        self.lb_HM_Servituudid_Pealkiri.setText(QCoreApplication.translate("MailablDialogBase", u"Servituudid", None))
        self.lb_HM_Teemakaardid_Pealkiri.setText(QCoreApplication.translate("MailablDialogBase", u"Teemakaardid", None))
        self.lb_HM_Andmete_laadimine_Pealkiri.setText(QCoreApplication.translate("MailablDialogBase", u"Andmete laadimine", None))
        self.lbl_HM_Andmete_Laadimine_Yldine.setText(QCoreApplication.translate("MailablDialogBase", u"Andmete Laadimine \u00fcldiselt", None))
        self.te_HM_Andmete_laadimine_Yldine.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Sissejuhatus </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.te_HM_Andmete_laadimine_Algandmete_laadimine.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Algandmete laadimine</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Maa-ametist laaditakse pluginasse SHP-fail.</span></p></body></html>", None))
        self.te_HM_Andmete_laadimine_MaaAmetisse.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Maa-ametist laadimine</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Siia jutt, kuidas andmeid Maa-ametist laadida.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.lb_HM_Projektid_Pealkiri.setText(QCoreApplication.translate("MailablDialogBase", u"Projektid", None))
        self.te_HM_Projektid_Sisu.setHtml(QCoreApplication.translate("MailablDialogBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Laetud on aktiivse staatusega  projektid, mis on peaprojektid ja mis pole privaatsed.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Tulpades on sortimise v\u00f5imalus.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Tabelis vastavale ikoonile vajutades saab:</span></p>\n"
"<p style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1. aluskaardil n\u00e4ha projektiga seotud kinnistuid</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2. liikuda projektile Malilablis</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">3. avada projektiga seotud faile ja kaustasid</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Projekti number, mille projekt on Mailablis loomise hetkel automaatsel"
                        "t saanud</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.lbVersionNumber.setText(QCoreApplication.translate("MailablDialogBase", u"v.31.01.24", None))
    # retranslateUi

