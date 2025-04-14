from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QFrame, QRadioButton, QMainWindow, QMenuBar, QFileDialog, QListWidget, QTableWidget, QTableWidgetItem, QButtonGroup
from PyQt6.QtGui import QFont, QAction, QPixmap
from PyQt6.QtCore import QTimer, QDir
import sys
import os
import matplotlib.pyplot as plt


class GlossaryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Glossary")
        self.setGeometry(200, 200, 600, 400)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #eeeeee;")

        self.glossary_label = QLabel("Glossary", self)
        self.glossary_label.setFont(QFont("Arial", 14))
        self.glossary_label.setFixedSize(500, 200)
        self.glossary_label.move(125, 10)

        self.glossary_list_widget = QListWidget(self)
        self.glossary_list_widget.setGeometry(10, 10, 100, 350)
        
        self.glossary_list_widget.addItem("Note")
        self.glossary_list_widget.addItem("Root")
        self.glossary_list_widget.addItem("Octave")
        self.glossary_list_widget.addItem("Accidental")
        self.glossary_list_widget.addItem("Position")
        self.glossary_list_widget.addItem("Interval")
        self.glossary_list_widget.addItem("Half-Step")
        self.glossary_list_widget.addItem("Whole-Step")
        self.glossary_list_widget.addItem("Augmented")
        self.glossary_list_widget.addItem("Harmony")
        self.glossary_list_widget.addItem("Chord")
        self.glossary_list_widget.addItem("Scale")
        self.glossary_list_widget.addItem("Mode")
        self.glossary_list_widget.addItem("Chromatic")
        self.glossary_list_widget.addItem("Minor")
        self.glossary_list_widget.addItem("Major")
        self.glossary_list_widget.addItem("Pentatonic")

        self.glossary_list_widget.itemSelectionChanged.connect(self.get_selected_glossary_item)


    def get_selected_glossary_item(self):
        selected_item = self.glossary_list_widget.currentItem()
        if selected_item is None:
            return
        
        if selected_item.text() == "Note":
            self.glossary_label.setText("A 'note' is a sound that represents a specific pitch,\ntypically indicated by a letter name in music notation.")

        if selected_item.text() == "Root":
            self.glossary_label.setText("The 'root' is the fundamental note of a chord or scale,\nserving as the base from which\nthe chord or scale is built.")

        if selected_item.text() == "Octave":
            self.glossary_label.setText("An 'octave' is the interval between one musical\npitch and another with half or double its frequency,\ntypically eight notes apart in a scale.")

        if selected_item.text() == "Accidental":
            self.glossary_label.setText("An 'accidental' in music is a symbol (such as a sharp,\nflat, or natural) placed before a note to alter its pitch\ntemporarily, outside of the key signature.")

        if selected_item.text() == "Position":
            self.glossary_label.setText("'Position' refers to the placement of a note on a staff,\nwhich determines its pitch relative to other notes.")

        if selected_item.text() == "Interval":
            self.glossary_label.setText("An 'interval' is the distance between two pitches,\nmeasured by the number of steps between them.")

        if selected_item.text() == "Half-Step":
            self.glossary_label.setText("A 'half-step' is the smallest musical interval,\nrepresenting the distance between two adjacent keys\non a keyboard, whether white or black.")

        if selected_item.text() == "Whole-Step":
            self.glossary_label.setText("A 'whole-step' is an interval consisting of two half-steps,\nor the distance between two notes with one note in\nbetween.")

        if selected_item.text() == "Augmented":
            self.glossary_label.setText("'Augmented' means a note or interval is increased\nby a half-step.")

        if selected_item.text() == "Harmony":
            self.glossary_label.setText("'Harmony' refers to the combination of different notes\nplayed simultaneously to create a pleasing sound.")

        if selected_item.text() == "Chord":
            self.glossary_label.setText("A 'chord' is a group of notes played together,\nusually built on a specific root note and its associated\nintervals.")

        if selected_item.text() == "Scale":
            self.glossary_label.setText("A 'scale' is a sequence of notes arranged in ascending\nor descending order, typically following a specific\npattern of intervals.")

        if selected_item.text() == "Mode":
            self.glossary_label.setText("A 'mode' is a type of scale with a specific pattern of\nintervals, often used to create different musical\nmoods or characters.")

        if selected_item.text() == "Chromatic":
            self.glossary_label.setText("'Chromatic' refers to a scale or melody that includes\nall twelve pitches, moving by half-steps.")

        if selected_item.text() == "Minor":
            self.glossary_label.setText("'Minor' refers to a type of scale or chord characterized\nby a lowered third note, giving it a darker or more\nsomber sound.")

        if selected_item.text() == "Major":
            self.glossary_label.setText("'Major' refers to a type of scale or chord characterized\nby a raised third note, giving it a brighter, happier\nsound.")

        if selected_item.text() == "Pentatonic":
            self.glossary_label.setText("'Pentatonic' refers to a scale with five notes.")



if __name__ == "__main__":
    app = QApplication([])
    window = GlossaryWindow()
    window.show()
    app.exec()