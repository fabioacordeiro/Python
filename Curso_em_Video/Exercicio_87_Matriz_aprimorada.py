#Crie um programa que desenvolva uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final mostre:
#A matriz na tela com a formatação correta.
#A soma dos valores pares;
#A soma dos valores da 3ª Coluna
#O maior valor da segunda linha é ?

L1 = []
L2 = []
L3 = []
digitado = []
valores = []
cont = par = impar = letra = 0
for v in range(0,9):
    cont = cont+1
    digitado = int(input(f'\033[7;30;44m Digite o {cont}º valor:'))
    if cont <=3:
        L1.append(digitado)
    elif cont >=4 and cont <=6:
        L2.append(digitado)
    else:
        L3.append(digitado)
valores.append(L1)
valores.append(L2)
valores.append(L3)
for v in valores:
   for letra in v:
        if int(letra) % 2 == 0:
            par = par + letra
print('='*50)
print(f'A soma dos valores pares são: {par}')
print(f'A soma dos valores da 3ª coluna são:{(L3[0]+L3[1]+L3[2])}')
#Print('carro novo' if tempo<=3 else 'carro velho')
print(f'\nO maior valor da 2ª Linha é: {L2[0]}'if L2[0] >= L2[1] and L2[0] >= L2[2] else'', end='')
print(f'O maior valor da 2ª Linha é: {L2[1]}'if L2[1] >= L2[0] and L2[1] >= L2[2] else'', end='')
print(f'O maior valor da 2ª Linha é: {L2[2]}'if L2[2] >= L2[0] and L2[2] >= L2[1] else'')
print('='*50)
print(F'\033[7;30;44m {"MATRIZ 3 X 3":^50}')
print('='*50)
print(f'{"":<19}[ {L1[0]} ][ {L1[1]} ][ {L1[2]} ]{"":>15}')
print(f'{"":<19}[ {L2[0]} ][ {L2[1]} ][ {L2[2]} ]{"":<15}')
print(f'{"":<19}[ {L3[0]} ][ {L3[1]} ][ {L3[2]} ]{"":<15}')
print('='*50)