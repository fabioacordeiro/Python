#Faça um programa melhorando o exercicio 107 formatando os números para moeda:

from EX109 import Moeda

help(dobro())
p = float(input('Digite o preço:'))
print(f'A metade de {Moeda.moeda(p,"R$")} é : {Moeda.metade(p,True)}')
print(f'O dobro de {Moeda.moeda(p, "R$")} é {Moeda.dobro(p,True)}')
print(f'Aumentando 10%, temos {Moeda.aumentar(p,10,True)}')
print(f'Diminuindo 13%, temos {Moeda.diminuir(p,13,True)}')