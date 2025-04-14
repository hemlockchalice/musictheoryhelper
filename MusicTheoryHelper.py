from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QFrame, QRadioButton, QMainWindow, QMenuBar, QFileDialog, QListWidget, QTableWidget, QTableWidgetItem, QButtonGroup, QMessageBox, QCheckBox
from PyQt6.QtGui import QFont, QAction, QIcon, QPixmap
from PyQt6.QtCore import QTimer
import sys
import os
from MTH_FreqCalc import FCWindow
from MTH_PitchFinder import PFWindow
from MTH_Help import HelpWindow
from MTH_Glossary import GlossaryWindow

script_dir = os.path.dirname(os.path.realpath(__file__))

note_to_num_A_flats= {'A1': 0, 'Bb1': 1, 'B1': 2, 'C1': 3, 'Db1': 4, 'D1': 5, 'Eb1': 6, 'E1': 7, 'F1': 8, 'Gb1': 9, 'G1': 10, 'Ab1': 11, 'A2': 12, 'Bb2': 13, 'B2': 14, 'C2': 15, 'Db2': 16}
note_to_num_As_flats= {'Bb1': 0, 'B1': 1, 'C1': 2, 'Db1': 3, 'D1': 4, 'Eb1': 5, 'E1': 6, 'F1': 7, 'Gb1': 8, 'G1': 9, 'Ab1': 10, 'A2': 11, 'Bb2': 12, 'B2': 13, 'C2': 14, 'Db2': 15, 'D2': 16}
note_to_num_B_flats = {'B1': 0, 'C1': 1, 'Db1': 2, 'D1': 3, 'Eb1': 4, 'E1': 5, 'F1': 6, 'Gb1': 7, 'G1': 8, 'Ab1': 9, 'A2': 10, 'Bb2': 11, 'B2': 12, 'C2': 13, 'Db2': 14, 'D2': 15, 'Eb2': 16}
note_to_num_C_flats = {'C1': 0, 'Db1': 1, 'D1': 2, 'Eb1': 3, 'E1': 4, 'F1': 5, 'Gb1': 6, 'G1': 7, 'Ab1': 8, 'A2': 9, 'Bb2': 10, 'B2': 11, 'C2': 12, 'Db2': 13, 'D2': 14, 'Eb2': 15, 'E2': 16}
note_to_num_Cs_flats = {'Db1': 0, 'D1': 1, 'Eb1': 2, 'E1': 3, 'F1': 4, 'Gb1': 5, 'G1': 6, 'Ab1': 7, 'A2': 8, 'Bb2': 9, 'B2': 10, 'C2': 11, 'Db2': 12, 'D2': 13, 'Eb2': 14, 'E2': 15, 'F2': 16}
note_to_num_D_flats = {'D1': 0, 'Eb1': 1, 'E1': 2, 'F1': 3, 'Gb1': 4, 'G1': 5, 'Ab1': 6, 'A2': 7, 'Bb2': 8, 'B2': 9, 'C2': 10, 'Db2': 11, 'D2': 12, 'Eb2': 13, 'E2': 14, 'F2': 15, 'Gb2': 16}
note_to_num_Ds_flats = {'Eb1': 0, 'E1': 1, 'F1': 2, 'Gb1': 3, 'G1': 4, 'Ab1': 5, 'A2': 6, 'Bb2': 7, 'B2': 8, 'C2': 9, 'Db2': 10, 'D2': 11, 'Eb2': 12, 'E2': 13, 'F2': 14, 'Gb2': 15, 'G2': 16}
note_to_num_E_flats = {'E1': 0, 'F1': 1, 'Gb1': 2, 'G1': 3, 'Ab1': 4, 'A2': 5, 'Bb2': 6, 'B2': 7, 'C2': 8, 'Db2': 9, 'D2': 10, 'Eb2': 11, 'E2': 12, 'F2': 13, 'Gb2': 14, 'G2': 15, 'Ab2': 16}
note_to_num_F_flats = {'F1': 0, 'Gb1': 1, 'G1': 2, 'Ab1': 3, 'A2': 4, 'Bb2': 5, 'B2': 6, 'C2': 7, 'Db2': 8, 'D2': 9, 'Eb2': 10, 'E2': 11, 'F2': 12, 'Gb2': 13, 'G2': 14, 'Ab2': 15, 'A3': 16}
note_to_num_Fs_flats = {'Gb1': 0, 'G1': 1, 'Ab1': 2, 'A2': 3, 'Bb2': 4, 'B2': 5, 'C2': 6, 'Db2': 7, 'D2': 8, 'Eb2': 9, 'E2': 10, 'F2': 11, 'Gb2': 12, 'G2': 13, 'Ab2': 14, 'A3': 15, 'Bb3': 16}
note_to_num_G_flats = {'G1': 0, 'Ab1': 1, 'A2': 2, 'Bb2': 3, 'B2': 4, 'C2': 5, 'Db2': 6, 'D2': 7, 'Eb2': 8, 'E2': 9, 'F2': 10, 'Gb2': 11, 'G2': 12, 'Ab2': 13, 'A3': 14, 'Bb3': 15, 'B3': 16}
note_to_num_Gs_flats = {'Ab1': 0, 'A2': 1, 'Bb2': 2, 'B2': 3, 'C2': 4, 'Db2': 5, 'D2': 6, 'Eb2': 7, 'E2': 8, 'F2': 9, 'Gb2': 10, 'G2': 11, 'Ab2': 12, 'A3': 13, 'Bb3': 14, 'B3': 15, 'C3': 16}


note_to_num_A_sharps= {'A1': 0, 'A#1': 1, 'B1': 2, 'C1': 3, 'C#1': 4, 'D1': 5, 'D#1': 6, 'E1': 7, 'F1': 8, 'F#1': 9, 'G1': 10, 'G#1': 11, 'A2': 12, 'A#2': 13, 'B2': 14, 'C2': 15, 'C#2': 16}
note_to_num_As_sharps= {'A#1': 0, 'B1': 1, 'C1': 2, 'C#1': 3, 'D1': 4, 'D#1': 5, 'E1': 6, 'F1': 7, 'F#1': 8, 'G1': 9, 'G#1': 10, 'A2': 11, 'A#2': 12, 'B2': 13, 'C2': 14, 'C#2': 15, 'D2': 16}
note_to_num_B_sharps = {'B1': 0, 'C1': 1, 'C#1': 2, 'D1': 3, 'D#1': 4, 'E1': 5, 'F1': 6, 'F#1': 7, 'G1': 8, 'G#1': 9, 'A2': 10, 'A#2': 11, 'B2': 12, 'C2': 13, 'C#2': 14, 'D2': 15, 'D#2': 16}
note_to_num_C_sharps = {'C1': 0, 'C#1': 1, 'D1': 2, 'D#1': 3, 'E1': 4, 'F1': 5, 'F#1': 6, 'G1': 7, 'G#1': 8, 'A2': 9, 'A#2': 10, 'B2': 11, 'C2': 12, 'C#2': 13, 'D2': 14, 'D#2': 15, 'E2': 16}
note_to_num_Cs_sharps = {'C#1': 0, 'D1': 1, 'D#1': 2, 'E1': 3, 'F1': 4, 'F#1': 5, 'G1': 6, 'G#1': 7, 'A2': 8, 'A#2': 9, 'B2': 10, 'C2': 11, 'C#2': 12, 'D2': 13, 'D#2': 14, 'E2': 15, 'F2': 16}
note_to_num_D_sharps = {'D1': 0, 'D#1': 1, 'E1': 2, 'F1': 3, 'F#1': 4, 'G1': 5, 'G#1': 6, 'A2': 7, 'A#2': 8, 'B2': 9, 'C2': 10, 'C#2': 11, 'D2': 12, 'D#2': 13, 'E2': 14, 'F2': 15, 'F#2': 16}
note_to_num_Ds_sharps = {'D#1': 0, 'E1': 1, 'F1': 2, 'F#1': 3, 'G1': 4, 'G#1': 5, 'A2': 6, 'A#2': 7, 'B2': 8, 'C2': 9, 'C#2': 10, 'D2': 11, 'D#2': 12, 'E2': 13, 'F2': 14, 'F#2': 15, 'G2': 16}
note_to_num_E_sharps = {'E1': 0, 'F1': 1, 'F#1': 2, 'G1': 3, 'G#1': 4, 'A2': 5, 'A#2': 6, 'B2': 7, 'C2': 8, 'C#2': 9, 'D2': 10, 'D#2': 11, 'E2': 12, 'F2': 13, 'F#2': 14, 'G2': 15, 'G#2': 16}
note_to_num_F_sharps = {'F1': 0, 'F#1': 1, 'G1': 2, 'G#1': 3, 'A2': 4, 'A#2': 5, 'B2': 6, 'C2': 7, 'C#2': 8, 'D2': 9, 'D#2': 10, 'E2': 11, 'F2': 12, 'F#2': 13, 'G2': 14, 'G#2': 15, 'A3': 16}
note_to_num_Fs_sharps = {'F#1': 0, 'G1': 1, 'G#1': 2, 'A2': 3, 'A#2': 4, 'B2': 5, 'C2': 6, 'C#2': 7, 'D2': 8, 'D#2': 9, 'E2': 10, 'F2': 11, 'F#2': 12, 'G2': 13, 'G#2': 14, 'A3': 15, 'A#3': 16}
note_to_num_G_sharps = {'G1': 0, 'G#1': 1, 'A2': 2, 'A#2': 3, 'B2': 4, 'C2': 5, 'C#2': 6, 'D2': 7, 'D#2': 8, 'E2': 9, 'F2': 10, 'F#2': 11, 'G2': 12, 'G#2': 13, 'A3': 14, 'A#3': 15, 'B3': 16}
note_to_num_Gs_sharps = {'G#1': 0, 'A2': 1, 'A#2': 2, 'B2': 3, 'C2': 4, 'C#2': 5, 'D2': 6, 'D#2': 7, 'E2': 8, 'F2': 9, 'F#2': 10, 'G2': 11, 'G#2': 12, 'A3': 13, 'A#3': 14, 'B3': 15, 'C3': 16}


global root_note, note_to_num_key, selected_chord
root_note = "A"
note_to_num_key = note_to_num_A_sharps
selected_chord = None


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HC Music Theory Helper")
        self.setWindowIcon(QIcon("MTH_assets/MTH_icon.ico"))
        self.setGeometry(100, 100, 1000, 800)

        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #eeeeee;")  # BG color
  
        menubar = self.menuBar()
        menubar.setStyleSheet("""
    QMenu {
        background-color: #eeeeee;  /* Background color for dropdown menu */
        color: black;  /* Text color for menu items */
    }
    QMenu::item {
        background-color: transparent;  /* Transparent background for menu items */
        color: black;  /* Text color for menu items */
    }
    QMenu::item:selected {
        background-color: #ADD8E6;  /* Background color when hovered over */
        color: black;  /* Text color when hovered */
    }
    QMenu::item:pressed {
        background-color: #7cb0c1;  /* Background color when pressed */
        color: black;  /* Text color when pressed */
    }
""")
        #menu
        menu_menu = menubar.addMenu("Menu")

        about_action = QAction("About", self)
        menu_menu.addAction(about_action)
        about_action.triggered.connect(self.open_about_dialog)

        exit_action = QAction("Exit", self)
        menu_menu.addAction(exit_action)
        exit_action.triggered.connect(self.close)

        #advanced
        advanced_menu = menubar.addMenu("Advanced")

        frequency_calculator_action = QAction("Frequency Calculator", self)
        advanced_menu.addAction(frequency_calculator_action)
        frequency_calculator_action.triggered.connect(self.open_frequency_calculator)

        pitch_finder_action = QAction("Pitch Finder", self)
        advanced_menu.addAction(pitch_finder_action)
        pitch_finder_action.triggered.connect(self.open_pitch_finder)

        #help
        help_menu = menubar.addMenu("Help")

        help_action = QAction("Help", self)
        help_menu.addAction(help_action)
        help_action.triggered.connect(self.open_help_menu)

        glossary_action = QAction("Glossary", self)
        help_menu.addAction(glossary_action)
        glossary_action.triggered.connect(self.open_glossary_menu)


        #selected root note
        self.selected_root_note_label = QLabel(f"Root Note: {root_note}", self)
        self.selected_root_note_label.setFont(QFont("Arial", 10))
        self.selected_root_note_label.setFixedSize(125, 25)
        self.selected_root_note_label.move(20, 50)
        self.selected_root_note_label.setStyleSheet("border: 2px ridge #999999;")

        #root notes header
        self.root_note_label = QLabel("Root Notes", self)
        self.root_note_label.setFont(QFont("Arial", 10))
        self.root_note_label.move(25, 75)


        # Buttons
        self.A_button = QPushButton("A", self)
        self.A_button.setFont(QFont("Arial", 8))
        self.A_button.move(20, 100)
        self.A_button.clicked.connect(self.note_A)
        self.A_button.setStyleSheet("""
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

        self.As_button = QPushButton("A#", self)
        self.As_button.setFont(QFont("Arial", 8))
        self.As_button.move(20, 130)
        self.As_button.clicked.connect(self.note_As)
        self.As_button.setStyleSheet("""
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

        self.B_button = QPushButton("B", self)
        self.B_button.setFont(QFont("Arial", 8))
        self.B_button.move(20, 160)
        self.B_button.clicked.connect(self.note_B)
        self.B_button.setStyleSheet("""
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

        self.C_button = QPushButton("C", self)
        self.C_button.setFont(QFont("Arial", 8))
        self.C_button.move(20, 190)
        self.C_button.clicked.connect(self.note_C)
        self.C_button.setStyleSheet("""
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

        self.Cs_button = QPushButton("C#", self)
        self.Cs_button.setFont(QFont("Arial", 8))
        self.Cs_button.move(20, 220)
        self.Cs_button.clicked.connect(self.note_Cs)
        self.Cs_button.setStyleSheet("""
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

        self.D_button = QPushButton("D", self)
        self.D_button.setFont(QFont("Arial", 8))
        self.D_button.move(20, 250)
        self.D_button.clicked.connect(self.note_D)
        self.D_button.setStyleSheet("""
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

        self.Ds_button = QPushButton("D#", self)
        self.Ds_button.setFont(QFont("Arial", 8))
        self.Ds_button.move(20, 280)
        self.Ds_button.clicked.connect(self.note_Ds)
        self.Ds_button.setStyleSheet("""
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

        self.E_button = QPushButton("E", self)
        self.E_button.setFont(QFont("Arial", 8))
        self.E_button.move(20, 310)
        self.E_button.clicked.connect(self.note_E)
        self.E_button.setStyleSheet("""
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

        self.F_button = QPushButton("F", self)
        self.F_button.setFont(QFont("Arial", 8))
        self.F_button.move(20, 340)
        self.F_button.clicked.connect(self.note_F)
        self.F_button.setStyleSheet("""
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

        self.Fs_button = QPushButton("F#", self)
        self.Fs_button.setFont(QFont("Arial", 8))
        self.Fs_button.move(20, 370)
        self.Fs_button.clicked.connect(self.note_Fs)
        self.Fs_button.setStyleSheet("""
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

        self.G_button = QPushButton("G", self)
        self.G_button.setFont(QFont("Arial", 8))
        self.G_button.move(20, 400)
        self.G_button.clicked.connect(self.note_G)
        self.G_button.setStyleSheet("""
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

        self.Gs_button = QPushButton("G#", self)
        self.Gs_button.setFont(QFont("Arial", 8))
        self.Gs_button.move(20, 430)
        self.Gs_button.clicked.connect(self.note_Gs)
        self.Gs_button.setStyleSheet("""
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

        self.flat_radio_button = QRadioButton("Flats", self)
        self.flat_radio_button.move(20, 475)
        self.flat_radio_button.toggled.connect(self.update_note_format)
        self.flat_radio_button.setChecked(True)


        self.sharp_radio_button = QRadioButton("Sharps", self)
        self.sharp_radio_button.move(80, 475)
        self.sharp_radio_button.toggled.connect(self.update_note_format)

        self.flatsharp_group = QButtonGroup(self)
        self.flatsharp_group.addButton(self.flat_radio_button)
        self.flatsharp_group.addButton(self.sharp_radio_button)

#######################################
        # Create a QTableWidget with 5 rows and 2 columns
        self.table = QTableWidget(self)
        self.table.setGeometry(375, 50, 500, 418)  # Manually position the table
        self.table.setRowCount(13)
        self.table.setColumnCount(4)

        # Set column headers
        self.table.setHorizontalHeaderLabels(["Note", "Position", "Step", "Relative Mode"])

        # Add items to the table
        for row in range(13):
            self.table.setItem(row, 0, QTableWidgetItem(f""))
            self.table.setItem(row, 1, QTableWidgetItem(f""))

         # Set the width of each column
        self.table.setColumnWidth(0, 75)  # first column width
        self.table.setColumnWidth(1, 125)  # second column 
        self.table.setColumnWidth(2, 100)  # second column 
        self.table.setColumnWidth(3, 150)  # fourth column
        self.table.setRowHeight(0, 30)  # row height

#######################################
        self.selected_chordscale_label = QLabel(f"No Chord Selected", self)
        self.selected_chordscale_label.setFont(QFont("Arial", 10))
        self.selected_chordscale_label.setFixedSize(150, 25)
        self.selected_chordscale_label.move(180, 50)
        self.selected_chordscale_label.setStyleSheet("border: 2px ridge #999999;")

        self.chordscale_label = QLabel(f"Chords", self)
        self.chordscale_label.setFont(QFont("Arial", 10))
        self.chordscale_label.setFixedSize(150, 25)
        self.chordscale_label.move(180, 75)

        self.chordscale_list_widget = QListWidget(self)
        self.chordscale_list_widget.setGeometry(180, 100, 150, 360)  # (x, y, width, height)

        self.chordscale_list_widget.setCurrentItem(self.chordscale_list_widget.item(0)) #power chord
        self.chordscale_list_widget.itemSelectionChanged.connect(self.get_selected_chordscale) #calls function on list selection change

        self.chord_radio_button = QRadioButton("Chords", self)
        self.chord_radio_button.move(200, 475)
        self.chord_radio_button.toggled.connect(self.update_theory_format)
        self.chord_radio_button.setChecked(True)

        self.scale_radio_button = QRadioButton("Scales", self)
        self.scale_radio_button.move(270, 475)
        self.scale_radio_button.toggled.connect(self.update_theory_format)

        self.chordscale_group = QButtonGroup(self)
        self.chordscale_group.addButton(self.chord_radio_button)
        self.chordscale_group.addButton(self.scale_radio_button)


#################################################################################################
    #PIANO
        self.piano_notes = [
            "A1", "A#1", "B1", "C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", "A2", "A#2", "B2",
            "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A3", "A#3", "B3", "C3"]
        
        # Mapping flats to sharps
       
        
        self.white_key_width = 30
        self.white_key_height = 150
        self.black_key_width = 20
        self.black_key_height = 100

        self.key_buttons = []
        white_key_positions = []

        black_key_offsets = { # Define black key pattern (offsets relative to white key index)
            "A#1": 0.7, "C#1": 0.7, "D#1": 0.7, "F#1": 0.7, "G#1": 0.7,
            "A#2": 0.7, "C#2": 0.7, "D#2": 0.7, "F#2": 0.7, "G#2": 0.7,
            "A#3": 0.7
        }
        white_key_index = 0  # Track white key positions for black key reference
        current_octave = 1

        for piano_notes in self.piano_notes:
            if "#" not in piano_notes:  # Only natural notes get a white key
                white_key_x = white_key_index * self.white_key_width
                white_key = QPushButton(self)
                white_key.setStyleSheet("background-color: white; border: 1px solid black;")
                white_key.setFixedSize(self.white_key_width, self.white_key_height)
                white_key.move((470 + white_key_x), 550)  # Place each white key sequentially
                white_key.setObjectName(piano_notes)
                white_key.clicked.connect(self.piano_chord)
                self.key_buttons.append(white_key)
                white_key_positions.append((piano_notes, white_key_x))
                white_key_index += 1

        # Now create black keys
        for i in range(len(white_key_positions) - 1):  # Loop through white keys
            piano_notes, white_key_x = white_key_positions[i]
            black_key_name = f"{piano_notes[0]}#{current_octave}" # Determine the black key name based on the white key's letter and add accidental and octave
            
            # If there is a black key between this white key and the next white key
            if black_key_name in black_key_offsets:
                black_x = white_key_x + int(black_key_offsets[black_key_name] * self.white_key_width) # Calculate x position for the black key using the offset
                black_key = QPushButton(self)
                black_key.setStyleSheet("background-color: black; border: 1px solid white;")
                black_key.setFixedSize(self.black_key_width, self.black_key_height)
                black_key.move((470 + black_x), 550)
                black_key.setObjectName(black_key_name)
                black_key.clicked.connect(self.piano_chord)
                black_key.raise_()  # Ensures the black key is on top of the white keys
                self.key_buttons.append(black_key)
                if piano_notes[0] == "G":  # increment octave
                    current_octave += 1

        self.piano_notes_checkbox = QCheckBox("Show Piano\nNotes", self)
        self.piano_notes_checkbox.stateChanged.connect(self.show_piano_notes)
        self.piano_notes_checkbox.move(470, 515)




#################################################################################################
    #SHEET MUSIC

    #TREBLE CLEF
        treble_clef_label = QLabel(self)
        treble_clef_path = os.path.join(script_dir, 'MTH_assets', 'treble_clef.png')
        pixmap = QPixmap(treble_clef_path)
        treble_clef_label.setPixmap(pixmap)
        treble_clef_label.resize(pixmap.width() + 100, pixmap.height())
        treble_clef_label.move(10, 590)

    #SHEET MUSIC LINES
        self.sheet_music_lines = ["Line1", "Line2", "Line3", "Line4", "Line5"]
        self.sm_line_width = 410
        self.sm_line_height = 2
        self.sm_line_labels = []
        sm_line_positions = []
        sm_line_index = 0

        for sheet_music_lines in self.sheet_music_lines:
            sm_line_y = sm_line_index * self.sm_line_height
            sm_line = QLabel(self)
            sm_line.setStyleSheet("background-color: white; border: 1px solid black;")
            sm_line.setFixedSize(self.sm_line_width, self.sm_line_height)
            sm_line.move(20, 610 + ((sm_line_index * 20) + sm_line_y))
            sm_line.setObjectName(sheet_music_lines)
            self.sm_line_labels.append(sm_line)
            sm_line_positions.append((sheet_music_lines, sm_line_y))
            sm_line_index += 1

        self.sheet_music_checkbox = QCheckBox("Show Sheet\nMusic Notes", self)
        self.sheet_music_checkbox.stateChanged.connect(self.show_sheet_music_notes)
        self.sheet_music_checkbox.move(25, 515)


##################################################
#SHEET MUSIC FUNCTIONS
        self.sheet_music_dict = {
        "C3": 559,
        "B3": 570,
        "Bb3": 570,
        "A#3": 581,
        "A3": 581,
        "Ab2": 581,
        "G#2": 592,
        "G2": 592,
        "Gb2": 592,
        "F#2": 603,
        "F2": 603,
        "E2": 614,
        "Eb2": 614,
        "D#2": 625,
        "D2": 625,
        "Db2": 625,
        "C#2": 636,
        "C2": 636,
        "B2": 647,
        "Bb2": 647,
        "A#2": 658,
        "A2": 658,
        "Ab1": 658,
        "G#1": 669,
        "G1": 669,
        "Gb1": 669,
        "F#1": 680,
        "F1": 680,
        "E1": 691,
        "Eb1": 691,
        "D#1": 702,
        "D1": 702,
        "Db1": 702,
        "C#1": 713,
        "C1": 713,
        "B1": 724,
        "Bb1": 724,
        "A#1": 735,
        "A1": 735
        }

        self.sm_note_width = 16
        self.sm_note_height = 16
        self.note_labels = []
        self.line_labels = {}

    def sheet_music_chord(self):
        for label in self.note_labels:
            label.deleteLater()
        self.note_labels.clear()
        for row in range(len(self.generated_notes)):
            note_name = self.generated_notes[row]
            note_x_position_chord = 100
            note_y_position = self.sheet_music_dict.get(note_name, 0)
            note_label = QLabel(self)
            note_label.setStyleSheet("background-color: transparent; border: 3px solid black; border-radius: 7px")
            note_label.setFixedSize(self.sm_note_width, self.sm_note_height)
            note_label.move(note_x_position_chord, note_y_position)
            note_label.show()
            self.note_labels.append(note_label)
            if 'b' in note_name:
                flatsharp_label = QLabel(self)
                flatsharp_label.setText("b")
                flatsharp_label.setStyleSheet("background-color: transparent; font-size: 20px;")
                flatsharp_label.setFixedSize(self.sm_note_width, self.sm_note_height + 5)
                flatsharp_label.move(note_x_position_chord - 12, note_y_position - 5)
                flatsharp_label.show()
                self.note_labels.append(flatsharp_label)
            if '#' in note_name:
                flatsharp_label = QLabel(self)
                flatsharp_label.setText("#")
                flatsharp_label.setStyleSheet("background-color: transparent; font-size: 20px;")
                flatsharp_label.setFixedSize(self.sm_note_width, self.sm_note_height + 5)
                flatsharp_label.move(note_x_position_chord - 12, note_y_position - 5)
                flatsharp_label.show()
                self.note_labels.append(flatsharp_label)
                
        #create outer note lines
            if "A1" in note_name:
                if "A1" not in self.line_labels:
                    A1_sm_line_1 = QLabel(self)
                    A1_sm_line_1.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A1_sm_line_1.setFixedSize(30, self.sm_line_height)
                    A1_sm_line_1.move(note_x_position_chord - 7, 742)
                    A1_sm_line_1.show()

                    A1_sm_line_2 = QLabel(self)
                    A1_sm_line_2.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A1_sm_line_2.setFixedSize(30, self.sm_line_height)
                    A1_sm_line_2.move(note_x_position_chord - 7, 720)
                    A1_sm_line_2.show()
                    self.line_labels["A1"] = [A1_sm_line_1, A1_sm_line_2]
                else:
                    for line in self.line_labels["A1"]:
                        line.show()

            if "A#1" in note_name:
                if "A#1" not in self.line_labels:
                    A1_sm_line_1 = QLabel(self)
                    A1_sm_line_1.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A1_sm_line_1.setFixedSize(30, self.sm_line_height)
                    A1_sm_line_1.move(note_x_position_chord - 7, 742)
                    A1_sm_line_1.show()

                    A1_sm_line_2 = QLabel(self)
                    A1_sm_line_2.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A1_sm_line_2.setFixedSize(30, self.sm_line_height)
                    A1_sm_line_2.move(note_x_position_chord - 7, 720)
                    A1_sm_line_2.show()
                    self.line_labels["A#1"] = [A1_sm_line_1, A1_sm_line_2]
                else:
                    for line in self.line_labels["A#1"]:
                        line.show()

            if "Bb1" in note_name:
                if "Bb1" not in self.line_labels:
                    C1_sm_line = QLabel(self)
                    C1_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C1_sm_line.setFixedSize(30, self.sm_line_height)
                    C1_sm_line.move(note_x_position_chord - 7, 720)
                    C1_sm_line.show()
                    self.line_labels["Bb1"] = C1_sm_line
                else:
                    self.line_labels["Bb1"].show()

            if "B1" in note_name:
                if "B1" not in self.line_labels:
                    C1_sm_line = QLabel(self)
                    C1_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C1_sm_line.setFixedSize(30, self.sm_line_height)
                    C1_sm_line.move(note_x_position_chord - 7, 720)
                    C1_sm_line.show()
                    self.line_labels["B1"] = C1_sm_line
                else:
                    self.line_labels["B1"].show()

            if "C1" in note_name:
                if "C1" not in self.line_labels:
                    C1_sm_line = QLabel(self)
                    C1_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C1_sm_line.setFixedSize(30, self.sm_line_height)
                    C1_sm_line.move(note_x_position_chord - 7, 720)
                    C1_sm_line.show()
                    self.line_labels["C1"] = C1_sm_line
                else:
                    self.line_labels["C1"].show()

            if "C#1" in note_name:
                if "C#1" not in self.line_labels:
                    C1_sm_line = QLabel(self)
                    C1_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C1_sm_line.setFixedSize(30, self.sm_line_height)
                    C1_sm_line.move(note_x_position_chord - 7, 720)
                    C1_sm_line.show()
                    self.line_labels["C#1"] = C1_sm_line
                else:
                    self.line_labels["C#1"].show()

            if "G2" in note_name:
                if "G2" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_chord - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["G2"] = A3_sm_line
                else:
                    self.line_labels["G2"].show()

            if "G#2" in note_name:
                if "G#2" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_chord - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["G#2"] = A3_sm_line
                else:
                    self.line_labels["G#2"].show()

            if "A3" in note_name:
                if "A3" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_chord - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["A3"] = A3_sm_line
                else:
                    self.line_labels["A3"].show()

            if "A#3" in note_name:
                if "A#3" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_chord - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["A#3"] = A3_sm_line
                else:
                    self.line_labels["A#3"].show()

            if "Bb3" in note_name:
                if "Bb3" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_chord - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["Bb3"] = A3_sm_line
                else:
                    self.line_labels["Bb3"].show()

            if "B3" in note_name:
                if "B3" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_chord - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["B3"] = A3_sm_line
                else:
                    self.line_labels["B3"].show()

            if "C3" in note_name:
                if "C3" not in self.line_labels:
                    C3_sm_line = QLabel(self)
                    C3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C3_sm_line.setFixedSize(30, self.sm_line_height)
                    C3_sm_line.move(note_x_position_chord - 7, 566)
                    C3_sm_line.show()
                    self.line_labels["C3"] = C3_sm_line
                else:
                    self.line_labels["C3"].show()
            
            if "C#3" in note_name:
                if "C#3" not in self.line_labels:
                    C3_sm_line = QLabel(self)
                    C3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C3_sm_line.setFixedSize(30, self.sm_line_height)
                    C3_sm_line.move(note_x_position_chord - 7, 566)
                    C3_sm_line.show()
                    self.line_labels["C#3"] = C3_sm_line
                else:
                    self.line_labels["C#3"].show()

        # Hide lines not needed for the current chord
        for line_name, lines in self.line_labels.items():
            if line_name not in [note for note in self.generated_notes]: # Check if the line_name is not in the list of generated_notes
                if isinstance(lines, list): # If it's a list (for cases like "A1"), iterate through each line in the list
                    for line in lines:
                        line.hide()
                else:
                    lines.hide() # If it's just a single QLabel (not a list), hide it directly

    def sheet_music_scale(self):
        for label in self.note_labels:
            label.deleteLater()
        self.note_labels.clear()
        new_note_x_position_scale = 0
        for row in range(len(self.generated_notes)):
            note_name = self.generated_notes[row]
            note_x_position_scale = 100
            note_y_position = self.sheet_music_dict.get(note_name, 0)
            note_label = QLabel(self)
            note_label.setStyleSheet("background-color: transparent; border: 3px solid black; border-radius: 7px")
            note_label.setFixedSize(self.sm_note_width, self.sm_note_height)
            note_label.move(note_x_position_scale + new_note_x_position_scale, note_y_position)
            new_note_x_position_scale += 30
            note_label.show()
            self.note_labels.append(note_label)
            if 'b' in note_name:
                flatsharp_label = QLabel(self)
                flatsharp_label.setText("b")
                flatsharp_label.setStyleSheet("background-color: transparent; font-size: 20px;")
                flatsharp_label.setFixedSize(self.sm_note_width, self.sm_note_height + 5)
                flatsharp_label.move((note_x_position_scale - 44) + new_note_x_position_scale, note_y_position - 5)
                flatsharp_label.show()
                self.note_labels.append(flatsharp_label)
            if '#' in note_name:
                flatsharp_label = QLabel(self)
                flatsharp_label.setText("#")
                flatsharp_label.setStyleSheet("background-color: transparent; font-size: 20px;")
                flatsharp_label.setFixedSize(self.sm_note_width, self.sm_note_height + 5)
                flatsharp_label.move((note_x_position_scale - 44) + new_note_x_position_scale, note_y_position - 5)
                flatsharp_label.show()
                self.note_labels.append(flatsharp_label)
                
        #create outer note lines
            if "A1" in note_name:
                if "A1" not in self.line_labels:
                    A1_sm_line_1 = QLabel(self)
                    A1_sm_line_1.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A1_sm_line_1.setFixedSize(30, self.sm_line_height)
                    A1_sm_line_1.move(note_x_position_scale - 7, 742)
                    A1_sm_line_1.show()

                    A1_sm_line_2 = QLabel(self)
                    A1_sm_line_2.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A1_sm_line_2.setFixedSize(30, self.sm_line_height)
                    A1_sm_line_2.move(note_x_position_scale - 7, 720)
                    A1_sm_line_2.show()
                    self.line_labels["A1"] = [A1_sm_line_1, A1_sm_line_2]
                else:
                    for line in self.line_labels["A1"]:
                        line.show()

            if "A#1" in note_name:
                if "A#1" not in self.line_labels:
                    A1_sm_line_1 = QLabel(self)
                    A1_sm_line_1.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A1_sm_line_1.setFixedSize(30, self.sm_line_height)
                    A1_sm_line_1.move(note_x_position_scale - 7, 742)
                    A1_sm_line_1.show()

                    A1_sm_line_2 = QLabel(self)
                    A1_sm_line_2.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A1_sm_line_2.setFixedSize(30, self.sm_line_height)
                    A1_sm_line_2.move(note_x_position_scale - 7, 720)
                    A1_sm_line_2.show()
                    self.line_labels["A#1"] = [A1_sm_line_1, A1_sm_line_2]
                else:
                    for line in self.line_labels["A#1"]:
                        line.show()

            if "Bb1" in note_name:
                if "Bb1" not in self.line_labels:
                    C1_sm_line = QLabel(self)
                    C1_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C1_sm_line.setFixedSize(30, self.sm_line_height)
                    C1_sm_line.move(note_x_position_scale - 7, 720)
                    C1_sm_line.show()
                    self.line_labels["Bb1"] = C1_sm_line
                else:
                    self.line_labels["Bb1"].show()

            if "B1" in note_name:
                if "B1" not in self.line_labels:
                    C1_sm_line = QLabel(self)
                    C1_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C1_sm_line.setFixedSize(30, self.sm_line_height)
                    C1_sm_line.move(note_x_position_scale - 7, 720)
                    C1_sm_line.show()
                    self.line_labels["B1"] = C1_sm_line
                else:
                    self.line_labels["B1"].show()

            if "C1" in note_name:
                if "C1" not in self.line_labels:
                    C1_sm_line = QLabel(self)
                    C1_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C1_sm_line.setFixedSize(30, self.sm_line_height)
                    C1_sm_line.move(note_x_position_scale - 7, 720)
                    C1_sm_line.show()
                    self.line_labels["C1"] = C1_sm_line
                else:
                    self.line_labels["C1"].show()

            if "C#1" in note_name:
                if "C#1" not in self.line_labels:
                    C1_sm_line = QLabel(self)
                    C1_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C1_sm_line.setFixedSize(30, self.sm_line_height)
                    C1_sm_line.move(note_x_position_scale - 7, 720)
                    C1_sm_line.show()
                    self.line_labels["C#1"] = C1_sm_line
                else:
                    self.line_labels["C#1"].show()

            if "G2" in note_name:
                if "G2" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_scale - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["G2"] = A3_sm_line
                else:
                    self.line_labels["G2"].show()

            if "G#2" in note_name:
                if "G#2" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_scale - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["G#2"] = A3_sm_line
                else:
                    self.line_labels["G#2"].show()

            if "A3" in note_name:
                if "A3" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_scale - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["A3"] = A3_sm_line
                else:
                    self.line_labels["A3"].show()

            if "A#3" in note_name:
                if "A#3" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_scale - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["A#3"] = A3_sm_line
                else:
                    self.line_labels["A#3"].show()

            if "Bb3" in note_name:
                if "Bb3" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_scale - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["Bb3"] = A3_sm_line
                else:
                    self.line_labels["Bb3"].show()

            if "B3" in note_name:
                if "B3" not in self.line_labels:
                    A3_sm_line = QLabel(self)
                    A3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    A3_sm_line.setFixedSize(30, self.sm_line_height)
                    A3_sm_line.move(note_x_position_scale - 7, 588)
                    A3_sm_line.show()
                    self.line_labels["B3"] = A3_sm_line
                else:
                    self.line_labels["B3"].show()

            if "C3" in note_name:
                if "C3" not in self.line_labels:
                    C3_sm_line = QLabel(self)
                    C3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C3_sm_line.setFixedSize(30, self.sm_line_height)
                    C3_sm_line.move(note_x_position_scale - 7, 566)
                    C3_sm_line.show()
                    self.line_labels["C3"] = C3_sm_line
                else:
                    self.line_labels["C3"].show()
            
            if "C#3" in note_name:
                if "C#3" not in self.line_labels:
                    C3_sm_line = QLabel(self)
                    C3_sm_line.setStyleSheet("background-color: transparent; border: 1px solid black;")
                    C3_sm_line.setFixedSize(30, self.sm_line_height)
                    C3_sm_line.move(note_x_position_scale - 7, 566)
                    C3_sm_line.show()
                    self.line_labels["C#3"] = C3_sm_line
                else:
                    self.line_labels["C#3"].show()

        # Hide lines not needed for the current scale
        for line_name, lines in self.line_labels.items():
            if line_name not in [note for note in self.generated_notes]: # Check if the line_name is not in the list of generated_notes
                if isinstance(lines, list): # If it's a list (for cases like "A1"), iterate through each line in the list
                    for line in lines:
                        line.hide()
                else:
                    lines.hide() # If it's just a single QLabel (not a list), hide it directly


    def show_sheet_music_notes(self):
        if self.sheet_music_checkbox.isChecked():
            if hasattr(self, 'sheet_music_labels'): # If labels exist, delete them first to refresh the selection
                for label in self.sheet_music_labels:
                    label.deleteLater()
                self.sheet_music_labels.clear()

            self.sheet_music_labels = []

            treble_notes_lines = ["A", "C", "E", "G", "B", "D", "F", "A", "C"]
            treble_notes_spaces = ["B", "D", "F", "A", "C", "E", "G", "B"]

            treble_notes_lines_x_position = 60
            treble_notes_lines_y_position = 738
            treble_notes_lines_label_spacing = 22

            treble_notes_spaces_x_position = 430
            treble_notes_spaces_y_position = 727
            treble_notes_spaces_label_spacing = 22

            for note in treble_notes_lines:
                label = QLabel(note, self)
                label.setFont(QFont("Arial", 8))
                label.setFixedSize(10, 10)  
                label.setStyleSheet("color: blue")
                label.move(treble_notes_lines_x_position, treble_notes_lines_y_position)
                label.show()
                self.sheet_music_labels.append(label)
                treble_notes_lines_y_position -= treble_notes_lines_label_spacing  

            for note in treble_notes_spaces:
                label = QLabel(note, self)
                label.setFont(QFont("Arial", 8))
                label.setFixedSize(10, 10)  
                label.setStyleSheet("color: blue")
                label.move(treble_notes_spaces_x_position, treble_notes_spaces_y_position)
                label.show()
                self.sheet_music_labels.append(label)
                treble_notes_spaces_y_position -= treble_notes_spaces_label_spacing  

        else:
            if hasattr(self, 'sheet_music_labels'):
                for label in self.sheet_music_labels:
                    label.deleteLater()
                self.sheet_music_labels.clear()



##################################################
#PIANO FUNCTIONS

    def show_piano_notes(self):
        if self.piano_notes_checkbox.isChecked():
            if hasattr(self, 'piano_labels'): # If labels exist, delete them first to refresh the selection
                for label in self.piano_labels:
                    label.deleteLater()
                self.piano_labels.clear()

            natural_notes = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", 
                            "A2", "B2", "C2", "D2", "E2", "F2", "G2",
                            "A3", "B3", "C3"]
            flat_notes = ["Bb1", "Db1", "Eb1", "Gb1", "Ab1", 
                        "Bb2", "Db2", "Eb2", "Gb2", "Ab2",
                        "Bb3"]
            sharp_notes = ["A#1", "C#1", "D#1", "F#1", "G#1", 
                        "A#2", "C#2", "D#2", "F#2", "G#2",
                        "A#3"]
            self.piano_labels = []

            natural_x_position = 472
            natural_y_position = 670  
            natural_label_spacing = 30

            flatsharp_x_position = 486
            flatsharp_y_position = 620
            flatsharp_space_flag = True
            flatsharp_space_count = 0
            flatsharp_label_spacing_big = 60
            flatsharp_label_spacing_small = 30

            for note in natural_notes:
                label = QLabel(note, self)
                label.setFont(QFont("Arial", 10))
                label.setFixedSize(26, 20)  
                label.setStyleSheet("border: 1px solid blue; border-radius: 4px; color: blue")
                label.move(natural_x_position, natural_y_position)
                label.show()
                self.piano_labels.append(label)
                natural_x_position += natural_label_spacing  

            selected_notes = flat_notes if self.flat_radio_button.isChecked() else sharp_notes
            for note in selected_notes:
                label = QLabel(note, self)
                label.setFont(QFont("Arial", 10))
                label.setFixedSize(28, 20)  
                label.setStyleSheet("border: 1px solid blue; border-radius: 4px; color: blue")
                label.move(flatsharp_x_position, flatsharp_y_position)
                label.show()
                self.piano_labels.append(label)  # Store all labels
                flatsharp_space_count += 1
                if flatsharp_space_flag:
                    flatsharp_x_position += flatsharp_label_spacing_big
                    flatsharp_space_flag = False
                else:
                    flatsharp_x_position += flatsharp_label_spacing_small
                    if flatsharp_space_count in [4, 9]:
                        flatsharp_space_flag = False
                    else:
                        flatsharp_space_flag = True
        else:
            if hasattr(self, 'piano_labels'):
                for label in self.piano_labels:
                    label.deleteLater()
                self.piano_labels.clear()

    def clear_piano(self):
        for key in self.key_buttons:
            if "#" in key.objectName():
                key.setStyleSheet("background-color: black; border: 1px solid white;")
            else:
                key.setStyleSheet("background-color: white; border: 1px solid black;")

    def piano_chord(self):
        self.clear_piano()
        sharp_to_flat = {
            "A#1": "Bb1", "C#1": "Db1", "D#1": "Eb1", "F#1": "Gb1", "G#1": "Ab1",
            "A#2": "Bb2", "C#2": "Db2", "D#2": "Eb2", "F#2": "Gb2", "G#2": "Ab2",
            "A#3": "Bb3"
        }
        if hasattr(self, 'generated_notes'):
            for key in self.key_buttons:
                note_name = key.objectName()
                if note_name in self.generated_notes:
                    key.setStyleSheet("background-color: lightgreen; border: 1px solid black;")
                elif note_name in sharp_to_flat and sharp_to_flat[note_name] in self.generated_notes:
                    key.setStyleSheet("background-color: lightgreen; border: 1px solid black;")
                else:
                    if "#" in note_name:  # This is a black key
                        key.setStyleSheet("background-color: black; border: 1px solid white;")
                    else:  # White keys reset to white background
                        key.setStyleSheet("background-color: white; border: 1px solid black;")


    def piano_scale(self):
        self.clear_piano()
        sharp_to_flat = {
            "A#1": "Bb1", "C#1": "Db1", "D#1": "Eb1", "F#1": "Gb1", "G#1": "Ab1",
            "A#2": "Bb2", "C#2": "Db2", "D#2": "Eb2", "F#2": "Gb2", "G#2": "Ab2",
            "A#3": "Bb3"
        }
        if hasattr(self, 'generated_notes'):
            for i, note in enumerate(self.generated_notes):
                for key in self.key_buttons:
                    note_name = key.objectName()
                    if note_name in self.generated_notes:
                        key.setStyleSheet(f"background-color: lightgreen; border: 1px solid black;")
                    elif note_name in sharp_to_flat and sharp_to_flat[note_name] in self.generated_notes:
                        key.setStyleSheet(f"background-color: lightgreen; border: 1px solid black;")
                    else:
                        # Reset style for black and white keys
                        if "#" in note_name:  # This is a black key
                            key.setStyleSheet("background-color: black; border: 1px solid white;")
                        else:  # White keys reset to white background
                            key.setStyleSheet("background-color: white; border: 1px solid black;")



#################################################################################################################################################################################################
#FUNCTIONS

    def open_about_dialog(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("About")
        msg_box.setText(
    "Hemlock Chalice Music Theory Helper<br><br>"
    "A tool designed for learning music theory.<br>"
    "This software is licensed under the GPL-3 license.<br>"
    "Comment or contribute on github:<br>"
    '<a href="https://github.com/hemlockchalice">https://github.com/hemlockchalice</a>'
)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)  # Add Ok button
        msg_box.exec()  # Show the dialog

    def open_frequency_calculator(self):
        self.frequency_calculator = FCWindow()
        self.frequency_calculator.show()

    def open_pitch_finder(self):
        self.pitch_finder = PFWindow()
        self.pitch_finder.show()

    def open_help_menu(self):
        self.help_menu = HelpWindow()
        self.help_menu.show()

    def open_glossary_menu(self):
        self.glossary_menu = GlossaryWindow()
        self.glossary_menu.show()

    def update_theory_format(self):
        self.chordscale_list_widget.clear()
        if self.chord_radio_button.isChecked():
            self.chordscale_label.setText(f"Chords")
            self.chordscale_list_widget.addItem("Fifth")
            self.chordscale_list_widget.addItem("Power Chord")
            self.chordscale_list_widget.addItem("Minor Triad")
            self.chordscale_list_widget.addItem("Major Triad")
            self.chordscale_list_widget.addItem("Suspended Fourth")
            self.chordscale_list_widget.addItem("Simple Minor Seventh")
            self.chordscale_list_widget.addItem("Minor Seventh")
            self.chordscale_list_widget.addItem("Minor Arpeggio")
            self.chordscale_list_widget.addItem("Simple Major Seventh")
            self.chordscale_list_widget.addItem("Major Seventh")
            self.chordscale_list_widget.addItem("Major Arpeggio")
            self.chordscale_list_widget.addItem("Dominant Seventh")
            self.chordscale_list_widget.addItem("Add Nine")
        elif self.scale_radio_button.isChecked():
            self.clear_piano()
            self.chordscale_label.setText(f"Scales")
            self.chordscale_list_widget.addItem("Chromatic")
            self.chordscale_list_widget.addItem("Minor (Aeolian)")
            self.chordscale_list_widget.addItem("Major (Ionian)")
            self.chordscale_list_widget.addItem("Phyrgian")
            self.chordscale_list_widget.addItem("Dorian")
            self.chordscale_list_widget.addItem("Locrian")
            self.chordscale_list_widget.addItem("Lydian")
            self.chordscale_list_widget.addItem("Mixolydian")
            self.chordscale_list_widget.addItem("Harmonic Minor")
            self.chordscale_list_widget.addItem("Harmonic Major")
            self.chordscale_list_widget.addItem("Minor Pentatonic")
            self.chordscale_list_widget.addItem("Major Pentatonic")


    def get_selected_chordscale(self):
        self.table.clearContents()
        selected_item = self.chordscale_list_widget.currentItem()
        if selected_item is None:
            return  # Exit the function if no chord is selected
        if selected_item.text() == "Fifth":
            self.fifth(root_note, note_to_num_key)
        if selected_item.text() == "Power Chord":
            self.power_chord(root_note, note_to_num_key)
        if selected_item.text() == "Minor Triad":
            self.minor_triad(root_note, note_to_num_key)
        if selected_item.text() == "Major Triad":
            self.major_triad(root_note, note_to_num_key)
        if selected_item.text() == "Suspended Fourth":
            self.suspended_fourth(root_note, note_to_num_key)
        if selected_item.text() == "Simple Minor Seventh":
            self.simple_minor_seventh(root_note, note_to_num_key)
        if selected_item.text() == "Minor Seventh":
            self.minor_seventh(root_note, note_to_num_key)
        if selected_item.text() == "Minor Arpeggio":
            self.minor_arpeggio(root_note, note_to_num_key)
        if selected_item.text() == "Simple Major Seventh":
            self.simple_major_seventh(root_note, note_to_num_key)
        if selected_item.text() == "Major Seventh":
            self.major_seventh(root_note, note_to_num_key)
        if selected_item.text() == "Major Arpeggio":
            self.major_arpeggio(root_note, note_to_num_key)
        if selected_item.text() == "Dominant Seventh":
            self.dominant_seventh(root_note, note_to_num_key)
        if selected_item.text() == "Add Nine":
            self.add_nine(root_note, note_to_num_key)

        if self.chord_radio_button.isChecked():
            self.piano_chord() #apply notes to the piano
            self.sheet_music_chord()
        
        if selected_item is None:
            return  # Exit the function if no scale is selected
        if selected_item.text() == "Chromatic":
            self.chromatic(root_note, note_to_num_key)
        if selected_item.text() == "Minor Pentatonic":
            self.minor_pentatonic(root_note, note_to_num_key)
        if selected_item.text() == "Minor (Aeolian)":
            self.minor(root_note, note_to_num_key)
        if selected_item.text() == "Harmonic Minor":
            self.harmonic_minor(root_note, note_to_num_key)
        if selected_item.text() == "Major Pentatonic":
            self.major_pentatonic(root_note, note_to_num_key)
        if selected_item.text() == "Major (Ionian)":
            self.major(root_note, note_to_num_key)
        if selected_item.text() == "Harmonic Major":
            self.harmonic_major(root_note, note_to_num_key)
        if selected_item.text() == "Phyrgian":
            self.phyrgian(root_note, note_to_num_key)
        if selected_item.text() == "Lydian":
            self.lydian(root_note, note_to_num_key)
        if selected_item.text() == "Mixolydian":
            self.mixolydian(root_note, note_to_num_key)
        if selected_item.text() == "Dorian":
            self.dorian(root_note, note_to_num_key)
        if selected_item.text() == "Locrian":
            self.locrian(root_note, note_to_num_key)

        if self.scale_radio_button.isChecked():
            self.piano_scale() #apply notes to the piano
            self.sheet_music_scale()
        selected_chordscale = selected_item.text()
        self.selected_chordscale_label.setText(f"{selected_chordscale}")


    def update_note_format(self):
        if self.flat_radio_button.isChecked():
            self.As_button.setText("Bb")
            self.Cs_button.setText("Db")
            self.Ds_button.setText("Eb")
            self.Fs_button.setText("Gb")
            self.Gs_button.setText("Ab")
        elif self.sharp_radio_button.isChecked():
            self.As_button.setText("A#")
            self.Cs_button.setText("C#")
            self.Ds_button.setText("D#")
            self.Fs_button.setText("F#")
            self.Gs_button.setText("G#")
        QTimer.singleShot(0, self.declare_root_note)
        QTimer.singleShot(0, self.get_selected_chordscale)


    def declare_root_note(self): #necessary for update_note_format, requires slingshot
        if root_note == "A":
            self.note_A()
        if root_note == "B":
            self.note_B()
        if root_note == "C":
            self.note_C()
        if root_note == "D":
            self.note_D()    
        if root_note == "E":
            self.note_E()
        if root_note == "F":
            self.note_F()
        if root_note == "G":
            self.note_G()
        #flats
        if root_note == "Bb":
            self.note_As()
        if root_note == "Db":
            self.note_Cs()
        if root_note == "Eb":
            self.note_Ds()
        if root_note == "Gb":
            self.note_Fs()
        if root_note == "Ab":
            self.note_Gs()
        #sharps
        if root_note == "A#":
            self.note_As()
        if root_note == "C#":
            self.note_Cs()
        if root_note == "D#":
            self.note_Ds()
        if root_note == "F#":
            self.note_Fs()
        if root_note == "G#":
            self.note_Gs()



################################################################################################################################################################################################
    #N0TE FUNCTIONS
    def note_A(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_A_flats
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_A_sharps
        root_note = 'A1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()


    def note_As(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_As_flats
            root_note = 'Bb1'
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_As_sharps
            root_note = 'A#1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()

    def note_B(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_B_flats
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_B_sharps
        root_note = 'B1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()

    def note_C(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_C_flats
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_C_sharps
        root_note = 'C1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()

    def note_Cs(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_Cs_flats
            root_note = 'Db1'
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_Cs_sharps
            root_note = 'C#1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()

    def note_D(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_D_flats
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_D_sharps
        root_note = 'D1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()

    def note_Ds(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_Ds_flats
            root_note = 'Eb1'
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_Ds_sharps
            root_note = 'D#1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()

    def note_E(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_E_flats
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_E_sharps
        root_note = 'E1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()

    def note_F(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_F_flats
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_F_sharps
        root_note = 'F1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()

    def note_Fs(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_Fs_flats
            root_note = 'Gb1'
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_Fs_sharps
            root_note = 'F#1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()

    def note_G(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_G_flats
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_G_sharps
        root_note = 'G1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()

    def note_Gs(self):
        global root_note, note_to_num_key
        if self.flat_radio_button.isChecked():
            note_to_num_key = note_to_num_Gs_flats
            root_note = 'Ab1'
        elif self.sharp_radio_button.isChecked():
            note_to_num_key = note_to_num_Gs_sharps
            root_note = 'G#1'
        self.selected_root_note_label.setText(f"Root Note: {root_note}")
        self.get_selected_chordscale()






#################################################################################################################################################################################################
#CHORDS
    def fifth(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 7]  # The intervals for the power chord (Root, Perfect 5th, Octave)
        generated_notes = []  # List to store the generated notes
        generated_positions = ["Root", "Fifth"]  # List to store the generated positions
        generated_steps = ["Root", "7"]
        for step in steps: # Generate the notes
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes #store notes as instance variable
        for row in range(len(generated_notes)):  # Append the generated notes and positions to the table (first column for notes, second for positions), and loop over the notes
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row])) # Update the first column (Column 0) with notes
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row])) # Update the second column (Column 1) with corresponding positions
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def power_chord(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 7, 5]
        generated_notes = []
        generated_positions = ["Root", "Fifth", "Octave"]
        generated_steps = ["Root", "7", "5"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def minor_triad(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 3, 4]
        generated_notes = []
        generated_positions = ["Root", "Minor Third", "Fifth"]
        generated_steps = ["Root", "3", "4"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def major_triad(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 4, 3]
        generated_notes = []
        generated_positions = ["Root", "Major Third", "Fifth"]
        generated_steps = ["Root", "4", "3"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def suspended_fourth(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 5, 2]
        generated_notes = []
        generated_positions = ["Root", "Fourth", "Fifth"]
        generated_steps = ["Root", "5", "2"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def simple_minor_seventh(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 7, 3]
        generated_notes = []
        generated_positions = ["Root", "Fifth", "Minor Seventh"]
        generated_steps = ["Root", "7", "3"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def minor_seventh(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 3, 4, 3]
        generated_notes = []
        generated_positions = ["Root", "Minor Third", "Fifth", "Minor Seventh"]
        generated_steps = ["Root", "3", "4", "3"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def minor_arpeggio(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 3, 4, 5]
        generated_notes = []
        generated_positions = ["Root", "Minor Third", "Fifth", "Octave"]
        generated_steps = ["Root", "3", "4", "5"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def simple_major_seventh(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 7, 4]
        generated_notes = []
        generated_positions = ["Root", "Fifth", "Major Seventh"]
        generated_steps = ["Root", "7", "4"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def major_seventh(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 4, 3, 4]
        generated_notes = []
        generated_positions = ["Root", "Major Third", "Fifth", "Major Seventh"]
        generated_steps = ["Root", "4", "3", "4"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def major_arpeggio(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 4, 3, 5]
        generated_notes = []
        generated_positions = ["Root", "Major Third", "Fifth", "Octave"]
        generated_steps = ["Root", "4", "3", "5"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def dominant_seventh(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 4, 3, 3]
        generated_notes = []
        generated_positions = ["Root", "Major Third", "Fifth", "Minor Seventh"]
        generated_steps = ["Root", "4", "3", "3"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def add_nine(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 7, 7]
        generated_notes = []
        generated_positions = ["Root", "Fifth", "Added Ninth"]
        generated_steps = ["Root", "7", "7"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))











#################################################################################################################################################################################################
#SCALES
    def chromatic(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # The intervals for the power chord (Root, Perfect 5th, Octave)
        generated_notes = []  # List to store the generated notes
        generated_positions = ["Root", "Semitone", "Semitone", "Semitone", "Semitone", "Semitone", "Semitone", "Semitone", "Semitone", "Semitone", "Semitone", "Semitone", "Octave"]  # List to store the generated positions
        generated_steps = ["Root", "Half", "Half", "Half", "Half", "Half", "Half", "Half", "Half", "Half", "Half", "Half", "Half"]
        for step in steps: # Generate the notes
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):  # Append the generated notes and positions to the table (first column for notes, second for positions), and loop over the notes
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row])) # Update the first column (Column 0) with notes
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row])) # Update the second column (Column 1) with corresponding positions
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))

    def minor_pentatonic(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 3, 2, 2, 3, 2]  
        generated_notes = []
        generated_positions = ["Root", "Minor Third", "Fourth", "Fifth", "Minor Seventh", "Octave"]
        generated_steps = ["Root", "3 Half", "Whole", "Whole", "3 Half", "Whole"]
        generated_relative_modes = ["Minor Pentetonic", "Major Pentatonic", None, None, None, "Minor Pentatonic"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))
            self.table.setItem(row, 3, QTableWidgetItem(generated_relative_modes[row]))

    def minor(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 2, 1, 2, 2, 1, 2, 2] 
        generated_notes = []
        generated_positions = ["Root", "Second", "Minor Third", "Fourth", "Fifth", "Minor Sixth", "Minor Seventh", "Octave"]
        generated_steps = ["Root", "Whole", "Half", "Whole", "Whole", "Half", "Whole", "Whole"]
        generated_relative_modes = ["Minor (Aeolian)", "Phyrgian", "Major", "Dorian", "Locrian", "Lydian", "Mixolydian", "Minor (Aeolian)"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))
            self.table.setItem(row, 3, QTableWidgetItem(generated_relative_modes[row]))

    def harmonic_minor(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 2, 1, 2, 2, 1, 3, 1]
        generated_notes = []
        generated_positions = ["Root", "Second", "Minor Third", "Fourth", "Fifth", "Minor Sixth", "Major Seventh", "Octave"]
        generated_steps = ["Root", "Whole", "Half", "Whole", "Whole", "Half", "3 Half", "Whole"]
        generated_relative_modes = ["Harmonic Minor", "Phyrgian", "Major", "Dorian", "Locrian", "Lydian", "Locrian #2", "Harmonic Minor"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))
            self.table.setItem(row, 3, QTableWidgetItem(generated_relative_modes[row]))

    def major_pentatonic(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 2, 2, 3, 2, 3]
        generated_notes = []
        generated_positions = ["Root", "Second", "Major Third", "Fifth", "Major Seventh", "Octave"]
        generated_steps = ["Root", "Whole", "Whole", "3 Half", "Whole", "3 Half"]
        generated_relative_modes = ["Major Pentetonic", None, None, None, "Minor Pentatonic", "Major Pentatonic"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))
            self.table.setItem(row, 3, QTableWidgetItem(generated_relative_modes[row]))

    def major(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 2, 2, 1, 2, 2, 2, 1]
        generated_notes = []
        generated_positions = ["Root", "Second", "Major Third", "Fourth", "Fifth", "Major Sixth", "Major Seventh", "Octave"]
        generated_steps = ["Root", "Whole", "Whole", "Half", "Whole", "Whole", "Whole", "Half"]
        generated_relative_modes = ["Major", "Dorian", "Phyrgian", "Lydian", "Mixolydian", "Minor (Aeolian)", "Locrian", "Major"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))
            self.table.setItem(row, 3, QTableWidgetItem(generated_relative_modes[row]))

    def harmonic_major(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 2, 2, 1, 2, 1, 3, 1]
        generated_notes = []
        generated_positions = ["Root", "Second", "Major Third", "Fourth", "Fifth", "Minor Sixth", "Major Seventh", "Octave"]
        generated_steps = ["Root", "Whole", "Whole", "Half", "Whole", "Half", "3 Half", "Half"]
        generated_relative_modes = ["Harmonic Major", "Locrian", "Major", "Dorian", "Phyrgian", "Lydian", "Mixolydian", "Harmonic Major"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))
            self.table.setItem(row, 3, QTableWidgetItem(generated_relative_modes[row]))

    def phyrgian(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 1, 2, 2, 1, 2, 2, 2]
        generated_notes = []
        generated_positions = ["Root", "Augmented Second", "Minor Third", "Fourth", "Flatted Fifth", "Minor Sixth", "Minor Seventh", "Octave"]
        generated_steps = ["Root", "Half", "Whole", "Whole", "Half", "Whole", "Whole", "Whole"]
        generated_relative_modes = ["Phyrgian", "Major", "Dorian", "Locrian", "Lydian", "Mixolydian", "Minor (Aeolian)", "Phyrgian"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))
            self.table.setItem(row, 3, QTableWidgetItem(generated_relative_modes[row]))

    def dorian(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 2, 1, 2, 2, 2, 1, 2]
        generated_notes = []
        generated_positions = ["Root", "Second", "Minor Third", "Fourth", "Fifth", "Major Sixth", "Minor Seventh", "Octave"]
        generated_steps = ["Root", "Whole", "Half", "Whole", "Whole", "Whole", "Half", "Whole"]
        generated_relative_modes = ["Dorian", "Locrian", "Lydian", "Mixolydian", "Minor (Aeolian)", "Phyrgian", "Major", "Dorian"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))
            self.table.setItem(row, 3, QTableWidgetItem(generated_relative_modes[row]))

    def locrian(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 1, 2, 2, 2, 1, 2, 2]
        generated_notes = []
        generated_positions = ["Root", "Augmented Second", "Minor Third", "Fourth", "Fifth", "Minor Sixth", "Minor Seventh", "Octave"]
        generated_steps = ["Root", "Half", "Whole", "Whole", "Whole", "Half", "Whole", "Whole"]
        generated_relative_modes = ["Locrian", "Lydian", "Mixolydian", "Minor (Aeolian)", "Phyrgian", "Major", "Dorian", "Locrian"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))
            self.table.setItem(row, 3, QTableWidgetItem(generated_relative_modes[row]))

    def lydian(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 2, 2, 2, 1, 2, 2, 1]
        generated_notes = []
        generated_positions = ["Root", "Second", "Major Third", "Augmented Fourth", "Fifth", "Major Sixth", "Major Seventh", "Octave"]
        generated_steps = ["Root", "Whole", "Whole", "Whole", "Half", "Whole", "Whole", "Half"]
        generated_relative_modes = ["Lydian", "Mixolydian", "Minor (Aeolian)", "Phyrgian", "Major", "Dorian", "Locrian", "Lydian"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))
            self.table.setItem(row, 3, QTableWidgetItem(generated_relative_modes[row]))
    
    def mixolydian(self, root_note, note_to_num_key):
        note_to_num = note_to_num_key
        steps = [0, 2, 2, 1, 2, 2, 1, 2]
        generated_notes = []
        generated_positions = ["Root", "Second", "Major Third", "Fourth", "Fifth", "Major Sixth", "Minor Seventh", "Octave"]
        generated_steps = ["Root", "Whole", "Whole", "Half", "Whole", "Whole", "Half", "Whole"]
        generated_relative_modes = ["Mixolydian", "Minor (Aeolian)", "Phyrgian", "Major", "Dorian", "Locrian", "Lydian", "Mixolydian"]
        for step in steps:
            next_note_index = (note_to_num[root_note] + step)
            next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
            root_note = next_note_candidates[0]
            generated_notes.append(root_note)
        self.generated_notes = generated_notes
        for row in range(len(generated_notes)):
            self.table.setItem(row, 0, QTableWidgetItem(generated_notes[row]))
            self.table.setItem(row, 1, QTableWidgetItem(generated_positions[row]))
            self.table.setItem(row, 2, QTableWidgetItem(generated_steps[row]))
            self.table.setItem(row, 3, QTableWidgetItem(generated_relative_modes[row]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())