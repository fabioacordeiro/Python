#Faça um programa que o usuário digite o nome do jogador e a quantidade de gols que o jogador
#fez nas ultimas 5 partidas e mostre, coloque todas as informações em um dicionário;
#Mostre o dicionário
#Os gols;
#Total de gols
from time import sleep
jogador = dict()
gols = []
Qtde = cont = v = TT = 0
print('\033[7;30;41m='*50)
jogador['Nome'] = str(input('Nome do Jogador:')).strip().upper()
Qtde = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? :'))
for v in range (0,Qtde):
    cont = cont+1
    digitado = int(input(f'Quantos gols na partida {cont} ?:'))
    gols.append(digitado)
    TT = TT + digitado
jogador['Gols'] = gols[:]
jogador['Total'] = TT
print('='*50)
for pos, v in jogador.items():
    print(f'{pos}: {v}')
print('='*50)
sleep(1)
print(f'O jogador {jogador["Nome"]} jogou {Qtde} partidas')
for pos, v in enumerate(gols):
    print(f'Na partida {pos+1} fez {v} gols')
    sleep(1)
print(f'Foi um total de {TT} gols')
print('='*50)
print(jogador)
print('='*50)