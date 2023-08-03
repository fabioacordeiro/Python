#Crie um programa que desenvolva uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final mostre a matriz na tela com a formatação correta.
L1 = []
L2 = []
L3 = []
digitado = []
valores = []
cont = 0
for v in range(0,9):
    cont = cont+1
    digitado = int(input(f'\033[7;30;44m Digite o {cont}º valor:'))
    if cont <=3:
        L1.append(digitado)
    elif cont >=4 and cont <=6:
        L2.append(digitado)
    else:
        L3.append(digitado)
print('='*15)
print(F'\033[7;30;44m {"MATRIZ 3 X 3":^15}')
print('='*15)
print(f'[ {L1[0]} ][ {L1[1]} ][ {L1[2]} ]')
print(f'[ {L2[0]} ][ {L2[1]} ][ {L2[2]} ]')
print(f'[ {L3[0]} ][ {L3[1]} ][ {L3[2]} ]')
print('='*15)