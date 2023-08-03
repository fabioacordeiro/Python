#Faça um programa que leia 4 números e armazene em uma tupla, no final mostre:
#Quantas vezes apareceu o valor 9 ?
#Em que posição foi digitado o primeiro valor 3 ?
#Quais foram os números pares ?
cont = Lista = n1 = n2 = n3 = n4 = 0
par = Pares = ''
linha =','
while cont != 4:
    cont = cont + 1
    Lista = int(input(f'Digite o {cont} Valor inteiro:'))
    if cont == 1:
        n1 = Lista
    if cont == 2:
        n2 = Lista
    if cont == 3:
        n3 = Lista
    if cont == 4:
        n4 = Lista
    if Lista % 2 ==0:
        par = str(Lista)+linha
        Pares = Pares + par
        par = ''
    if n1 and n2 and n3 and n4 > 0:
        tupla = (n1, n2, n3, n4)
print(f'\033[7;30;41m Os números pares são: {Pares}')
if 3 in tupla:
    print('\033[7;30;42m O valor 3 foi digitado na posicão: {}'.format(tupla.index(3)+1))
else:
    print('\033[7;30;43m O valor 3 não foi digitado em nenhuma posição')
if 9 in tupla:
    print(f'\033[7;30;41m O número 9 apareceu {tupla.count(9)} vezes')
else:
    print(' O valor 9 não foi digitado nenhuma vez')
print('\033[7;30;45m Os valores pares são:', end='')
for cont in tupla:
    if cont % 2 == 0:
        print(cont, end=',')
print(f'\033[7;30;44m \n Os valores da tupla são: {tupla}   Fim...')