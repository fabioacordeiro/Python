#Crie um pacote chamado UtilidadesCeV que tenha dois módulos internos moeda e dado.
#Transfira todas as funções utilizadas nos desafios 111 e valide o valor digitado para dinheiro
# #primeiro pacote e mantenha tudo funcionando.

from EX112.UtilidadesCeV import Moeda
from EX112.UtilidadesCeV import Dado

vlr = Dado.leiaDin('Digite um preço R$:')
#vlr = float(input('Digite um preço: R$'))
#a = float(input('Digite o % de aumento: '))
#r = float(input('Digite o % de redução: '))
Moeda.resumo(vlr, 12, 20)