from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QFrame, QRadioButton, QMainWindow, QMenuBar, QFileDialog, QListWidget, QTableWidget, QTableWidgetItem, QButtonGroup
from PyQt6.QtGui import QFont, QAction, QPixmap
from PyQt6.QtCore import QTimer, QDir
import sys
import os
import matplotlib.pyplot as plt


class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help")
        self.setGeometry(200, 200, 600, 700)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #eeeeee;")  # BG color

        self.help_text_edit = QTextEdit(self)
        self.help_text_edit.setFont(QFont("Arial", 10))
        self.help_text_edit.setFixedSize(400, 600)  # width and height
        self.help_text_edit.move(150, 10)  # position
        self.help_text_edit.setPlainText("Select an item on the left to learn more.") #init text
        self.help_text_edit.setStyleSheet("background-color: #ffffff; color: #000000; border: 1px ridge #000000;")

        self.help_list_widget = QListWidget(self)
        self.help_list_widget.setGeometry(10, 10, 125, 400)  # (x, y, width, height)
        
        self.help_list_widget.addItem("Introduction")
        self.help_list_widget.addItem("Notes")
        self.help_list_widget.addItem("Positions / Intervals")
        self.help_list_widget.addItem("Chords")
        self.help_list_widget.addItem("Scales")

        self.help_list_widget.addItem("Frequency Calculator")
        self.help_list_widget.addItem("Pitch Finder")

        self.help_list_widget.itemSelectionChanged.connect(self.get_selected_help_item) #calls function on list selection change


    def get_selected_help_item(self):
        selected_item = self.help_list_widget.currentItem()
        if selected_item is None:
            return  # Exit the function if no chord is selected
        if selected_item.text() == "Introduction":
            self.text_introduction()

        if selected_item.text() == "Notes":
            self.text_notes()

        if selected_item.text() == "Positions / Intervals":
            self.text_position()

        if selected_item.text() == "Chords":
            self.text_chords()

        if selected_item.text() == "Scales":
            self.text_scales()

        if selected_item.text() == "Frequency Calculator":
            self.text_fc()

        if selected_item.text() == "Pitch Finder":
            self.text_pf()



########################################################################################################################################
    def text_introduction(self):
        self.help_text_edit.clear()
        self.help_text_edit.append(f'''Introduction
_______________________________________________________  
                                                                  
Music Theory Helper is designed as a general and easy-to-use approach to music theory.
Learning chords and scales can be daunting to a newcomer, so this tool is designed to have all pertinent information as easily accessible as possible.
                                   
If any terminology in this program is new to you, consult the Glossary in the help menu.
                                   
The fundamental goals of this program are as follows:
1. The musician can efficiently understand and memorize the positions that constitute chords and scales
2. The musician will become familiar with the pattern nature of music, such as intervals or relative modes
3. The musician may be able to quickly excel at any instrument by learning the concepts of music theory                                                                                                        
                                   
Comments or contributions can be submitted at:
https://github.com/hemlockchalice                                                                                                     
''')
        



########################################################################################################################################
    def text_notes(self):
        self.help_text_edit.clear()
        self.help_text_edit.append(f'''Notes
_______________________________________________________  
In music, notes are the building blocks of melodies and harmonies. There are 12 unique notes in Western music, which repeat across different octaves. These notes are represented by the letters A, B, C, D, E, F, and G, with sharps (#) and flats (b) used to modify the natural notes. The 12 notes are:

A
A# / Bb (A sharp / B flat)
B
C
C# / Db (C sharp / D flat)
D
D# / Eb (D sharp / E flat)
E
F
F# / Gb (F sharp / G flat)
G
G# / Ab (G sharp / A flat)
                                   
These notes are arranged in a repeating cycle called an octave, where each note is doubled in frequency when moving to the next octave. Notes can also be altered with accidentals (sharps and flats), creating half-step intervals between the natural notes. The relationship between these notes forms the foundation of musical scales and chords.                                  
''')
        



########################################################################################################################################     
    def text_position(self):
        self.help_text_edit.clear()
        self.help_text_edit.append(f'''Positions / Intervals
_______________________________________________________  
                                  
Positions are where the note is located on the staff or instrument, and intervals are the distance between one note and another.
Intervals are measured by half-steps and whole-steps.
In example: note A to its nearest A#/Bb is a half-step, and note A to its nearest B is a whole-step. Note B to its nearest C is a half-step.                                                                                                                            
''')



########################################################################################################################################
    def text_chords(self):
        self.help_text_edit.clear()
        self.help_text_edit.append(f'''Chords
_______________________________________________________  
                                    
Chords in music are combinations of three or more notes played together, usually built from a root note, a third, and a fifth, creating harmonic structures.
They can be major, minor, diminished, augmented, or extended with additional tones like sevenths, ninths, and more. 
Chords provide harmony and support melodies, establishing the tonal context of a piece of music.    
''')



########################################################################################################################################
    def text_scales(self):
        self.help_text_edit.clear()
        self.help_text_edit.append(f'''Scales
_______________________________________________________  
                                    
Scales in music are ordered sequences of notes that span an octave, typically starting and ending on the same note.
They can be major, minor, or other modes, and are built using specific patterns of whole and half steps.
Scales provide the foundation for melody and harmony, defining the tonal framework of a piece of music.     
''')



########################################################################################################################################
    def text_fc(self):
        self.help_text_edit.clear()
        self.help_text_edit.append(f'''Frequency Calculator
_______________________________________________________  
                                    
The Frequency Calculator displays two full octaves worth of frequency values, both descending and ascending, from the entered value.
This tool can be used in combination with 'Pitch Finder' to generate and identify precise pitches.

One example of how this tool may prove useful is as follows:
Say a musician wishes to tune their acoustic guitar to a non-standard tuning, such as E standard tuning in 432Hz, but does not have the necessary digital tuner or I/O to use the tuner.
The Frequency Calculator can be used to find the exact frequency of each strings tuned note (i.e. if A: 432Hz, then E: 323.63Hz), and then these frequencies can be assigned to a generator, from which the musician may accurately tune their guitar to the proper pitch.                                                                                                                                                                                                     

Formula:                                   
                    ƒₙ = ƒᵣₒₒₜ * (2^¹/²)ⁿ   
where ƒₙ is the frequency of the 𝑛-th note
ƒᵣₒₒₜ is the frequency of the root note
ⁿ is the number of semitones above and below the root note                                                                              
                                   
''')


########################################################################################################################################
    def text_pf(self):
        self.help_text_edit.clear()
        self.help_text_edit.append(f'''Pitch Finder
_______________________________________________________  
                                    
The Pitch Finder can be used to identify a base-tones pitch by comparing the base-tone with the generated tone.
This tool is useful when used in combination with 'Frequency Calculator' for precise pitch identification, especially when applied to non-440Hz-based tones.      
This tool can also be used to tune instruments by ear.                                                                
''')
        





if __name__ == "__main__":
    app = QApplication([])
    window = HelpWindow()
    window.show()
    app.exec()