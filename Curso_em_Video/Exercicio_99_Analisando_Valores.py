#Faça um programa que analise vários valores e mostre o maior valor, desenvolva uma função para esta análise
from time import sleep

def maior(* núm):
    cont = 0
    maior2 = 0
    print(f'='*50)
    print(' Analisando os valores...')
    for valor in núm:
        cont = cont + 1
        print(f' {valor} ', end='')
        sleep(0.3)
    maior2 = max(núm)
    print(f'\n O maior número é: {maior2}', end='')
    print(f'\n Foram informados {cont} ao todo.')



#Programa Principal
maior(2, 9, 300, 6, 1)
maior(350,158,100,45,2)
maior(2,0)
