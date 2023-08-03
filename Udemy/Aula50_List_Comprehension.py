# Introdução à compreensão de lista em Python
# Lista de compreensão é uma forma rápida para criar listas
# a partir de iteráveis.
# print(lista(intervalo(10)))
list  = []

for numero in range(10):
    list.append(numero)
print(f'Print list:{list}')
'''
lista  = [
    numero  *  2
    para  numero  no  intervalo ( 10 )
]
imprimir ( lista )
'''
def imprimir(*args):
    print(*args)



lista  = [numero * 2 for numero in range(10)]
imprimir (f'Imprimindo lista:{lista}')
print(60*'-')
print('Listando produtos:')
produtos = [{'nome':'p1', 'preço':20},
{'nome':'p2', 'preço':17},
{'nome':'p3', 'preço':15},
{'nome':'p4', 'preço':30},
]

print(*produtos, sep='')
novos_produtos = [{**produto, 'preço':produto['preço']*1.05}
for produto in produtos]
print(60*'-')
print('Listando novos_produtos com 1.05% de aumento:')
print(*novos_produtos, sep='')

print(60*'-')
novos_produtos2 = [{**produto, 'preço':produto['preço']*1.05}
if produto['preço'] > 20 else {**produto}
for produto in produtos]
print(60*'-')
print('Listando novos_produtos2 somente maiores que 20 reais com 1.05% de aumento:')
print(*novos_produtos2, sep='')