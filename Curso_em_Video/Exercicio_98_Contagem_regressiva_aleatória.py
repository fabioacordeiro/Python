#Faça um programa que inicie uma contagem progressiva pausada de 1 a 10;
#Faça uma contagem regressiva pausada de 10 a 1;
#Faça uma contagem regressiva aleatória com início, fim e passo informado pelo usuário utilizando uma função
from time import sleep
print('='*45)
print('Contagem de 1 até 10 de 1 em 1')

for vetor in range(1, 11):
    print(f'{vetor}, ', end='')
    sleep(1)
print('Fim')
print('='*45)
print('Contagem de 10 até 1 de 2 em 2')
for vetor in range(10, 0, -2):
    print(f'{vetor}, ', end='')
    sleep(1)
print('Fim')
print('='*45)
print('Agora é sua vez de personalizar a contagem !!!')
a = int(input('Início:'))
b = int(input('Fim :'))
c = int(input('Passo:'))
print('='*45)
print(f'A contagem de {a} até {b} de {c} em {c} é:')
for v in range(a,b,c):
    print(f'{v}, ', end='')
    sleep(0.5)
print('Fim')