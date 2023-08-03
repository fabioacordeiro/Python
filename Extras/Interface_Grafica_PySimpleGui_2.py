#para instalar no Python abra a janela cmd do windows
#digite 3+2 se o resultado for diferente de 5 é o porque você
#deve ativar o Powershell para isso basta digitar Powershell no prompt e enter
#pronto agora digite
#pip install pysimplegui
#Caso tenha alguma dúvida 
# abra a documentação no link https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)), sg.Input(size=(15,0),key='idade')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'),sg.Checkbox('Yahoo', key='yahoo') ],
            [sg.Button('Enviar')],
        ]
        #janela
        janela = sg.Window('Dados do usuário:').layout(layout)
        #Extrair os dados  da tela
        self.button, self.values = janela.Read()


def Iniciar(self):
    print(self.values)


tela = TelaPython()
Iniciar(tela)