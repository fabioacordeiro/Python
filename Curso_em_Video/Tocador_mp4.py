from PyQt5.qtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('player.ico'))
        self.setWindowTitle('PyPlayer')
        self.setGeometry(350,100, 700,500)
        p=self.palette()
        p.setColor(QPalette.Window, Qt)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
