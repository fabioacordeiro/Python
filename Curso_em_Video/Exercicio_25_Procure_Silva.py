#Faça um programa que procure o sobrenome Silva.
nome = str(input('Digite o seu nome completo :')).strip().upper()
#OU PODEMOS FAZER COMO O GUSTAVAO GUANABARA FEZ ABAIXO, ELE CONSEGUIU FAZER COM 1 TERÇO DE LINHAS A MENOS
# print('Seu nome tem Silva ? {}'.format('SILVA' in nome))
nome2 = nome.find('SILVA')
if nome2 >= 0:
    print('True')
elif nome2 == -1:
    print('False')
