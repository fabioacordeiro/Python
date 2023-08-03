#Crie um pacote chamado UtilidadesCeV que tenha dois módulos internos moeda e dado.
#Transfira todas as funções utilizadas nos desafios 107,108 e 109 para o
#primeiro pacote e mantenha tudo funcionando.

from EX111.UtilidadesCeV import Moeda
vlr = float(input('Digite um preço: R$'))
a = float(input('Digite o % de aumento: '))
r = float(input('Digite o % de redução: '))
Moeda.resumo(vlr, a, r)
