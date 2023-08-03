# Faça uma função onde melhoramos o exercicio 109 para trazer os mesmos valores.
# Porém com 5 linhas de código e com os valores em formato mais organizado e resumido:
# Onde digitados o número o percentual de aumento e em seguida a redução.

from EX110 import Moeda
vlr = float(input('Digite um preço: R$'))
a = float(input('Digite o % de aumento: '))
r = float(input('Digite o % de redução: '))
Moeda.resumo(vlr, a, r)