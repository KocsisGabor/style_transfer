# pip install PyQt5
import sys
import os
import subprocess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Style Transfer GUI")

        self.file_label_1 = QLabel("Source image:", self)
        self.file_label_1.move(10, 10)
        self.file_line_edit_1 = QLineEdit(self)
        self.file_line_edit_1.move(110, 10)
        self.file_line_edit_1.setFixedWidth(180)
        self.file_button_1 = QPushButton("Browse", self)
        self.file_button_1.move(300, 10)
        self.file_button_1.clicked.connect(self.select_file_1)

        self.file_label_2 = QLabel("Style image:", self)
        self.file_label_2.move(10, 40)
        self.file_line_edit_2 = QLineEdit(self)
        self.file_line_edit_2.move(110, 40)
        self.file_line_edit_2.setFixedWidth(180)
        self.file_button_2 = QPushButton("Browse", self)
        self.file_button_2.move(300, 40)
        self.file_button_2.clicked.connect(self.select_file_2)

        self.run_button = QPushButton("Style Transfer Run", self)
        self.run_button.move(10, 80)
        self.run_button.clicked.connect(self.run_command)

        self.setGeometry(500, 300, 400, 120)

    def select_file_1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Source image", "", "Images (*.jpg *.png)", options=options)
        if file_name:
            self.file_line_edit_1.setText(file_name)

    def select_file_2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Style image", "", "Images (*.jpg *.png)", options=options)
        if file_name:
            self.file_line_edit_2.setText(file_name)

    def run_command(self):
        file1 = self.file_line_edit_1.text()
        file2 = self.file_line_edit_2.text()
        if file1 and file2:
            # call your command line tool here with file1 and file2 as arguments
            # for example:
            subprocess.run(["style_transfer", file1, file2, "-o", f"{os.path.splitext(file1)[0]}_{os.path.basename(file2).split('.')[0]}.png", "-s 512"])
            pass
        else:
            # show an error message to the user if either file is not selected
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())