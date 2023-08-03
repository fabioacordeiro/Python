#Faça um programa que leia dois valores e mostre um menu de opções conforme abaixo:
# 1 para Somar
# 2 para Multiplicar
# 3 para Ver maior entre eles
# 4 para Novos Números
# 5 para Sair do programa
from time import sleep
n1 = int(input('Digite o primeiro valor :'))
n2 = int(input('Digite o segundo valor :'))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA    
    ''')
    #opcao = 0
    #while opcao is not (1) or (2) or (3) or (4) or (5):
    opcao = int(input('Opção :'))
    if opcao == 1:
        soma = (n1 + n2)
        print ('O resultado da SOMA entre {} e {} é :{}'.format(n1,n2,soma))
    elif opcao == 2:
        multi = (n1 * n2)
        print('O resultado da SOMA entre {} e {} é :{}'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            print('O número maior entre {} e {} é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('O número maior entre {} e {} é {}'.format(n2, n1, n2))
        else:
            print('Os números {} e {} são iguais '.format(n1, n2))
    elif opcao ==4:
        n1 = int(input('Digite o primeiro valor :'))
        n2 = int(input('Digite o segundo valor :'))
    elif opcao == 5:
        sair = True
        print('SAIR DO PROGRAMA')
        sleep(2)
    else:
        print('opção inválida !!!')
print('Programa encerrado !!!')