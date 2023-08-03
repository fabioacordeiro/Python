#Fábio Alves Cordeiro
#Instalar pyttsx3
#Pip install pyttsx3
#https://pypi.org/project/pyttsx3/   consulte a biblioteca muito simples

import pyttsx3 
from pathlib import Path
import time


#Pegando o caminho completo do arquivo
print(60*'-')
print(f'{"Caminho completo e nome do arquivo atual":^60}')
Caminho_do_Projeto = Path(__file__)
print(Caminho_do_Projeto)
print(f'{"Diretorio atual":^60}')
Caminho = Caminho_do_Projeto.parent #Movendo caminho completo para um nível acima
print(Caminho)
print(f'{"Caminho completo e nome do arquivo a ser transformado em áudio":^60}')
#Colocando o caminho completo do arquivo aqui na variável
#Pode ser desta forma abaixo comentado também
#'C:\Fabio\Python\Extras.Black.txt'
New_file = Caminho / 'Black.txt'
print(New_file)
print(60*'-')
#Definindo as pausas para verificação de passo a passo no desenvolvimento
time.sleep(0.1)
#Lendo o arquivo txt


#f = open('C:\Fabio\Python\Extras.Black.txt', 'r', encoding="utf8")
f = open(New_file, 'r', encoding="utf8")
texto = f.read()
# Criando o objeto = object creation
Falar = pyttsx3.init() #inicia serviço biblioteca
voices = Falar.getProperty('voices') # Pegando as vozes instaladas
print(60*'-')
#Listando as vozes instaladas na maquina com o for
'''
for voice in voices:
    print(voice, voice.id) #traz os idiomas de voz instalados em sua maquina
'''
#print(60*'-')
lista = []
idioma = []
for voice in voices:
    lista.append(voice.id)
#print('Lista:', lista)
#encontrando onde está o início do TTS que define o idioma com o find
#print(lista[0].find("TTS"))
#Fatiando agora a lista
for valor in lista:
    idioma.append(valor[59:])
#Criando uma variável e inserindo o valor 0
cont = 0
#Imprimindo na tela os idiomas localizados
print(f'{"Idiomas instalados nesta máquina":^60}')
for valor in idioma:
    print(f'Índice: {cont}-{valor}')
    cont+=1
print(60*'-')
#Informe qual idioma quer utilizar 
select = int(input('Digite qual idioma deseja utilizar:'))
#print(select)
#Pausando o programa para que o usuário veja as informações durante 4 segundos
time.sleep(4)
Falar.setProperty('voice', voices[select].id) #O índice começa com 0 verificar quais foram instaladas e informar o número do índice que deseja, eu quero a segunda que esta no índice [1] Inglês
rate = Falar.getProperty('rate')
Falar.setProperty('rate', rate-15) #muda velocidade da leitura, quando menor mais lento

print(texto) #escreve o texto na tela
Falar.say(texto) #define o texto que será lido
Falar.runAndWait() #le o texto
f.close() #fecha o modo deleitura do arquivo txt