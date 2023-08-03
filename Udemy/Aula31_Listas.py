'''
Vamos criar e aprender a manipular as listas
'''
Lista = [10, 20, 30, 40, 50]
print(Lista)#Imprimindo a lista
print(Lista[1])#Visualizando o item 1 da lista lembrando que o primeiro numero esta no item zero
print(Lista[3])
del(Lista[1])#Deletando item 20 da lista
print(Lista[1])#Visualizando novamente o item 1 da lista lembrando que o primeiro numero esta no item zero
Lista[1] = 33 #Alterando o item 1 da lista de 30 para 33
print(Lista)
Lista.append(60)#Acrescentando itens no final da lista
Lista.append(70)#Acrescentando itens no final da lista
print(Lista)
Lista.pop()#Deletando o ultimo item da lista
print(Lista)
Lista.pop(0)#Deletando o item zero da lista
print(Lista)
Lista.insert(0,10)#Inserindo o número 10 no item zero da lista
print(Lista)
Lista.clear()#Limpar a lista
print(Lista)
A = [1,2,3]
B = [4,5,6]
C = A + B #Unindo os valores de 2 listas
print(C)
A.extend(B) #Extendendo os valores de A com os valores de B
print(A)
D = B.copy()#Copiando valores da Lista B para C
print(D)
# Imprimindo os valores da lista A
for valor in A:
    print(f'{valor} ',end='')
print()
print(50*'-')
E = ['Maria', 'João', 'Pedro']
cont = 0
for valor in E:
    print(f'{cont} {valor} ')
    cont +=1
print(50*'-')
print('Com o enumerate do for')

for valor in enumerate(E):
    print(valor)