#Faça um programa de par ou ímpar de melhor de 3 para jogar contra o
#Fiz o programa inteiro e tive que fazer vários checks ponto a ponto para ir corrigindo os erros,
# estou feliz que sabia fazer isso somente no VBA e agora sei no python...

from random import shuffle,choice
par = impar = humano = cont = 0
escolha = 'L'
vhumano = vcomp = 0

while cont != 3:
    cont = cont + 1
    lista = [1,2,3,4,5,6,7,8,9,10]
    computador = choice(lista)
    #print('Resultado computador {}'.format(computador))
    humano = str(input('\033[7;30;41m Digite um valor :'))
    #print('Ponto 1 Resultado humano {}'.format(humano))
    result = int(computador) + int(humano)
    #print('Ponto 2 Resultado Soma computador e humano {}'.format(result))
    #print('Ponto 3')
    escolha = 'L'
    while escolha not in 'PpIi':
        escolha = str(input('\033[7;30;41m Par ou ímpar [P/I]')).strip().upper()[0]#Strip retirar espações e Upper para colocar em maiúscula [0] para considerar a primeira letra
        if result % 2 == 0:
            #print('Ponto 4 Definicao Par OK')
            if escolha == 'P':
                vhumano = vhumano + 1
                #print('Ponto 8 Definicao PAR HUMANO VENCE OK')
                print('Você jogou {} e o computador {}. Total foi {}, deu PAR !!!'.format(humano,computador, result))
                print('HUMANO VENCEU !!!!')
                print('Vamos jogar novamente.')
                #escolha = 'l'
            elif escolha == 'I':
                vcomp = vcomp + 1
                #print('Ponto 9 Definicao PAR COMPUTADOR VENCE OK')
                print('Você jogou {} e o computador {}. Total foi {}, deu PAR !!!'.format(humano,computador, result))
                print('COMPUTADOR VENCEU !!!!')
                print('Vamos jogar novamente.')
               # escolha = 'l'
        else:
            #print('Ponto 5 Definicao IMPAR OK')
            if escolha == 'I':
                vhumano = vhumano + 1
                #print('Ponto 6 Definicao IMPAR HUMANO VENCE OK')
                print('Você jogou {} e o computador {}. Total foi {}, deu ÍMPAR !!!'.format(humano,computador, result))
                print('HUMANO VENCEU !!!!')
                print('Vamos jogar novamente.')
                #escolha = 'l'
            if escolha == 'P':
                vcomp = vcomp + 1
                #print('Ponto 7 Definicao IMPAR COMPUTADOR VENCE OK')
                print('Você jogou {} e o computador {}. Total foi {}, deu ÍMPAR !!!'.format(humano,computador, result))
                print('COMPUTADOR VENCEU !!!!')
                print('Vamos jogar novamente.')
                #escolha = 'l'
if vhumano > vcomp:
    print('\033[7;30;41m Parabéns você Venceu o computador !!!, pura sorte !!!')
else:
    print('\033[7;30;41m Mais uma vitória do Computador contra os Humanos !!!! Quer tentar novamente ? KKKKKKKKKKKKKK')
print ('\033[7;30;41m GAME OVER !!!')
print('\033[7;30;41m Você venceu {} vez(es)'.format(vhumano))
print ('\033[7;30;41m O computador venceu {} vez(es)'.format(vcomp))