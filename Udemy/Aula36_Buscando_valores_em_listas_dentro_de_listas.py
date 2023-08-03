'''
Vamos ver alguns métodos possíveis para executar estas buscas
Lembrando que pode ser listas dentro de lista ou tuplas dentro de listas
'''
Classe_A = ['Maria','Helena','Gisele']
Classe_B = ['Carlos', 'Pedro','Daniel']
Classe_C = ['Geografia','Ciências','Matemática','História']
Classe_N = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
geral = []
geral.append(Classe_A)
geral.append(Classe_B)
geral.append(Classe_C)
geral.append(Classe_N)
print(Classe_A)
print(Classe_B)
print(Classe_C)
print(Classe_N)
print(geral)
print('Acessando pontos específicos da lista:')
print(f'Acessando item 2 da Lista Classe_A dentro da geral :{geral[0][2]}')
print(f'Acessando item 2 da Lista Classe_N dentro da geral: {geral[3][2]}')
print(f'Acessando o item 3 da lista Geral: {geral[3]}')
print('Listando com o For:')
for sala in geral:
    print(f'A sala é:{sala}')
    for aluno in sala:
        print(aluno)
print('Fim laço For')