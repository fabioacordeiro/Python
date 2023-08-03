#para instalar no Python abra a janela cmd do windows
#digite 3+2 se o resultado for diferente de 5 é o porque você
#deve ativar o Powershell para isso basta digitar Powershell no prompt e enter
#pronto agora digite
#pip install pysimplegui
#Caso tenha alguma dúvida 
# abra a documentação no link https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg
import time

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade',size=(5,0)), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos ?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão ?')],
            [sg.Radio('Sim','cartões',key='aceitaCartao'), sg.Radio('Não','cartões', key='naoaceitaCartao')],
            [sg.Slider(range=(0,255), default_value=0, orientation='h', size=(15,10), key='sliderVelocidade')],
            [sg.Button('Enviar')],
            [sg.Text('Fechar programa ?')],
            [sg.Checkbox('Sim', key='Sair')]
            ]
        #janela
        janela = sg.Window("Dados do usuário:").layout(layout)
        #Extrair os dados  da tela
        self.button, self.values = janela.Read()


def Iniciar(self):
    #print(self.values)
    #self.button, self.values = self.janela.Read()
    print(60*'-')
    nome = self.values['nome']
    idade = self.values['idade']
    agree_gmail = self.values['gmail']
    agree_yahoo = self.values['yahoo']
    agree_outlook = self.values['outlook']
    agree_cartao = self.values['aceitaCartao']
    desagree_cartao = self.values['naoaceitaCartao']
    velocidadeslider = self.values['sliderVelocidade']
    Sair = self.values['Sair']
    print(f'nome:{nome}')
    print(f'idade:{idade}')
    print(f'Gmail:{agree_gmail}')
    print(f'Yahoo:{agree_yahoo}')
    print(f'Outlook:{agree_outlook}')
    print(f'Aceita Cartão:{agree_cartao}')
    print(f'Não aceita Cartão:{desagree_cartao}')
    print(f'Velocidade Slider:{velocidadeslider}')
    print(f'Sair do programa:{Sair}')
    #time.sleep(2)
    print('Fim')


tela = TelaPython()
Iniciar(tela)
print(60*'/')
