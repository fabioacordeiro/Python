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
    #Definindo uma cor de thema da Tela
    #Caso não goste da cor atual escolha uma de sua preferencia no 
    #link https://www.geeksforgeeks.org/themes-in-pysimplegui/
    sg.change_look_and_feel('DarkAmber')
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(20,0), key='nome')],
            [sg.Text('Idade',size=(5,0)), sg.Input(size=(20,0), key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos ?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão ?')],
            #Esta opção Radio ela obriga a seleção de apenas 1 opção
            [sg.Radio('Sim','cartões',key='aceitaCartao'), sg.Radio('Não','cartões', key='naoaceitaCartao')],
            # Slider é a regua de seleção de um valor a orientação pode ser h = horizontal ou v=vertical
            [sg.Slider(range=(0,255), default_value=0, orientation='h', size=(15,10), key='sliderVelocidade')],
            [sg.Button('Enviar')],
            [sg.Text('Fechar programa ?')],
            [sg.Checkbox('Sim', key='Sair')],#Esta checkbox é utilizada para sair do programa se estiver selecionada ela retorna True
            [sg.Output(size=(30,20), key='Impressora')]#Imprime na tela as variáveis
            ]
        #janela
        self.janela = sg.Window("Dados do usuário:").layout(layout)
      
      


def Iniciar(self):
    while True:
        #Extrair os dados  da tela
        self.button, self.values = self.janela.Read()
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
        if Sair == True:
            break
       
        

    


tela = TelaPython()
Iniciar(tela)
print(60*'/')

#Temas disponíveis

#[‘Black’, ‘BlueMono’, ‘BluePurple’, ‘BrightColors’, ‘BrownBlue’, ‘Dark’, ‘Dark2’, ‘DarkAmber’, ‘DarkBlack’, ‘DarkBlack1’, ‘DarkBlue’, ‘DarkBlue1’, ‘DarkBlue10’, ‘DarkBlue11’, ‘DarkBlue12’, ‘DarkBlue13’, ‘DarkBlue14’, ‘DarkBlue15’, ‘DarkBlue16’, ‘DarkBlue17’, ‘DarkBlue2’, ‘DarkBlue3’, ‘DarkBlue4’, ‘DarkBlue5’, ‘DarkBlue6’, ‘DarkBlue7’, ‘DarkBlue8’, ‘DarkBlue9’, ‘DarkBrown’, ‘DarkBrown1’, ‘DarkBrown2’, ‘DarkBrown3’, ‘DarkBrown4’, ‘DarkBrown5’, ‘DarkBrown6’, ‘DarkGreen’, ‘DarkGreen1’, ‘DarkGreen2’, ‘DarkGreen3’, ‘DarkGreen4’, ‘DarkGreen5’, ‘DarkGreen6’, ‘DarkGrey’, ‘DarkGrey1’, ‘DarkGrey2’, ‘DarkGrey3’, ‘DarkGrey4’, ‘DarkGrey5’, ‘DarkGrey6’, ‘DarkGrey7’, ‘DarkPurple’, ‘DarkPurple1’, ‘DarkPurple2’, ‘DarkPurple3’, ‘DarkPurple4’, ‘DarkPurple5’, ‘DarkPurple6’, ‘DarkRed’, ‘DarkRed1’, ‘DarkRed2’, ‘DarkTanBlue’, ‘DarkTeal’, ‘DarkTeal1’, ‘DarkTeal10’, ‘DarkTeal11’, ‘DarkTeal12’, ‘DarkTeal2’, ‘DarkTeal3’, ‘DarkTeal4’, ‘DarkTeal5’, ‘DarkTeal6’, ‘DarkTeal7’, ‘DarkTeal8’, ‘DarkTeal9’, ‘Default’, ‘Default1’, ‘DefaultNoMoreNagging’, ‘Green’, ‘GreenMono’, ‘GreenTan’, ‘HotDogStand’, ‘Kayak’, ‘LightBlue’, ‘LightBlue1’, ‘LightBlue2’, ‘LightBlue3’, ‘LightBlue4’, ‘LightBlue5’, ‘LightBlue6’, ‘LightBlue7’, ‘LightBrown’, ‘LightBrown1’, ‘LightBrown10’, ‘LightBrown11’, ‘LightBrown12’, ‘LightBrown13’, ‘LightBrown2’, ‘LightBrown3’, ‘LightBrown4’, ‘LightBrown5’, ‘LightBrown6’, ‘LightBrown7’, ‘LightBrown8’, ‘LightBrown9’, ‘LightGray1’, ‘LightGreen’, ‘LightGreen1’, ‘LightGreen10’, ‘LightGreen2’, ‘LightGreen3’, ‘LightGreen4’, ‘LightGreen5’, ‘LightGreen6’, ‘LightGreen7’, ‘LightGreen8’, ‘LightGreen9’, ‘LightGrey’, ‘LightGrey1’, ‘LightGrey2’, ‘LightGrey3’, ‘LightGrey4’, ‘LightGrey5’, ‘LightGrey6’, ‘LightPurple’, ‘LightTeal’, ‘LightYellow’, ‘Material1’, ‘Material2’, ‘NeutralBlue’, ‘Purple’, ‘Reddit’, ‘Reds’, ‘SandyBeach’, ‘SystemDefault’, ‘SystemDefault1’, ‘SystemDefaultForReal’, ‘Tan’, ‘TanBlue’, ‘TealMono’, ‘Topanga’]