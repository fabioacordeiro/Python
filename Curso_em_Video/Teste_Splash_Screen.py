#Vamos lá
from PyQT5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import Qtimer
from PyQt5.QtGui import QPixmap

app = QApplication([])

pixmap = QPixmap("Familia.jpg")

splash = QSplashScreen()
splash.setPixmap(pixmap)
Qtimer.singleShot(1000, splash.close) #1000 para 1 segundo
splash.show()
app.exec_()
main.show()