from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QDialog, QPushButton, QHBoxLayout, QCheckBox, QLabel, QFrame, QWidget
from PyQt5.QtCore import QDate

class ChangeComparer:
    @staticmethod
    def show_changes_summary(changes):
        print("changes:")
        print(changes)
        dialog = QDialog()
        dialog.setWindowTitle("Uuendatavate andemte ülevaade")
        
        layout = QVBoxLayout()
        
        # Check if there are any geometry changes
        any_geom_changes = any(geom_changed for _, _, geom_changed in changes)
        
        # Add a frame for geometry changes if applicable
        geom_change_checkbox = None
        if any_geom_changes:
            geom_frame = QFrame()
            geom_layout = QHBoxLayout()
            geom_change_label = QLabel("Soovitatav on ka uuendada ruumikuju andmeid.")
            geom_change_checkbox = QCheckBox()
            geom_change_checkbox.setChecked(True)
            geom_layout.addWidget(geom_change_label)
            geom_layout.addWidget(geom_change_checkbox)
            geom_frame.setLayout(geom_layout)
            layout.addWidget(geom_frame)
        
        # Calculate the total number of rows required
        total_rows = sum(len(attr_changes) + 1 for _, attr_changes, _ in changes)
        
        table = QTableWidget()
        table.setRowCount(total_rows)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Field", "Andmed hetkel", "Uued andmed", "Uuenda andmeid"])
        
        def format_value(value):
            if isinstance(value, QDate):
                return value.toString("dd.MM.yyyy")
            return str(value)
        
        row = 0
        for fid, attr_changes, geom_changed in changes:
            # Add a row for Kataster
            table.setItem(row, 0, QTableWidgetItem("Kataster"))
            table.setItem(row, 1, QTableWidgetItem(str(fid)))
            table.setItem(row, 2, QTableWidgetItem(str(fid)))
            kataster_checkbox = QCheckBox()
            kataster_checkbox.setChecked(True)
            table.setCellWidget(row, 3, kataster_checkbox)
            row += 1
            
            # Add rows for attribute changes
            for field_name, (old_value, new_value) in attr_changes.items():
                table.setItem(row, 0, QTableWidgetItem(field_name))
                table.setItem(row, 1, QTableWidgetItem(format_value(old_value)))
                table.setItem(row, 2, QTableWidgetItem(format_value(new_value)))
                accept_checkbox = QCheckBox()
                accept_checkbox.setChecked(True)
                table.setCellWidget(row, 3, accept_checkbox)
                row += 1
        
        layout.addWidget(table)
        
        # Automatically resize columns to fit content
        table.resizeColumnsToContents()
        
        # Calculate the total width of the table
        total_width = (table.verticalHeader().width() + table.frameWidth() * 2) + 10
        height = 500
        for column in range(table.columnCount()):
            total_width += table.columnWidth(column)
        
        # Adjust the dialog size to fit the table horizontally and set the height
        dialog.resize(total_width, height)
        
        # Hide row numbers
        table.verticalHeader().setHidden(True)
        
        # Add confirm buttons layout
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()  # Add a stretchable space to push buttons to the right
        confirm_button = QPushButton("Kinnita")
        cancel_button = QPushButton("Tühista")
        buttons_layout.addWidget(confirm_button)
        buttons_layout.addWidget(cancel_button)
        layout.addLayout(buttons_layout)
        
        dialog.setLayout(layout)
        
        confirm_button.clicked.connect(dialog.accept)
        cancel_button.clicked.connect(dialog.reject)
        
        if dialog.exec_() == QDialog.Accepted:
            return geom_change_checkbox.isChecked() if geom_change_checkbox else False
        else:
            return False
