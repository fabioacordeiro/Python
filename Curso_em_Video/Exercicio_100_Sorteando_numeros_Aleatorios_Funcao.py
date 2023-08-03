#Faça uma função que sorteia 5 números aletatórios e some somente os números pares
from random import randint
from time import sleep

def sorteio(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        números.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('Pronto')




def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'A soma dos valores pares da {lista} são {soma}')

sleep(0.5)

números = list()
sorteio(números)
somapar(números)
print(f'Números sorteados: {números}')

