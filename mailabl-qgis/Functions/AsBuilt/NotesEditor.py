from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QCheckBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QTextEdit, QVBoxLayout, QGroupBox
)
from PyQt5.QtWidgets import QSizePolicy
from datetime import datetime


class NotesEditor:
    NOTE_COL_WIDTHS = {
        "note": 500,
        "checkbox": 25,
        "resolved_date": 100
    }

    NOTE_HEADERS = {
        "note": "🗒️ Märkus",
        "checkbox": "",
        "resolved_date": "📅 Lahendatud"
    }

    def _get_notes_layout(self, widget):
        notes_frame = widget.findChild(QFrame, "frame")
        if not notes_frame:
            print("❌ 'frame' container not found!")
            return None
        notes_layout = notes_frame.layout()
        if not notes_layout:
            print("❌ 'Notes' layout not found!")
        return notes_layout

    def _add_note_table_headers(self, layout: QVBoxLayout):
        frame = QFrame()
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(10)

        for key in ["note", "checkbox", "resolved_date"]:
            label = QLabel(self.NOTE_HEADERS[key])
            label.setFixedWidth(self.NOTE_COL_WIDTHS[key])
            header_layout.addWidget(label)

        frame.setLayout(header_layout)
        layout.addWidget(frame)


    def _create_note_row(self, row_data=None) -> QFrame:
        from PyQt5.QtWidgets import QSizePolicy

        frame = QFrame()
        layout = QHBoxLayout()
        layout.setContentsMargins(2, 0, 2, 0)  # ⬅️ More breathing room around the row
        layout.setSpacing(2)  # Add horizontal space between elements
        
        row_data = row_data or {
            "note": "", "resolved": False, "resolved_date": ""
        }

        # 📝 Note text
        note_edit = QTextEdit()
        note_edit.setText(row_data["note"])
        note_edit.setFixedWidth(self.NOTE_COL_WIDTHS["note"])
        note_edit.setFixedHeight(40)  # Slightly increased for comfort
        note_edit.setContentsMargins(2, 2, 2, 2)  # Padding inside the QTextEdit
        note_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        note_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        note_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # ✅ Centered checkbox (both vertically and horizontally)
        checkbox_container = QFrame()
        checkbox_container.setFixedWidth(self.NOTE_COL_WIDTHS["checkbox"])
        checkbox_container.setFixedHeight(40)  # Match QTextEdit height exactly

        checkbox_layout = QHBoxLayout(checkbox_container)
        checkbox_layout.setContentsMargins(0, 2, 0, 2)  # Add vertical padding
        checkbox_layout.setAlignment(Qt.AlignCenter)

        checkbox = QCheckBox()
        checkbox.setChecked(row_data["resolved"])
        checkbox.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        checkbox_layout.addWidget(checkbox)


        # 📅 Resolved date
        resolved_date_edit = QLineEdit(row_data["resolved_date"])
        resolved_date_edit.setFixedWidth(self.NOTE_COL_WIDTHS["resolved_date"])

        # Auto fill today's date if checked
        def on_state_changed(state):
            if state == Qt.Checked:
                resolved_date_edit.setText(datetime.today().strftime("%d.%m.%Y"))
            else:
                resolved_date_edit.clear()

        checkbox.stateChanged.connect(on_state_changed)

        layout.addWidget(note_edit)
        layout.addWidget(checkbox_container)
        layout.addWidget(resolved_date_edit)

        frame.setLayout(layout)
        return frame


    def add_frame(self, widget, data):
        layout = self._get_notes_layout(widget)
        if not layout:
            return

        grouped = {}
        for note in data:
            grouped.setdefault(note["date"], []).append(note)

        for date, notes in grouped.items():
            group_box = QGroupBox()
            group_box.setTitle(date.strip() if date.strip() else "📅 Kuupäev puudub")
            group_layout = QVBoxLayout()
            group_layout.setSpacing(4)

            self._add_note_table_headers(group_layout)

            for note in notes:
                group_layout.addWidget(self._create_note_row(note))

            group_box.setLayout(group_layout)
            layout.addWidget(group_box)


    def add_note_row_from_button(self, widget):
        layout = self._get_notes_layout(widget)
        if not layout:
            return

        today = datetime.today().strftime("%d.%m.%Y")
        target_group_box = None

        # Check for existing group box with today's date
        for i in range(layout.count()):
            item = layout.itemAt(i).widget()
            if isinstance(item, QGroupBox) and item.title().strip() == today:
                target_group_box = item
                break

        if target_group_box:
            group_layout = target_group_box.layout()
            if group_layout:
                group_layout.addWidget(self._create_note_row())
        else:
            # Create new group box with today's date
            group_box = QGroupBox(today)
            group_layout = QVBoxLayout()
            group_layout.setSpacing(8)

            self._add_note_table_headers(group_layout)
            group_layout.addWidget(self._create_note_row())

            group_box.setLayout(group_layout)
            layout.addWidget(group_box)
        widget.adjustSize()

