#Crie um programa que leia vários numeros inteiros pelo teclado.
#o programa só vai parar quando o usuário digitar 999
#No final mostre:
#Quanto números foram digitados e qual foi a soma entre eles sem considerar a parada 999
soma = cont = 0
while True:
    n = int(input('Digite um valor [999 para parar] :'))
    if n == 999:
        break
    soma = soma + n #O mesmo que soma = soma + n
    cont = cont + 1 #O mesmo que cont = cont + 1
print('O total de números digitado foi {}'.format(cont))
print('A soma dos números é {} e a média é {}'.format(soma,soma/cont))

