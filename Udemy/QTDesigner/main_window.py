# pip3 install PyQt6

import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        mainWindow.show()
        app.exec()
