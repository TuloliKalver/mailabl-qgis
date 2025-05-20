from PyQt5.QtWidgets import QApplication
from ..config.iconHandler import iconHandler
from PyQt5.QtWidgets import QMenu, QAction, QTableView
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon
from ..Functions.AsBuilt.AsBuiltTools import AsBuiltTools
from ..Functions.AsBuilt.AsBuiltHelpers import AsBuiltHelpers, NotesTableGenerator
from ..Functions.WORKS.works import WorkMapHelper

from ..widgets.decisionUIs.DecisionMaker import DecisionDialogHelper
from ..app.Animations.AnimatedGradientBorderFrame import AnimatedGradientBorderFrame
from ..KeelelisedMuutujad.messages import Headings
from ..widgets.properties_connector_UIcontroller import PropertiesConnectorUIController
from ..KeelelisedMuutujad.modules import Module


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
        table = cls.dialog.tblAsBuilt
        print(f" click on position: {pos}")
        if QApplication.mouseButtons() != Qt.RightButton:
            print("a right-click.")
            
            
            index = table.indexAt(pos)
            
            col = index.column()
            if col in [0, 1, 5, 7, 8, 9, 10, 11, 12, 13]:  # ⛔ Block right-click on columns 0 and 1
                return

            #[0 'id', 1 'flag', 2'type', 3'name', 4'tähtaeg', 5'color', 6'responsible', 7'property_number', 
            # 8 'properties_icon', 
            # 9'parent_id', 10 'web_link_button', 11'documents', 12'file_path',13 'statuses']
            
            if not index.isValid():
                return

            row = index.row()

            menu = QMenu(table)

            icon = iconHandler.add_more_files()
            icon_edit = iconHandler.edit_data()
            pin_add = iconHandler.pin_add()

            actio_add_files = QAction(QIcon(icon), "Lisa faile", table)
            helper = RightClickHelper(cls.dialog)
            actio_add_files.triggered.connect(lambda: helper._handle_file_add(table, row))
            

            asBuiltTools = AsBuiltTools(cls.dialog, table)
            action_edit_notes = QAction(QIcon(icon_edit), "Halda märkusi", table)
            action_edit_notes.triggered.connect(lambda:asBuiltTools.load_asBuiltTools())


            button_asBuilt = cls.dialog.pbTeostusConnectproperties
            action_add_properties = QAction(QIcon(pin_add), "Seosta kinnistuid", table)
            
            action_add_properties.triggered.connect(
                lambda: PropertiesConnectorUIController.load_properties_connector(
                    cls.dialog, Module.ASBUILT, table, button_asBuilt
                )
            )


            menu.addAction(actio_add_files)
            menu.addAction(action_edit_notes)
            menu.addAction(action_add_properties)

            menu.exec_(table.viewport().mapToGlobal(pos))
        else:
            print("not a right-click.")
            return



    @classmethod
    def WORKS_right_click_action(cls):
        if cls.dialog is None:
            print("❌ RightClickHelper.dialog is not set.")
            return

        cls.dialog.tblWorks.setContextMenuPolicy(Qt.CustomContextMenu)
        cls.dialog.tblWorks.customContextMenuRequested.connect(cls.WORKS_table_right_click_menu)

    @classmethod
    def WORKS_table_right_click_menu(cls, pos: QPoint):
        table = cls.dialog.tblWorks
        #print(f" click on position: {pos}")
        if QApplication.mouseButtons() != Qt.RightButton:
            #print("a right-click.")
            
            
            index = table.indexAt(pos)
            
            col = index.column()
            if col in [0, 1, 5, 7, 8, 9, 10, 11, 12, 13]:  # ⛔ Block right-click on columns 0 and 1
                return

            #[0 'id', 1 'flag', 2'type', 3'name', 4'tähtaeg', 5'color', 6'responsible', 7'property_number', 
            # 8 'properties_icon', 
            # 9'parent_id', 10 'web_link_button', 11'documents', 12'file_path',13 'statuses']
            
            if not index.isValid():
                return

            row = index.row()
            id_index = index.sibling(row, 0)  # Assuming column 0 is 'id'
            task_id = id_index.data()


            menu = QMenu(table)

            pin_add = iconHandler.pin_add()

            action_reposition = QAction(QIcon(pin_add), "Paiguta töö ringi", table)
            
            action_reposition.triggered.connect(
                lambda: WorkMapHelper.begin_reposition_work_feature(task_id)
            )


            menu.addAction(action_reposition)

            menu.exec_(table.viewport().mapToGlobal(pos))
        else:
            print("not a right-click.")
            return











    def _handle_file_add(self, table: QTableView, row) -> bool:
        model = table.model()
        property_id = model.data(model.index(row, 0), Qt.DisplayRole)

        from ..Functions.AsBuilt.ASBuilt import TaskQueries
        existing_descriptions = TaskQueries._query_AsBuilt_by_id(property_id=property_id)

        table_check = AsBuiltHelpers.find_existing_notes_table_in_html(existing_descriptions)

        if  table_check is False:
            buttons = {"keep": "Ei ole vaja", "delete": "Jah"}
            ret = DecisionDialogHelper.ask_user(
                title=Headings.inFO_SIMPLE,
                message="Kontrolli tabel puudub. \n\nKas loon kohe ka Konttrolli tabeli?",
                options=buttons,
                parent=self,
                type=AnimatedGradientBorderFrame.PROLOOK
            )
            notes_bool = ret 
        else:
            notes_bool = True

        # Generate file table (and optionally notes block)
        AsBuiltHelpers._handle_drawTool(notes_table=notes_bool)
        prepared_text = AsBuiltHelpers.html

        # Merge file rows only
        combined_html = AsBuiltHelpers.merge_file_table_with_existing(prepared_text, existing_descriptions)

        # Inject/replace notes section if needed
        if notes_bool:
            notes_html = NotesTableGenerator.generate_empty_table()
            combined_html = AsBuiltTools.patch_notes_table_in_html(combined_html, notes_html)

        # Save updated HTML
        res = TaskQueries._update_AsBuilt_by_id(property_id=property_id, description=combined_html)

        if res:
            from ..app.workspace_handler import WorkSpaceHandler
            WorkSpaceHandler.asBuilt_reload(None)

        # Reset temp state
        AsBuiltHelpers.html = ""

