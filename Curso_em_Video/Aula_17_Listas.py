#Aula listas
#A diferença entre tuplas e listas
# Tuplas são representadas por () parenteses => são imutáveis, não se pode mudar, alterar, acrescentar ou deletar itens;
# Listas são representadas por [] colchetes => são mutáveis, podemos fazer qualquer alteração
tuplas =('Hamburger', 'Suco', 'Pizza', 'Pudim')
listas = ['Hamburger', 'Suco', 'Pizza', 'Pudim']
print('Tupla {}'.format(tuplas))
print('Listas ',listas)
listas[3] = 'Sorvete'
print('Listas 2',listas)
listas.append('Feijoada')#incluir na ultima posição
print('Listas 3', listas)
listas.insert(0,'Banana')
listas.insert(7,8)
listas.insert(0,'Jabuticaba')
print('Listas 3', listas)
#Deletando os itens
del listas[3]
print('Listas 4', listas)
listas.pop(4)
print('Listas 5', listas)
listas.remove('Jabuticaba')
print('Listas 6', listas)
if 'Feijoada' in listas:
    listas.remove('Feijoada')
print('Listas 7', listas)
#criando novas listas com range
valores = list(range(4,21))
print('Nova lista valores:',valores)
valores1 = list(range(0,20,2))# Criar valores pulando de 2 em 2
print('Nova lista valores1:',valores1)
valores2 = list(range(0,20,5))# Criar valores pulando de 5 em 5
print('Nova lista valores2:',valores2)
valores3 = [8,2,2,4,7,2,1,3,5,9]
print('Nova lista valores3:',valores3)
valores3.sort()
print('Nova lista valores4:',valores3)
valores3.sort(reverse=True)
print('Nova lista valores5:',valores3)
print('Qtde Elementos em lista valores5 :',len(valores3))
valores3.remove(2)
valores3.remove(2)
print('Removendo o valor 2 :',(valores3))
print('Removendo o valor 5 :')
if 5 in valores3:
    valores3.remove(5)
else:
    print ('Não encontrei o número 5')
print(f'Essa lista tem {len(valores3)}:')
print('Removendo o valor 5 :',(valores3))
print('Criando nova lista usando o comando append()')
valores4 = []
valores4.append(5)
valores4.append(9)
valores4.append(4)
print('Imprimindo nova lista:', valores4)
print('='*50)
print(f'{"NOVA VISIUALIZAÇÃO":^40}')
print(f'{"Imprimindo nova lista usando o FOR:":.^50}')
print('='*50)
for posicao, valor in enumerate(valores4):
    print(f'Na posição {posicao} encontrei o valor {valor} !!')
print('Cheguei ao final da lista.')
print('='*50)

cont=0
valores10 = []
for cont in range(0,5):
    cont = cont + 1
    valores10.append(int(input('Digite o número {}º de 5 para criar uma lista :'.format(cont))))
print('Cheguei no final da lista digitada')
print(f'A lista é :{valores10}')
print('='*50)
#Importante a informação a seguir
#Criando uma lista a
a = [2,3,4,7]
b = a # Esse comando cria um vínculo entre as duas listas a e b, ou seja, qualquer alteração em b reflete em a e qualquer alteração em a reflete em b
print ('A lista A:', a)
print ('A lista B:', b)
print('='*50)
b[2] = 8 #Aqui estamos inserindo o valor 8 na posição 2 em b, na posição 2 temos o valor 4
print ('A lista A alterada:', a)
print ('A lista B alterada:', b)
print('='*50)
# Para criar uma nova lista sem o vínculo cria desta forma:
c = a[:]
print ('A lista A:', a)
print ('A lista C:', c)
print('='*50)
c[2] = 15 #Aqui estamos inserindo o valor 15 na posição 2 em b, na posição 2 temos o valor 8
print ('A lista A:', a)
print ('Somente a lista C alterada:', c)