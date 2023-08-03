meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'}

#Acrescentar items
meu_dicionario[5] = 'Joaquina'
print(meu_dicionario)
#Acrescentar items com update
meu_dicionario.update({6: 'Pedro'})
print(meu_dicionario)

meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'}

#pop() Remover items
meu_dicionario.pop(2)
print(meu_dicionario)

meu_dicionario = {1 : 'Fabio', 2 : 'Maria', 3 : 'João', 4 : 'José'}

#len() Ver o tamanho do meu dicionário
print(len(meu_dicionario))

meu_dicionario.update({3: 'Marlene'})
print(meu_dicionario)

#aluno = {'Nome:':'Fabio', 'Nota1:': 9.5, 'Nota2:': 10.0,'Nome:':'Maria', 'Nota1:': 7.5, 'Nota2:': 6.0,'Nome:':'João', 'Nota1:': 7.5, 'Nota2:': 4.5, 'Nome:':'José', 'Nota1:': 8.5, 'Nota2:': 9.2, 'Nome:':'Ricardo', 'Nota1:': 8.5, 'Nota2:': 9.2}
#print(f'Print aluno:{aluno[0]}')
aluno = {}
aluno1 = {'Nome':'Fabio', 'Nota1': 9.5, 'Nota2': 10.0}
aluno2 = {'Nome':'Maria', 'Nota1': 7.5, 'Nota2': 6.0}
aluno3 = {'Nome':'João', 'Nota1': 7.5, 'Nota2': 4.5}

print(f'Print aluno vazio:{aluno}')
aluno.update({'Nome':'Fabio', 'Nota1': 9.5, 'Nota2': 10.0})
print(f'Print aluno novo:{aluno}')
aluno1.append(aluno.copy({'Nome':'Fabio', 'Nota1': 7.5, 'Nota2': 6.0}))
print(f'Print aluno novo1:{aluno}')
print(f'Print aluno1:{aluno1}')
print(f'Print aluno2:{aluno2}')

print(f'Print aluno3:{aluno.values()}')

def merge(aluno1,aluno2,aluno3):
    py={**aluno1,**aluno2,**aluno3}
    return py
aluno = (merge(aluno1, aluno2, aluno3))
print(f'Print aluno80:{aluno}')
'''
def merge(D1,D2):
    py={**D1,**D2}
    return py
D1 = {"loginID":"xyz","country":"USA"}
D2 = {"firstname":"justin","lastname":"lambert"}
D3 =(merge(D1,D2))
print(D3)
'''



dados = {'nome':'Lucas','idade':3,'nome':'Fabio','idade':46}
print(f'Print dados:{dados.keys()}')
for v in aluno.values():
    print(f'Print dados:{v}')