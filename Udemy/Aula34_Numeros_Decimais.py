'''
Quando for trabalhar com uma precisão absurda de números decimais
podemos utilizar o recurso do python abaixo que é a função decimal,
porém 95% das vezes não precisamos de tamanha precisão e trabalhar com o 
arredondamento das casas decimais já é o suficiente com a função round
vamos ver os exemplos abaixo'''
import decimal
print('Somando 2 números A = 0.1 e B = 0.7 temos:')
A = 0.1
B = 0.7
C = A + B
print(C)
# Utilizando o round que tem menos precisão:
print(f'O Valor arredondado com "round" é:{(C)}')
print(f'O Valor arredondado com ":.f" é:{C:.2f}')
X = decimal.Decimal(A)
Y = decimal.Decimal(B)
Z = X+Y
print(f'Utilizando o arredondamento "Decimal" o valor é:{Z}')
print('Podemos também transformar "strings" em valores "decimais":')
X = decimal.Decimal('0.1')
Y = decimal.Decimal('0.7')
Z = X+Y
print(f'String transformada em Decimal o valor é:{Z}')
