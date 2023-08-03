#Desenvolver um programa que leia o nome, idade e sexo de 4 pessas e mostre
# média de anos do grupo
# Qual o nome do homem mais velho
# Quantas mulheres tem com menos de 20 anos ?

idadeg = 0
sexof = 0
for cont in range (1,5):
    print ('----- {} PESSOA -----'.format(cont))
    Nome = str(input('Nome :'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:'))
    idadeg = (idadeg + idade)
    if sexo == 'M':
        Idadehmaisvelho = idade
        Nomehmaisvelho = Nome
        if idade > Idadehmaisvelho:
            Idadehmaisvelho = idade
            Nomehmaisvelho = Nome
    elif sexo == 'F':
        if idade < 20:
            sexof = sexof + 1
print ('A idade média do grupo é de {}'.format(idadeg/cont))
print ('O homem mais velho tem {} anos e se chama {} '.format(Idadehmaisvelho,Nomehmaisvelho))
print ('Ao todo são {} mulheres com menos de 20 anos'.format(sexof))