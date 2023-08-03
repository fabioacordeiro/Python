# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
print(60*'-')
print(f'produto:',produto)
print(60*'-')
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'#Só vai incluir quando for verdadeira esta operação, ou seja, estou excluindo Categoria
}
print(f'dc:',dc)
print(60*'-')
dc2 = {
    chave: valor if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor
    in produto.items()
}
print(f'dc2:',dc2)
print(60*'-')


lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {2 ** i for i in range(10)}
print(f's1:',s1)
print(60*'-')
s1 = {2 ** i for i in range(10)}
print(set(range(10)))

