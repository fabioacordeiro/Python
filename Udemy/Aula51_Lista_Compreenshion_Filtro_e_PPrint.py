# Introdução à compreensão de lista em Python
# Lista de compreensão é uma forma rápida para criar listas
# a partir de iteráveis.
# print(lista(intervalo(10)))
import pprint

def p(v):
    pprint.pprint(v,sort_dicts=False, width=40)


print(60*'-')
lista  = []
for numero in range(10):
    lista.append(numero)
print(lista)

lista  = [
    numero*2
    for numero in range(10)
]
# print(lista(intervalo(10)))
# print(lista)

# Mapeamento de dados em compreensão de lista
produtos  = [
    { 'nome' : 'p1' , 'preco' : 20 , },
    { 'nome' : 'p2' , 'preco' : 10 , },
    { 'nome' : 'p3' , 'preco' : 30 , },
]
novos_produtos  = [
    { ** produto ,'preco': produto['preco'] * 1.05}
    if  produto['preco'] > 20 else {** produto}
    for produto in produtos
]
print(60*'-')
# # print(novos_produtos)
# print(novos_produtos)
#p(novos_produtos)
# lista = [n para n no intervalo(10) se n < 5]
novos_produtos  = [
    { ** produto ,'preco': produto['preco'] * 1.05 }
    if  produto ['preco'] > 20 else {** produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05 ) > 10
]
p(novos_produtos)
print(60*'-')

lista2  = [numero for numero in range(10) if numero < 5]

print(f'Lista2:{lista2}')
print(60*'-')

# os parametros a esquerda do For é mapeamento o que vem a direita é filtro
novos_produtos2  = [
    { ** produto ,'preco': produto['preco'] * 1.05 }
    # Mapeamento
    if  produto ['preco'] > 20 else {** produto}
    for produto in produtos
    # Filtro
    if (produto['preco'] >= 20 and produto['preco'] * 1.05 ) > 10
]
p(novos_produtos2)