lista = []
for x in range(1,4):
    for y in range(1,4):
        lista.append((x, y))
print(lista)
print(50*'-')
lista = []

lista = [x
    for x in range(3)
    for y in range(3)
]
print(lista)
print(50*'-')

lista2 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista2)
print(50*'-')

lista3 = [
    (x, y, z)
    for x in range(3)
    for y in range(3)
    for z in range(3)
]
print(lista3)

print(50*'-')
lista4 = [[letra for letra in 'Luiz']
    for x in range(3)
]

print(lista4)

print(50*'-')
lista5 = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista5)