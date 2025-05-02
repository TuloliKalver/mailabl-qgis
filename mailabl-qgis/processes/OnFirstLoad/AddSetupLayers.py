from qgis.core import QgsProject, QgsLayerTreeGroup
from ...KeelelisedMuutujad.FolderHelper import MailablGroupFolders


class SetupLayers:
    def __init__(self):
        self.main_group = MailablGroupFolders.MAILABL_MAIN
        self.ordered_groups = [
            MailablGroupFolders.SANDBOXING,
            MailablGroupFolders.IMPORT,
            MailablGroupFolders.NEW_PROPERTIES,
            MailablGroupFolders.ARCHIVE,
            MailablGroupFolders.ARCHIVED_PROPERTIES
        ]

    def create_mailabl_setup_group_layer(self):
        root = QgsProject.instance().layerTreeRoot()
        mailabl_group = root.findGroup(self.main_group)

        if mailabl_group is None:
            mailabl_group = QgsLayerTreeGroup(self.main_group)
            root.insertChildNode(-1, mailabl_group)

        # Ensure all groups exist before reordering
        for group_name in self.ordered_groups:
            if mailabl_group.findGroup(group_name) is None:
                mailabl_group.addChildNode(QgsLayerTreeGroup(group_name))

        # Now reorder groups safely
        self._reorder_mailabl_child_groups(mailabl_group)

    def _reorder_mailabl_child_groups(self, parent_group):
        # Build a lookup of all child groups by name
        name_to_group = {group.name(): group for group in parent_group.findGroups()}

        insert_at = 0
        for expected_name in self.ordered_groups:
            original_node = name_to_group.get(expected_name)
            if original_node is None:
                continue

            current_index = parent_group.children().index(original_node)
            if current_index != insert_at:
                # Clone and reinsert at correct position
                clone = original_node.clone()
                parent_group.insertChildNode(insert_at, clone)
                parent_group.removeChildNode(original_node)

            insert_at += 1
