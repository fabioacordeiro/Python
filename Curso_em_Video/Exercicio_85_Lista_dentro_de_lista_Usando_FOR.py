#Faça um programa onde o usuário digite 7 valores numéricos e cadastre em uma única lista onde mantenha separado
# os números pares e ímpares, no final mostre:
#Valores pares e ímpares separados.
cont = c = 0
par = []
impar = []
lista = []
digitado = []
for c in range(0,7):
    cont = cont + 1
    digitado = int(input(f'\033[7;30;41m Digite o {cont}º valores:'))
    if digitado % 2 == 0:#Valores pares
        par.append(digitado)
    else: #Valores ímpares
         impar.append(digitado)
impar.sort()
par.sort()
lista.insert(0,par)
lista.insert(1,impar)
print('='*50)
print(f'\033[7;30;41m Lista completa: {lista}')
print('='*50)
print('\033[7;30;44m Usando o FOR: Os valores pares são: ', end='')
for v in lista:
    for num in v:
        if int(num) % 2 == 0:
            print(f'{num},', end='')
    else:
        print('',end='')
c = 0
print('\n',end='')
print('='*50,end='')
print('\n \033[7;30;45mUsando o FOR: Os valores ímpares são: ', end='')
for v in lista:
    for num in v:
        if int(num) % 2 != 0:
            print(f'{num},', end='')
    else:
        print('',end='')
print('\n',end='')
print('='*50)
print(f'{"Usando o print {lista[0]}":^50}')
#print(f'{"Estrutura de repetição FOR":^60}')
#print('\n',end='')
print(f'Lista Par : {lista[0]}')
print(f'Lista Ímpar : {lista[1]}')
print('='*50,end='')