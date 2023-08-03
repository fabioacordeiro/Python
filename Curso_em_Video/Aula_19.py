#Dicionários
tupla = () #Tuplas
listas = [] #Listas
lista = list() #Listas
dicionarios = {} #Dicionários
dados = dict() #Dicionários
dados = {'nome': 'Fábio Cordeiro', 'idade':46}
print(f'Dicionário Nome:{dados["nome"]}')
print(f'Dicionário idade:{dados["idade"]}')
dados = {'nome':'Lucas','idade':3}
print(f'Dicionário Nome:{dados["nome"]}')
dados = {'nome':'Lucas','idade':3,'nome':'Fabio','idade':46}
print(f'Dicionário values:{dados.values()}')
print(f'Dicionário keys:{dados.keys()}')
print(f'Dicionário items:{dados.items()}')
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(f'Print Brasil:{brasil}')
print(f'Print Brasil[1]:{brasil[1]}')
print(f'Print uf brail[1]:{brasil[0]["uf"]}')
estado = dict()
brasil2 = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: ').upper().strip())
    estado['sigla'] = str(input('Sigla do Estado: ').strip().upper())
    brasil2.append(estado.copy()) #Essa é a forma correta de fazer uma cópia e
for e in brasil2:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in brasil2:
    for v in e.values():
        print(v, end=' ')
    print()
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'c': 40, 'd': 60, 'e': 20}
d1.update(d2)
print(f'Print d1 (d1.update(d2):{d1}')

d1 = {'a': 10, 'b': 20, 'c': 30}
d3 = {**d1, **d2}
print(f'Print d3 ("d3 = **d1, **d2:{d3}')

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'c': 40, 'd': 60, 'e': 20}
print(f'Print d1: {d1}')
print(f'Print d2: {d2}')

d3 = d1 | d2  # Merging
d1 |= d2      # Updating

print(f'Print d3 (d3 = d1 | d2: {d3} Merging')
print(f'Print d1 (d1 |= d2: {d1} Updating')
dt = dict()
dt.copy()

