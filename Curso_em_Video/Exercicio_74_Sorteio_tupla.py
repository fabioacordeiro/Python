#Faça um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso mostram a listagem
# de números gerados e também indique o menor e o maior número que estão na tupla.
import random
from random import randint
n  = randint(0,9)
n1 = randint(10,19)
n2 = randint(20,29)
n3 = randint(30,39)
n4 = randint(40,49)
n5 = randint(50,59)
Lista = [n,n1,n2,n3,n4,n5]
#print(f'Print sorteio :{Lista}')
print('Números sorteados:', end='')
random.shuffle(Lista)
print(f'Lista {Lista} ')
print('Print Lista em ordem :{}, {}, {}, {}, {}, {}'.format(n, n1, n2, n3, n4, n5))
print('O número menor é: {}'.format(n))
print('O número maior é: {}'.format(n5))
print(f'Outra forma de fazer número maior é: {max(Lista)}')
print(f'Outra forma de fazer número menor é: {min(Lista)}')
