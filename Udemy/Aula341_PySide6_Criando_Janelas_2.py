# QApplication e QPushButton de PySide6.QtWidgets
# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')
# necessário:
# 1 Widget central 'central_widget = QWidget()'
# 2 layout 'central_widget.setLayout(layout)' podemos escolher qualquer layout que quiser
# 3 E adicionamos os Widget dentro do layout 'layout.addWidget(botao, 1, 1, 1, 1)'
# 4 Poderíamos ter outro layout dentro do layout
central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show()  # Central widget entre na hierarquia e mostre sua janela
app.exec()  # O loop da aplicação
