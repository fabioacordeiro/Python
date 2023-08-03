#Faça um programa que utilize o Interactive Help do Python.
#O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar a palavra "FIM". O programa se encerra. OBS: use cores.
from time import sleep

c = (
    '\033[4;30;40m',# 0 - Padrão
    '\033[7;30;41m',# 1 - Vermelho
    '\033[7;30;42m',# 2 - Verde
    '\033[4;30;43m',# 3 - Amarelo
    '\033[7;30;44m',# 4 - Azul
    '\033[7;30;45m',# 5 - Roxo
    '\033[7;30m'    # 6 - Branco
)



def ajuda(com):
    titulo(f'Acessando o manual: {com}', 3)
    help(com)
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor],end='')
    print('='*tam)
    print(f'  {msg}')
    print('='* tam)
    print(c[6], end='')
    sleep(1)


#Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('\033[7;30;45m<< Função ou Biblioteca >>:'))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO !!!', 5)
