a = (2,5,1,4)
b = (5,8,1,2,3,0)
c = a + b
d = a
lanche = ('Carne', 'Suco', 'Arroz', 'Feijoada', 'Pudim')

del(d)
#Comando para deletar uma tupla, a tupla não pode ser alterada,
# não podemos deletar membros da lista nem adicionar, mas podemos deletar a tupla inteira
print(f'Quantos números 5 aparecem na lista ?:', c.count(5))
print('Imprime a lista:',c)
print('Qual a posição do número 5 na lista ?:',c.index(5))
print('Lista em ordem',sorted(c))#Tupla foi colocada em ordem somente na visualização, mas não alterada na fonte.
print('Quantidade de itens da lista:',c.__len__())

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
print('Outra forma de fazer o laço:')
#Outra forma de fazer o laço
for cont in range (0,len(lanche)):
    print(f'Nós vamos comer {lanche[cont]}, na posicao {cont}')

for comida in lanche:
    print(f'Vocês vão comer {comida} ')
print('Fim do programa')