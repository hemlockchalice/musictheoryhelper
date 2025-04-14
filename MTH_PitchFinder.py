import numpy as np
import sounddevice as sd
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QSlider, QTextEdit, QFrame, QRadioButton, QMainWindow, QMenuBar, QFileDialog, QListWidget, QTableWidget, QTableWidgetItem, QButtonGroup, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import os


class PFWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pitch Finder")
        self.setGeometry(200, 200, 300, 300)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #eeeeee;")  # BG color

        #pitch
        self.pitch_label = QLabel("Pitch:", self)
        self.pitch_label.setFont(QFont("Arial", 10))
        self.pitch_label.move(70, 15) #position

        self.pitch_entry = QLineEdit(self)
        self.pitch_entry.setText("440") # Set the default text (optional)
        self.pitch_entry.setFixedSize(80, 25)
        self.pitch_entry.move(110, 10)

        self.hz_label = QLabel("Hz", self)
        self.hz_label.setFont(QFont("Arial", 10))
        self.hz_label.move(200, 15) #position

        #time
        self.duration_slider = QSlider(Qt.Orientation.Horizontal, self)  # Horizontal slider
        self.duration_slider.setMinimum(5)   # Minimum value
        self.duration_slider.setMaximum(50) # Maximum value
        self.duration_slider.setValue(10)    # Default value
        self.duration_slider.setTickPosition(QSlider.TickPosition.TicksBelow)  # Show tick marks
        self.duration_slider.setTickInterval(2)  # Set tick intervals
        self.duration_slider.setFixedSize(200, 25)
        self.duration_slider.move(50, 100)
        self.duration_slider.valueChanged.connect(self.update_duration_label)

        self.duration_label = QLabel(f"Duration: 1 seconds", self)
        self.duration_label.setFont(QFont("Arial", 10))
        self.duration_label.setFixedSize(140, 25)
        self.duration_label.move(90, 70) #position


        #play
        self.PlaySine_button = QPushButton("Play Tone", self)
        self.PlaySine_button.setFont(QFont("Arial", 8))
        self.PlaySine_button.setFixedSize(100, 25)
        self.PlaySine_button.move(100, 150)
        self.PlaySine_button.clicked.connect(self.play_sine)
        self.PlaySine_button.setStyleSheet("""
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

        self.help_label = QLabel("For more info on how to use this tool,\n        refer to the 'Help' section", self)
        self.help_label.setFont(QFont("Arial", 8))
        self.help_label.move(60, 260) #position

    def update_duration_label(self):
        value = (self.duration_slider.value() * 0.1)
        self.duration_label.setText(f"Duration: {value:.1f} seconds")

    def play_sine(self):
        fs = 44100  # Sampling frequency (Hz)
        duration = (self.duration_slider.value() * 0.1)
        freq = float(self.pitch_entry.text())
        t = np.linspace(0, duration, int(fs * duration), endpoint=False) # Generate the waveform
        waveform = 0.5 * np.sin(2 * np.pi * freq * t)  # Amplitude scaled to 0.5
        sd.play(waveform, samplerate=fs) # Play the sound
        sd.wait()

        
if __name__ == "__main__":
    app = QApplication([])
    window = PFWindow()
    window.show()
    app.exec()