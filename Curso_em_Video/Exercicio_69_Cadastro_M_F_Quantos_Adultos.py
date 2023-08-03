#Crie um programa que leia a idade e o sexo de várias pessoas e a cada pessoa cadastrada ele deve perguntar se o
#usuário quer continuar, no final mostre:
#Quantas pessoas tem mais de 18 anos ?
#Quantos homens foram cadastrados ?
#Quantas mulheres tem menos de 20 anos;
ver = 'L'
sexo = 'L'
Cont_idade = 0
Conth = 0
mm = 0
while ver not in 'N':
    sexo = 'L'
    idade = int(input('Qual a idade ?:'))
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo ? [M/F]:')).strip().upper()[0]
    Cont_idade = Cont_idade +1
    if sexo == 'M':
        Conth = Conth +1
    if sexo == 'F' and idade < 20:
        mm = mm +1
    ver = str(input('Quer continuar [S/N]:')).strip().upper()[0]
print('Temos no total {} pessoas com mais de 18 anos'.format(Cont_idade))
print('Foram cadastrados {} homens'.format(Conth))
print('Neste grupo tem {} mulheres com menos de 20 anos'.format(mm))
