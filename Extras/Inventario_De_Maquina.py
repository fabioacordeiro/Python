#Importando as bibliotecas necessárias documentação
#https://psutil.readthedocs.io/en/latest/#
#https://www.pysimplegui.org/en/latest/#hardware-and-os-support
import sys # Biblioteca do sistema
import os # Pegar um diretorio
import PySimpleGUI as sg #Tela do sistema apelido sg
import datetime # Data e hora do computador
import time  # Hora do sistema
import platform # Pegando o usuário, processador
import psutil # Info HD
import socket # Pegando o IP
import wmi # Informações do processador
 
#Pegando a versão do Python
Versao1 = {sys.version}
#Diretório atual
Diretorio = {os.getcwd()}
#Data do sistema
Data = (f'{datetime.date.today().day}/{datetime.date.today().month}/{datetime.date.today().year}')
#Hora do sistema
Hora = {time.strftime("%H:%M")}
#Colocando as Informações do sistema em uma lista apenas para melhorar a estética
Infosystem = []
Infosystem2 = platform.architecture()
Infosystem.append(Infosystem2[1])
Infosystem.append(Infosystem2[0])
#print(60*'-')
pc = platform.machine()
#print('PC:', pc)
#print(60*'-')
#Informações do Processador e marca, tem mais de 1 biblioteca com essas informações
#estou buscando as informações onde estão mais claras e apresentáveis
c = wmi.WMI()    
my_system = c.Win32_ComputerSystem()[0]
Marca = my_system.Manufacturer
Modelo = my_system.Model
familia = my_system.SystemFamily
Qtd_Processador = my_system.NumberOfProcessors
#Imprimindo as informaçoes na tela
#print(f"Manufacturer: {my_system.Manufacturer}")
#print(f"Model: {my_system.Model}")
#printprint(f"Name: {my_system.Name}")
#print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
#print(f"SystemType: {my_system.SystemType}")
#print(f"SystemFamily: {my_system.SystemFamily}")
#parando o sistema 100 segundos
#time.sleep(100)
#Sistema Operacional
windows = platform.platform()
#Processador
processador = platform.processor()
#Processador grupo de informações não utilizadas
processador1 = platform.platform()
#Pausando o sistema para verificar as informações ==> funções Print e time.sleep(10) parando 10 segundos
##print(processador1)
#time.sleep(10)
#Identificando o usuário do sistema
user = os.getlogin()
#Marca/Modelo do processador
##processador = os.popen('systeminfo')
#Capturando todas as informações da memória do computador
used_memory = psutil.virtual_memory()
#Criando uma lista 
memoria = []
#Acrescentado as informações da variável used_memory na lista memoria com o for
for valor in used_memory:
    memoria.append(valor)
#Buscando os valores da lista de acordo com cada localização dentro da lista
#Transformando de Bytes para Gigabytes(/1000000000)
#Aredondando os valores de Gigabytes com o round(valor, quantidade de casas desejadas)
Ram_TT = round((memoria[0]/1000000000), 2)
#Transformando os valores de inteiro para uma string/texto
# e unindo o novo valor tipo texto com outro texto acredite o Python faz isso com o sinal de +, tem outras formas...
Ram_TT = str(Ram_TT)+' GB Total'
#Repetindo os 2 passos anteriores
Ram_Used = round((memoria[3]/1000000000),2)
Ram_Used = str(Ram_Used)+' GB Used'
Ram_Free = round((memoria[4]/1000000000), 2)
Ram_Free = str(Ram_Free)+' GB Free'
Ram_P = (memoria[2])
Ram_P = str(Ram_P)+' % Used'
#Identificando o Ip da máquina
ip = socket.gethostbyname(socket.gethostname())
#Grupo de informações referente conexão internet
Conect = psutil.net_if_stats()
visualizar = []
for valor in Conect:
    visualizar.append(valor)
#print(visualizar)
#time.sleep(0.10)
#Verificando qual a data e hora do último Boot do computador
Data_hora = psutil.boot_time()
#Formatando a data e hora do computador
boot = datetime.datetime.fromtimestamp(Data_hora).strftime("%d-%m-%Y %H:%M:%S")
##print(boot)
##print(f'RAM memory "%" used:{psutil.virtual_memory()[2]}')
rr = psutil.Process()
rr.memory_info()
##print('login:', rr)
#Informações do usuário
user = os.getlogin()
#Mais informações do usuário
user1 = socket.gethostname()
#Todas as informações do HD
HDi = psutil.disk_usage('/')
#Separando as informações do HD e transformando bytes em Gigabytes
HD_tt = str(round((HDi[0]/1000000000),2))+ ' Gbytes TT'
HD_usado = str(round((HDi[1]/1000000000),2))+ ' Gbytes Used'
HD_free = str(round((HDi[2]/1000000000),2))+ ' Gbytes Free'
HD_p = str(round((HDi[3]),2))+ ' Gbytes %'


#Criando a tela através de uma classe
class TelaPython:
    #Criando um tema é opcional
    Tema = "BlueMono" #Outros temas Black’, ‘BlueMono’, ‘BluePurple’, ‘BrightColors’, ‘BrownBlue’, ‘Dark’, ‘Dark2’, ‘DarkAmber’, ‘DarkBlack’, ‘DarkBlack1’, ‘DarkBlue’,
    sg.change_look_and_feel(Tema)
    #Uma função dentro de uma classe é um método a linha abaixo é um método
    def __init__(self):
        #Definindo as iformações e layout da tela
        layout = [
            #Título (não obrigatório)
            [sg.Titlebar('Informações para inventário de Hardware e Software')],
            #criando um texto, definindo o tamanho, caso não definir o sg se auto define, definindo um texto que recebe uma variável
            # key é o nome estático que você definiu da para a variável Marca que agora é Versao e pode ser utilizada mais tarde 
            [sg.Text('Manufacter/Marca:', size=(15,0)), sg.Text(Marca, size=(50,0), key='Versao')],  
            [sg.Text('Model Processador:', size=(15,0)), sg.Text(Modelo), sg.Text('Família:'), sg.Text(familia)],
            [sg.Text('Brand Processador:', size=(15,0)), sg.Text(processador, size=(50,0))],
            [sg.Text('Info System:', size=(15,0)), sg.Text(Infosystem, size=(50,0))],
            [sg.Text('System Operation:', size=(15,0)), sg.Text(windows, size=(50,0))],
            [sg.Text('Hard Disk:', size=(15,0)), sg.Text(HD_tt), sg.Text(HD_usado), sg.Text(HD_free), sg.Text(HD_p, size=(20,0))],
            [sg.Text('Ram Memory:', size=(15,0)), sg.Text(Ram_TT), sg.Text(Ram_Used), sg.Text(Ram_Free), sg.Text(Ram_P)],
            [sg.Text('IP.:', size=(15,0)), sg.Text(ip)],
            [sg.Text('Last Boot:', size=(15,0)), sg.Text(boot)],
            [sg.Text('User:', size=(15,0)), sg.Text(user), sg.Text(user1)],
            [sg.Text('Data', size=(15,0)), sg.Text(Data)],
            [sg.Text('Hora', size=(15,0)), sg.Text(Hora)],
            [sg.Text('Actual Directory:', size=(15,0)), sg.Text(Diretorio, size=(50,0), key='caminho')],
            [sg.Text('Version of Python:', size=(15,0)), sg.Text(Versao1, size=(50,0), key='Versao1')],
            [sg.Text('Conect:', size=(15,0)), sg.Text(visualizar, size=(30,5))],
            #Criando um botão e definindo a chave como "Ok"
            [sg.Button('Fechar', key='Sair')]
            ]
            #Criando a janela
        self.janela = sg.Window("Info System:").layout(layout)


        #self.button, self.values = self.janela.Read()


#Função iniciando a janela
def Iniciar(self):
    #Criando um looping da janela
    while True:
        #self.event, self.button, self.values = self.janela.Read()
        self.event, self.button = self.janela.Read()
        #Criando uma forma de fechar o loop através do event ao clicar no botão fechar está na documentação do pysimplegui
        if self.event == sg.WIN_CLOSED or self.event == 'Fechar':
            break
        sg.Window.close(self.janela)
    


tela = TelaPython()
Iniciar(tela)
print(60*'/')
print('Fim')
