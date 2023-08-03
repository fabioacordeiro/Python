#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo
# cadastrando tudo em uma lista composta.
from random import randint
from random import choice
lista = []
valores = []
digitado = n1 = n2 = n3 = n4 = n5 = n6 = v = cont = 0
digitado = int(input('\033[7;30;46m Qual a quantidade de palpites a serem gerados ? :'))
print('='*50)
while v != digitado:
    v = v + 1
    n1 = randint(1,60)
    n2 = randint(1,60)
    n3 = randint(1,60)
    n4 = randint(1,60)
    n5 = randint(1,60)
    n6 = randint(1,60)
    if n1 != n2 and n1 != n3 and n1 != n4 and n1 != n5 and n1 != n6 \
            and n2 != n3 and n2 != n4 and n2 != n5 and n2 != n6\
        and n3 != n4 and n3 != n5 and n3 != n6 \
        and n4 != n5 and n4 != n6 \
        and n5 != n6:
        lista.append(n1)
        lista.append(n2)
        lista.append(n3)
        lista.append(n4)
        lista.append(n5)
        lista.append(n6)
        valores.append(lista[:])
        lista.clear()
    else:
        v = v - 1
print(f'{"Palpites de sugestão":^50}')
print('='*50)
for v in valores:
    cont = cont + 1
    print(f'Jogo {cont}: {v}')
print('='*50)