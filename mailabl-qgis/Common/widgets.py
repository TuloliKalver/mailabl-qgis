# widget_specs.py
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableView

class Frames:
    FRAME_4 = (QtWidgets.QFrame, 'frame_4')
    FRAME_5 = (QtWidgets.QFrame, 'frame_5')
    FRAME_2 = (QtWidgets.QFrame, 'frame_2')
    FR_LABEL = (QtWidgets.QFrame, 'frLabel')

    FR_CONTROLL_BUTTONS = (QtWidgets.QFrame, 'frControllButtons')
    FRAME_SELECTOR_MAINFRAME = (QtWidgets.QFrame, 'Frame_Selector_MainFrame')
    FR_COUNTY = (QtWidgets.QFrame, 'FRCounty')
    FRAME_TOOLS_COUNTY = (QtWidgets.QFrame, 'Frame_Tools_County')
    FRAME_7 = (QtWidgets.QFrame, 'frame_7')
    FR_STATE = (QtWidgets.QFrame, 'FrState')
    FRAME_8 = (QtWidgets.QFrame, 'frame_8')
    FRAME_11 = (QtWidgets.QFrame, 'frame_11')
    FRAME_6 = (QtWidgets.QFrame, 'frame_6')
    FR_MUNICIPALITY = (QtWidgets.QFrame, 'FrMunicipality')
    FRAME_TOOLS_CITY = (QtWidgets.QFrame, 'Frame_Tools_City')
    FRAME = (QtWidgets.QFrame, 'frame')
    FRAME_3 = (QtWidgets.QFrame, 'frame_3')
    FR_RESULT_VIEWER = (QtWidgets.QFrame, 'frResultViewer')
    FRAME_17 = (QtWidgets.QFrame, 'frame_17')
    FRAME_12 = (QtWidgets.QFrame, 'frame_12')

class Buttons:
    BTN_MAP_ACTIONS = (QtWidgets.QPushButton, 'btnMapActions')
    BTN_ADD_ELEMENTS = (QtWidgets.QPushButton, 'btnAddElements')
    BTN_REMOVE_ITEMS = (QtWidgets.QPushButton, 'btnRemoveItems')
    BTN_UPDATE_DATA = (QtWidgets.QPushButton, 'btnUpdateData')
    BTN_CONFIRM_ACTION = (QtWidgets.QPushButton, 'btnConfirmAction')
    BTN_CANCEL_ACTION = (QtWidgets.QPushButton, 'btnCancelAction')

class Labels:
    LBL_ACTION_NAME = (QtWidgets.QLabel, 'lblActionName')
    LBL_COUNTY = (QtWidgets.QLabel, 'lblCounty')
    LBL_STATE = (QtWidgets.QLabel, 'lblState')
    LBL_CITY = (QtWidgets.QLabel, 'lblCity')

class ListWidgets:
    LV_COUNTY = (QtWidgets.QListWidget, 'lvCounty')
    LV_STATE = (QtWidgets.QListWidget, 'lvState')
    LV_SETTLEMENT = (QtWidgets.QListWidget, 'lvSettlement')

class Widgets:
    PROGRESS_BAR = (QtWidgets.QProgressBar, 'progressBar')
    QT_SCROLLAREA_VIEWPORT = (QtWidgets.QWidget, 'qt_scrollarea_viewport')
    QT_SCROLLAREA_HCONTAINER = (QtWidgets.QWidget, 'qt_scrollarea_hcontainer')
    QT_SCROLLAREA_VCONTAINER = (QtWidgets.QWidget, 'qt_scrollarea_vcontainer')

class CheckBoxes:
    CHK_SELECT_ALL_SETTLEMENTS = (QtWidgets.QCheckBox, 'chkSelectAllSettlements')
    CHK_TOGGLE_ROAD_SELECTION = (QtWidgets.QCheckBox, 'chkToggleRoadSelection')

class TableViews:
    TV_SELECTED_MAP_ITEMS = (QTableView, 'tvSelectedMapItems')
    TABLE_VIEW = (QTableView, 'tableView')

# This will unpack the tuple (widget type, object name) into findChild.
#my_frame = self.findChild(*Frames.FRAME_4)