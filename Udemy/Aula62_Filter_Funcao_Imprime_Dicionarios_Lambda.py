def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


def imprime_dicionarios(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def filtrar_preco(produto):
    return produto['preco'] > 100



def filtrar_preco_menor(produto):
    return produto['preco'] < 90



precos_baixos = filter(
    filtrar_preco_menor, produtos
)




print(60*'-')
print('Fazendo o filtro com o for')
novos_produtos = [
    p for p in produtos
    if p['preco'] > 100
    ]

print(novos_produtos)

print(60*'-')
produtos1 = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
novos_produtos1 = filter(
    lambda p: p['preco'] <= 20  ,
    produtos1
)

print('Fazendo o filtro com a filter, lambda e a função print_iter')
print_iter(novos_produtos1)

novos_produtos = filter(
    # lambda produto: produto['preco'] > 100,
    filtrar_preco,
    produtos
)

novos_produtos2 = filter(
    filtrar_preco_menor,
    produtos1
)


print(60*'-')
print('Lista de produtos')
print_iter(produtos)

print(60*'-')
print('Lista de novos produtos')
print_iter(novos_produtos)

print(60*'-')
print('Lista de precos_baixos')
print_iter(precos_baixos)

print(60*'-')
print('Função Imprime_dicionario e filtro com função filtrar_preco_menor')
imprime_dicionarios(novos_produtos2)