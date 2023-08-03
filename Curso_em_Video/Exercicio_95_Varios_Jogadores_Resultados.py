    #Faça um programa que o usuário digite o nome do jogador e a quantidade de partidas, os gols que o jogador
#fez em cada partida e pergunte se quer continuar, coloque todas as informações em um dicionário;
#Mostre todos os jogadores e resultados, 1 linha para cada jogador:
#O programa vai criar um indice e cada indice digitado mostre individualmente os resultados de cada jogador:
from time import sleep
#time = []
gol = []
jogador = dict()
placar = []
qtde = cont = TT = 0
qtdegols = TTgol = 2
print('\033[7;30;41m='*50)
while True:
    jogador.clear()
    gol.clear()
    jogador['Nome'] = str(input('Nome do Jogador:')).strip().upper()
    qtde = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? :'))
    for v in range (0,qtde):
        cont = cont+1
        gol.append(int(input(f'Quantos gols na partida {cont} ?:')))
    jogador['Gols'] = gol[:]
    jogador['Total'] = sum(gol)
    cont = 0
    placar.append(jogador.copy())
    #print(placar)
    while True:
        resp = str(input('Quer continuar [S/N]:')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO!!! Por favor, digite apenas S ou N:')
    if resp == 'N':
        break
print('='*50)
print(f'placar:{placar}')
print(f'time:{time}')
print(f'gol:{gol}')
print(f'jogador:{jogador}')
print('='*50)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for pos, v in enumerate(placar):
    print(f'{pos:>2}'  , end='')
    for d in v.values():
        print(f' {str(d):<15}' , end='')
    print()
    sleep(1)
print('='*50)
while True:
    localizar = int(input('Mostrar dados de qual jogador ? [999 = parar]:'))
    if localizar == 999:
        break
    if localizar >= len(placar):
        print(f'ERRO!!! Não existe o jogador !!! Veja o índice (Cod) ')
    else:
        print(f'O jogador {placar[localizar]["Nome"]}:')
        for pos, g in enumerate(placar[localizar]['Gols']):
                sleep(1)
                print(f'No jogo {pos+1} fez {g} gols ')
    print('='*50)
print(f'{"VOLTE SEMPRE":^50}')
print('='*50)