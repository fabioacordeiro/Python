#Faça um programa melhorando o exercicio 107 formatando os números para moeda:

from EX108 import Moeda

p = float(input('Digite o preço:'))
print(f'A metade de {Moeda.vformatado(p)} é : {Moeda.metade(p)}')
print(f'O dobro de {Moeda.vformatado(p)} é {Moeda.dobro(p)}')
print(f'Aumentando 10%, temos {Moeda.aumentar(p,10)}')
print(f'Diminuindo 13%, temos {Moeda.diminuir(p,13)}')