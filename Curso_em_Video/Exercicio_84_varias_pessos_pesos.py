# Crie um programa que leia nome e peso de várias pessoas infinito, pergunte se quer continuar, guardando tudo em uma lista e mostre:
#Quantas pessoas foram cadastradas
#Uma listagem com pessoas mais pesadas
#Uma listagem com as pessoas mais leves
pessoas = []
dpessoas = []
peso = []
pesadas = []
leves = []
cont = tp = tl = pmin = pmax = metade = cont2 = 0
digitado = 'L'
while True:
    dpessoas.append(str(input('Nome:')).strip().upper())
    dpessoas.append(int(input('Peso:')))
    pessoas.append(dpessoas[:])
    dpessoas.clear()
    cont = cont+1
    digitado = str(input('Deseja continuar [S/N] ?:')).strip().upper()
    if digitado == 'N':
        break
for p in pessoas:
    peso.append(int(p[1]))
pmin = min(peso)
pmax = max(peso)
metade = cont // 2
peso.sort()
for p in peso:
    cont2 = cont2+1
    if cont2 <= metade and cont2 <= 2:
        leves.append(p)
cont2 = 0
peso.sort(reverse=True)
for p in peso:
    cont2 = cont2+1
    if cont2 <= metade and cont2 <= 2:
        pesadas.append(p)
print('\033[7;30;42m='*50)
print(f'\033[7;30;42m Foram cadastradas {cont} pessoas')
print('='*50)
print(f'\033[7;30;44m As pessoas leves são:')
for p in pessoas:
    if p[1] in leves:
        print(f'{p[0]} com {p[1]}',end=', ')
print('\n ')
print('='*50)
print(f'\033[7;30;46m As pessoas pesadas são:')
for p in pessoas:
    if p[1] in pesadas:
        print(f'\033[7;30;46m {p[0]} com {p[1]}', end=', ')
print('\n ')
print('='*50)