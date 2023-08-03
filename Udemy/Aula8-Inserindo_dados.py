import datetime

dt = 2023
nome = 'Fábio'
sobrenome = 'Alves Cordeiro'
idade = 47
ano_nascimento = dt - idade
maior_de_idade = idade >= 18
altura_metros = 1.90

print("Nome:", nome)# Com as variáveis dentro das aspas
print("Sobrenome: {}".format(sobrenome))# Com as variáveis fora das aspas
print("Idade: {} ".format(idade))
print("Ano de Nascimento:", ano_nascimento)
print("É maior de idade:", maior_de_idade)
print("Altura em metros {} mts".format (altura_metros))
