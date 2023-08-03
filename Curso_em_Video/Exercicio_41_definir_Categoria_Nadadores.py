#Faça um programa que leia a idade de nascimento dos atletas e defina a categoria dos nadadores de acordo com a sua idade:
#Critérios da Confederação Nacional de Nadadores;
#Até 9 anos = MIRIM
#Até 14 anos = INFANTIL
#Até 19 anos = JUNIOR
#Até 25 anos = SENIOR
#Acima 25 anos = MASTER

from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento :'))
idade = atual-nasc
print('O atleta tem {} anos'.format(idade))
if idade < 10:
    print ('Classificação: MIRIM')
elif idade < 15:
    print ('Classificação: INFANTIL')
elif idade < 20:
    print('Classificação: JUNIOR ')
elif idade < 26:
    print('Classificação: SÊNIOR')
else:
    print ('Classificação: MASTER')

