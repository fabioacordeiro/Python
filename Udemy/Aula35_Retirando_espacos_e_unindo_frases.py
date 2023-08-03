'''
Vamos aprender alguns métodos de retirar espaços e unir frases
split = retira os espaços da direita, do meio e da esquerda;
rsplit = retira os espaços da direita
lsplit = retira os espaços da esquerda
strip = quebra a string ou frase em caracteres demarcados como , / espaços etc

'''

frase = '   Estamos aprendendo Python, com o Fábio Alves Cordeiro, desde 2023   '
print(f'String Original:{frase}')
frase1 = frase.split(' ')
print(frase1)
frase2 = frase.split(',')
print(frase2)
frase3 = frase.rsplit(',')
print(frase3)
frase4 = frase.strip('')
print(frase4)
frase4 = frase.strip(' ')
print(frase4)
nova_frase = []

for i, palavra in enumerate(frase):
    nova_frase.append(frase[i].strip())

print(f'Frase Original:{frase1}')
print(f'Frase nova:{nova_frase}')

print(50*'_')
print('Utilizando o Join')
A = 'Estamos aprendendo Python'
B = 'com o Fábio Alves Cordeiro'
C = 'desde 2023'
print(A)
print(B)
print(C)
A=''.join(B)
B = '- '.join(C)
print(A)
print(B)
print(C)
J = A + B + C
print(J)