from random import choice
from time import sleep
Lista = [0,1,2,3,4,5]
escolhido = choice(Lista)
suposicao = int(input('\033[4;33;40m Tente adivinhar qual o número que eu pensei entre 0 e 5 :'))
print('PROCESSANDO ....')
sleep(1)
if suposicao == escolhido:
    print ('Não sei como você fez isto, mas foi sensacional !!! \n Eu pensei de fato no número {}'.format(escolhido))
    print('Parabéns !!! Você me venceu !!!!')
    print('Quer tentar de novo ?')
    print ('\033[0;31;40m Acho que não ousaria')
else:
    print('O número no qual pensei foi \033[32m :{}\n \033[m \033[4;33;40m E você chutou o número \033[32m {} \033[m, \033[4;33;40m \n Não acho que você consiga me vencer, mas tente novamente, \n Talvez tenha mais sorte da próxima vez'.format(escolhido, suposicao))
    print('Você não me venceu !!!!')

