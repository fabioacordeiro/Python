#Crie um programa que leia o nome completo de uma pessoa e faça:
#Mostrar todas as letras maiúsculas;
#Mostras o nome com todas as minúsculas;
#Quantas letras ao "todo sem considerar espaços"
#Quantas letras tem o primeiro nome
nome = str(input('Digite um nome e sobrenome :'))
nome1 = nome.upper()
print('Maiúscula: {}'.format(nome1))
print('Minúscula: {}'.format(nome.lower()))
nome3 = str(nome.strip())
print('A quantidade de Letras sem espaço é: ',len(nome.strip()))
nome4 = nome.split()
#nome5 = nome4.find('')
nome5 = nome4[0]
#print(nome4[0])
print('A quantidade de letras do primeiro nome é: ',len(nome5))

