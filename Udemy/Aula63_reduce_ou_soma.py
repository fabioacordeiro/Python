from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]


# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']


print('Total com a função reduce simples é')
def funcao_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    return acumulador + produto['preco']
    

TT = reduce(
    funcao_reduce, 
    produtos,
    0 #Sempre passar o valor inicial zero para que o reduce consiga somar, caso contrario ele soma um dicionario com o valor e gera erro
    )

print(TT)

print(60*'-')

print('Total com a função reduce com Lambda é')
total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0 #Sempre passar o valor inicial zero para que o reduce consiga somar, caso contrario ele soma um dicionario com o valor e gera erro
)

print(total)

print(60*'-')
print('Total com for')
total = 0
for p in produtos:
    total += p['preco']

print(total)

print(60*'-')
print('Total com list compreension')
print(sum([p['preco'] for p in produtos]))