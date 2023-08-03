#Faça um programa criando pacotes (Package), crie um pacote chamado moeda:
#

from EX107 import Moeda

p = float(input('Digite o preço:'))
print(f'A metade de {p} é : {Moeda.metade(p)}')
print(f'O dobro de {p} é {Moeda.dobro(p)}')
print(f'Aumentando 10%, temos {Moeda.aumentar(p,10)}')
print(f'Diminuindo 13%, temos {Moeda.diminuir(p,13)}')