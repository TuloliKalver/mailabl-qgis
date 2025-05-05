
from ..config.iconHandler import iconHandler
from PyQt5.QtWidgets import QMenu, QAction, QTableView
from PyQt5.QtCore import Qt, QPoint, QSize
from ..Functions.AsBuilt.AsBuiltTools import AsBuiltTools
from ..Functions.AsBuilt.AsBuiltHelpers import AsBuiltHelpers
from ..KeelelisedMuutujad.TableHeaders import HeaderKeys, TableHeaders_new
from ..widgets.decisionUIs.DecisionMaker import DecisionDialogHelper
from ..app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ..KeelelisedMuutujad.messages import Headings, HoiatusTexts


class RightClickHelper:
    dialog = None  # Class variable

    def __init__(self, main):
        RightClickHelper.dialog = main  # Assign correctly

    @classmethod
    def ASBuilt_right_click_action(cls):
        if cls.dialog is None:
            print("❌ RightClickHelper.dialog is not set.")
            return

        cls.dialog.tblAsBuilt.setContextMenuPolicy(Qt.CustomContextMenu)
        cls.dialog.tblAsBuilt.customContextMenuRequested.connect(cls.AsBuilt_table_right_click_menu)

    @classmethod
    def AsBuilt_table_right_click_menu(cls, pos: QPoint):
        from PyQt5.QtGui import QIcon
        table = cls.dialog.tblAsBuilt
        index = table.indexAt(pos)
        if not index.isValid():
            return

        row = index.row()

        menu = QMenu(table)

        icon = iconHandler.set_no_file_icon()
        icon_edit = iconHandler.edit_data()

        action_hello = QAction(QIcon(icon), "Lisa fail", table)
        helper = RightClickHelper(cls.dialog)
        action_hello.triggered.connect(lambda: helper._handle_file_add(table,row))
        


        asBuiltTools = AsBuiltTools(cls.dialog, table)
        action_try_better = QAction(QIcon(icon_edit), "Halda märkusi", table)
        action_try_better.triggered.connect(lambda:asBuiltTools.load_asBuiltTools())

        menu.addAction(action_hello)
        menu.addAction(action_try_better)

        menu.exec_(table.viewport().mapToGlobal(pos))


    def _handle_file_add(self,table:QTableView, row) -> bool:
        language = "et"
        model = table.model()
       



        property_id = model.data(model.index(row,0), Qt.DisplayRole)
        
        buttons={"keep": "Ei ole vaja", "delete": "Jah"}
        ret = DecisionDialogHelper.ask_user(
            title=Headings.inFO_SIMPLE,
            message="Kas loon kohe ka Konttrolli tabeli?",
            options=buttons,
            parent=self,
            type= AnimatedGradientBorderFrame.PROLOOK
                )


        AsBuiltHelpers._handle_drawTool(notes_table=ret)
        prepared_text = AsBuiltHelpers.html
        #print(f"Textbrowser content: {prepared_text}")
        # 2. Fetch descriptions from Mailabl (already done)
        from ..Functions.AsBuilt.ASBuilt import AsBuiltQueries
        existing_descriptions = AsBuiltQueries._query_AsBuilt_by_id(property_id=property_id)
        #print(f"Existing descriptions: {existing_descriptions}")
        # 3. Merge: put file table first, then append all descriptions
        combined_html = AsBuiltHelpers.merge_file_table_with_existing(prepared_text, existing_descriptions)

        res = AsBuiltQueries._update_AsBuilt_by_id(property_id=property_id, description=combined_html)
    
        if res:
            from ..app.workspace_handler import WorkSpaceHandler
            WorkSpaceHandler.asBuilt_reload(None)
        
        AsBuiltHelpers.html = ""
