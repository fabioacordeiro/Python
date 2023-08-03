# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]
print(60*'-')
print('Imprimindo todos os itens e classes, verificando se type é set:')
for item in lista:
    print(item, isinstance(item, set))
    print(type(item))
    print('----------------')

print(60*'-')
print('Imprimindo todos os itens e somente se for set:')
for item in lista:
    if isinstance(item, set):
        print(item, isinstance(item, set))


print(60*'-')
for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item)

