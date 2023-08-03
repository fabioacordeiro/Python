#Faça o jogo JOKENPO no Python, eu também não conhecia o jogo
#Regras
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)#O computador recebe a variável entre 0 e 2
#print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
humano = int(input('Qual é a sua jogada ? :'))
print ('-=' * 40)
print('Computador jogou {}'.format(itens[computador]))
print('Humano jogou {}'.format(itens[humano]))
print('-=' * 40)
if computador == 0:#Computador jogou PEDRA
           if humano == 0:
               print ('EMPATE')
           elif humano == 1:
               print('HUMANO VENCEU !!!')
           elif humano == 2:
               print('COMPUTADOR VENCEU !!!')
           else:
               print('JOGADA INVALIDA')
elif computador == 1: #Computador jogou PAPEL
        if humano == 0:
            print('COMPUTADOR VENCEU !!!')
        elif humano == 1:
            print('EMPATE')
        elif humano == 2:
            print('HUMANO VENCEU !!!')
        else:
            print('JOGADA INVALIDA')
elif computador == 2:#Computador jogou TESOURA
        if humano == 0:
            print('HUMANO VENCEU !!!')
        elif humano == 1:
            print('COMPUTADOR VENCEU !!!')
        elif humano == 2:
            print('EMPATE')
        else:
            print('JOGADA INVALIDA')
else:
    print('Erro')


