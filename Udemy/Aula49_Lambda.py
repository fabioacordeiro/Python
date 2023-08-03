# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
# {'nome': 'Luiz', 'sobrenome': 'miranda'},
# {'nome': 'Maria', 'sobrenome': 'Oliveira'},
# {'nome': 'Daniel', 'sobrenome': 'Silva'},
# {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
# {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# classificado(lista)
lista  = [
    { 'nome' : 'Luiz' , 'sobrenome' : 'Miranda' },
    { 'nome' : 'Maria' , 'sobrenome' : 'Oliveira' },
    { 'nome' : 'Daniel' , 'sobrenome' : 'Silva' },
    { 'nome' : 'Eduardo' , 'sobrenome' : 'Moreira' },
    { 'nome' : 'Aline' , 'sobrenome' : 'Souza' },
]

# Ordenando a lista sem a lambda
def exibir(item):
    return item['nome']
    
print(f'Lista:{lista}')
print(60*'-')
lista.sort(key=exibir)
print(f'Lista Ordena:{lista}')

print(60*'-')
print('Listando os valores com For')
# Listando os valores com for
for num in lista:
    #print(num)
    for valor in num.values():
        print(valor, end=' ')
    print()


print(60*'-')
# Listando os valores com lambda
print(f'Listando os valores com lambda e sort():')
lista.sort(key=lambda item: item['nome'])
print(f'Lista ordenada com lambda :{lista}')
print(60*'-')

print(f'Listando os valores com lambda e sorted():')
sorted(lista, key=lambda item: item['nome'])
print(f'Lista ordenada com lambda :{lista}')
print(60*'-')

def mostrar(lista):
    for item in lista:
        print(item)
    print()



l1  =  sorted( lista, key=lambda  item : item ['nome'])
l2  =  sorted( lista, key=lambda  item : item ['sobrenome'])
print('Ordenada com lambda e função')
print(60*'-')
print('Ordenado pelo nome:')
mostrar ( l1 )
print(60*'-')
print('Ordenado pelo sobrenome:')
mostrar ( l2 )

print('Fazendo funções com lambda:')
#Fazendo funções com lambda
def soma(x,y):
    return x+y



def executa(funcao,*args):
    return funcao(*args)



print(executa(
    lambda x, y : x + y, 2,3
))

print('Fazendo funções sem lambda:')
print(executa(
    soma,2,3
))
print(60*'-')

def mostro_argumentos_nomeados(*args,**kwargs):
    print(f'ARGUMENTOS NAO NOMEADOS', args)
    for chave, valor in kwargs.items():
        print(f'Argumentos nomeados{chave, valor}')



mostro_argumentos_nomeados(1,2,nome='Joana',lpq=123)