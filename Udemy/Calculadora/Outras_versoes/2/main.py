import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from display import Display
from main_window import MainWindow
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display = Display()
    #display.setPlaceholdertext('Digite algo aqui...')
    window.addToVLayout(display)
    window.addToVLayout(Display('Display 2'))
    window.addToVLayout(Display())    

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()