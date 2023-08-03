from random import choice
from time import sleep
cont = 0
Lista = [0,1,2,3,4,5,6,7,8,9,10]
escolhido = choice(Lista)
#print(escolhido)
print('\033[7;30;41m Acabei de pensar em um número entre 0 e 10')
suposicao = int(input('\033[7;30;41m Qual é o seu palpite ? :'))
print('PROCESSANDO ....')
cont = 1
sleep(1)
if suposicao == escolhido:
    print ('\033[7;30;41m Não sei como você fez isto, mas foi sensacional !!! \n Eu pensei de fato no número {}'.format(escolhido))
while suposicao != escolhido:
    cont = cont + 1
    if suposicao > escolhido:
        print('\033[7;30;41m Menos... Tente mais uma vez !!!')
    if suposicao < escolhido:
        print('\033[7;30;41m Mais... Tente mais uma vez !!!')
    suposicao = int(input('\033[7;30;41m Qual é o seu palpite ? :'))
    sleep(1)
#else:
 #   print('O número no qual pensei foi \033[32m :{} \033[m \033[4;33;40m e você chutou o número \033[32m {} \033[m, \033[4;33;40m não acho que você consegue me vencer, mas tente novamente, talvez tenha mais sorte da próxima vez'.format(escolhido, suposicao))
print('\033[7;30;44m Parabéns você acertou. Fim de Jogo !!!!')
print ('\033[7;30;44m Você precisou de {} tentativas'.format(cont))