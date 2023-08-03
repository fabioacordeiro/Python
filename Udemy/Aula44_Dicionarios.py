'''
Aprendendo a manipular dicionários

'''
#Dicionários
import copy
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
print(f'Print uf Brasil[1]:{brasil[0]["uf"]}')
estado = dict()
brasil2 = list()
for c in range(0,3):
    estado['uf'] = str(input('informe o nome do Estado: ').upper().strip())
    estado['sigla'] = str(input('Informe a Sigla do Estado: ').strip().upper())
    brasil2.append(estado.copy()) #Essa é a forma correta de fazer uma cópia e
print(50*'-')
print('Valores digitados')
for e in brasil2:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print(50*'-')
for e in brasil2:
    for v in e.values():
        print(v, end=' ')
    print()
print(50*'-')
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'c': 40, 'd': 60, 'e': 20}
d1.update(d2)
print(f'Print d1 "d1.update(d2)":{d1}')

d1 = {'a': 10, 'b': 20, 'c': 30}
d3 = {**d1, **d2}
print(f'Print d3 "d3 = **d1, **d2":{d3}')

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'c': 40, 'd': 60, 'e': 20}
print(f'Print d1: {d1}')
print(f'Print d2: {d2}')

d3 = d1 | d2  # Merging
d1 |= d2      # Updating

print(f'Print d3 "d3 = d1 | d2": {d3} Merging')
print(f'Print d1 "d1 |= d2": {d1} Updating')
dt = dict(d1)
print(f'dt:{dt}')

pessoa = {'nome':'Lucas da Silva Cordeiro',
'idade':4,
'Endereco':'Av. Açucenas, Porltal dos Ipes',
'Cidade':'Cajamar'}
#A função setdefault insere a informação default mesmo se a chave não existir no dicionário
#pessoa.setdefault('idade':0)
print(pessoa['idade'])
'''
Cópia rasa e cópia profunda
A cópia rasa, copia os dados somente no primeiro nível, ou seja, listas dentro do dicionário 
serão copiados, porém as alterações feitas em uma das listas afetaram os 2 dicionários

A cópia produnda fara uma 
cópia dos dados totalmente independentes
Exemplo
'''
# Cópia rasa
print(50*'-')
print('Exemplo de cópia rasa')
d = {'nome':'Lucas da Silva Cordeiro',
'idade':4,
'Endereco':'Av. Açucenas, Porltal dos Ipes',
'Cidade':'Cajamar',
'Notas':[10, 8, 9, 10],}
copiarasa = d.copy()

d['Cidade'] = 'São Paulo'
copiarasa['Notas'][1] = 8, 9,7
print(d)
print(copiarasa)
print(50*'-')
print('Exemplo de cópia profunda, é necessário "import copy" codigo "copiaprofunda = copy.deepcopy(d)"')
copiaprofunda = copy.deepcopy(d)

d['Cidade'] = 'Niteroi'
copiaprofunda['Notas'][1] = 9.9
print(d)
print(copiaprofunda)
print(50*'-')
print('Imprimir com get "d.get(nome, não existe)"e chamada direta no dicionário "(d[nome])"')
print(d['nome'])
print(d.get('nome', 'não existe'))
print(50*'-')
print(' Deletando uma chave específica ou a ultima chave')
ver = d.pop('Cidade')
print(f'Item a ser deletado especificando Cidade:{ver}')
print(d)
ver2 = d.popitem()
print(f'Ultimo Item a ser deletado "dicionario.popitem":{ver2}')
print(d)
print(50*'-')
print(f'Fazendo update no seu dicionário "dicionario.update(chave"Nome":chave, "idade":15,chave)"')
print(d)
#podemos acrescentar chaves ou simplesmente atualizar, alterar as existentes
d.update({'Cidade':'Itanhaem', 'idade':15,'Classe':'Terceiro ano'})
print(d)
print(f'Fazendo update no seu dicionário "dicionario.update(Cidade="Campinas", tamanho=15)"')
d.update(Cidade='Campinas', tamanho_sapato=17)
print(d)
print(50*'-')
print(f'Fazendo update em tuplas e listas dentro dos dicionarios de outra forma')
tupla = (('Matéria','Matemática'),('Nota1',9),('Nota2',8.5))
d.update(tupla)
lista = [['Matéria2','Português'],['Nota1',9.5],['Nota2',9.5]]
d.update(lista)
print(d)