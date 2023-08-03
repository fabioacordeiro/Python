#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório
#nas eleições

from datetime import date
atual = date.today().year
#16 a <18 facultativo
#  > 70

def voto(num=0):
    idade = atual - num
    if idade > 16 and idade < 18:
        print('O voto é opcional !!!')
    elif idade >70:
        print('O voto é opcional !!!')
    elif idade < 16:
        print('Você ainda não pode votar !!!')
    else:
        print('O voto é obrigatório')


num = int(input('Digite a sua idade: '))
voto(num)
