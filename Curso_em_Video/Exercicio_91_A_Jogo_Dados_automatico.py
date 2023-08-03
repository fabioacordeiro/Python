#Faça um programa que gere 4 números aleatório de um dado (1 a 6) e coloque em ordem de quem tirou o maior número;
#Nenhuma informação será imputada neste exercicio;
from random import randint
from time import sleep
from operator import itemgetter
#time_duration = 3.5
#sleep(time_duration)
print('='*50)
print(f'{"DADOS LANÇADOS":^50}')
print('='*50)
sleep(2)
jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}
ranking = list()
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou{v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i} lugar: {v[0]} com {v[1]}.')
    sleep(1)
