from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QPushButton
from PyQt6.QtGui import QFont, QAction, QColor
from PyQt6.QtCore import QTimer, Qt
import sys


class FCWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Frequency Calculator")
        self.setGeometry(600, 100, 325, 725)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #eeeeee;")  # BG color

        #label
        self.frequency_entry_label = QLabel(f"Enter Frequency:", self)
        self.frequency_entry_label.setFont(QFont("Arial", 10))
        self.frequency_entry_label.move(10, 30)

        #Create Entry
        self.entry = QLineEdit(self)
        self.entry.setPlaceholderText("440") # Placeholder text
        #self.entry.setText("Hello, PyQt6!") # Set the default text (optional)
        self.entry.setMaxLength(50) # Set maximum character limit (optional)
        self.entry.move(115, 25)

        self.enter_button = QPushButton("Enter", self)
        self.enter_button.setFont(QFont("Arial", 8))
        self.enter_button.move(250, 24)
        self.enter_button.clicked.connect(self.submit)
        self.enter_button.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #000000;
                border: 2px ridge #999999;
                width: 50px;
                height: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                border: 2px solid #0000ff;
            }
            QPushButton:pressed {
                background-color: #0000dd;
                color: #ffff00;
            }
        """)

        # Create a QTableWidget
        self.fc_table = QTableWidget(self)
        self.fc_table.setGeometry(40, 70, 240, 650)
        self.fc_table.setRowCount(25)
        self.fc_table.setColumnCount(2)
        self.fc_table.setHorizontalHeaderLabels(["Note", "Frequency"])

        for row in range(25):
            note_item = QTableWidgetItem("")
            freq_item = QTableWidgetItem("")
            self.fc_table.setRowHeight(row, 1)
            if row == 12:
                note_item.setBackground(QColor("#ADD8E6"))
                freq_item.setBackground(QColor("#ADD8E6"))
            self.fc_table.setItem(row, 0, note_item)
            self.fc_table.setItem(row, 1, freq_item)

        self.fc_table.setColumnWidth(0, 50)
        self.fc_table.setColumnWidth(1, 150)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.submit()  # Call the button function

    def submit(self):
        self.fc_table.clearContents()  # Clear previous entries

        try:
            root_pitch = float(self.entry.text())  # Get user input frequency
        except ValueError:
            return  # Exit if input is invalid

        semitone_ratio = 2 ** (1 / 12)

        # FIXED note list for correct row mapping
        note_list_down = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
        note_list_up = ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A']

        generated_frequencies = [(note_list_down[0], round(root_pitch, 2))]  # 'A' at row 12

        # Generate lower frequencies (rows 11 → 0)
        pitch_down = root_pitch
        for i in range(11, -1, -1):  # Start from Bb (index 10), going downward
            pitch_down /= semitone_ratio
            generated_frequencies.insert(0, (note_list_down[i], round(pitch_down, 2)))

        # Generate higher frequencies (rows 13 → 24)
        pitch_up = root_pitch
        for i in range(12):
            pitch_up *= semitone_ratio
            generated_frequencies.append((note_list_up[i], round(pitch_up, 2)))

        # Populate table
        for row, (note, freq) in enumerate(generated_frequencies):
            item_note = QTableWidgetItem(note)
            item_freq = QTableWidgetItem(f"{freq} Hz")
            self.fc_table.setItem(row, 0, QTableWidgetItem(note))
            self.fc_table.setItem(row, 1, QTableWidgetItem(f"{freq} Hz"))
            if row == 12:
                item_note.setBackground(QColor("#ADD8E6"))  # Light Blue
                item_freq.setBackground(QColor("#ADD8E6"))
                self.fc_table.setItem(row, 0, item_note)
                self.fc_table.setItem(row, 1, item_freq)


    


if __name__ == "__main__":
    app = QApplication([])
    window = FCWindow()
    window.show()
    app.exec()