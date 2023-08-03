'''
Vamos ver como o Python trabalha na chamada das funções
'''
A = ['Maria','Helena','Gisele']#listas
B = 'Carlos', 'Pedro','Daniel' #Tuplas
C = ['Geografia','Ciências','Matemática','História']
D = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)#tuplas

A.append(D)
print(f'Lista A {A}')
print(f'Utilizando o For end= e sep=')
for nome in B:
    print(nome, end=';', sep=';')
print()
print(*A)
print(*A, sep=' ; ')