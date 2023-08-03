#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
#a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from EX113 import Moeda

n = Moeda.leiaint('Digite um número inteiro:')
n2 = Moeda.leiafloat('Digite um valor R$:')
print(f'O valor inteiro digitado foi :{n} e o valor monetário foi {n2}')