#Faça um programa que inicie uma contagem progressiva pausada de 1 a 10;
#Faça uma contagem regressiva pausada de 10 a 1;
#Faça uma contagem regressiva aleatória com início, fim e passo informado pelo usuário utilizando uma função
from time import sleep

def contregressiva(i, f, p):
    print(f'='*50)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p = p * (-1)
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont}', end='')
            sleep(0.5)
            cont = cont + p
        print(' Fim...')
    else:
        cont = i
        while cont >= f:
            print(f' {cont}', end='')
            sleep(0.5)
            cont = cont - p
        print(' Fim...')



#Programa principal
contregressiva(1, 10, 1)
contregressiva(10, 0, 2)
print(f'='*50)
print(f'{"Agora é sua vez de personalizar a contagem":^50}')
ini = int(input('Início: '))
fim = int(input(f'Fim: '))
pas = int(input(f'Passo: '))
contregressiva(ini, fim, pas)