from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog

from ui_gui_4 import Ui_MainWindow

import json

from pyrogram import Client

class MainWindow(QMainWindow):
    def __init__(self, connect, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(connect)
        self.ui.pushButton.clicked.connect(self.load_settings)
        self.started = False
        self.switch = False

    def load_settings(self):
        file, folder = QFileDialog.getOpenFileName(self, 'Choose settings', '', 'json(*.json)')
        with open(file, 'r') as f:
            text_settings = json.load(f)
        if folder:
            self.ui.lineEdit.setText(str(text_settings['Questions']))
            self.ui.lineEdit_2.setText(str(text_settings['Exceptions']))
            self.ui.lineEdit_3.setText(str(text_settings['Greeting']))
            self.ui.lineEdit_4.setText(str(text_settings['Character']))
            self.ui.lineEdit_5.setText(str(text_settings['api_id']))
            self.ui.lineEdit_6.setText(str(text_settings['api_hash']))