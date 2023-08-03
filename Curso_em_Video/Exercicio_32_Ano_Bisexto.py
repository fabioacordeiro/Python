#No calendário gregoriano, um ano normal consiste em 365 dias.
# Como o comprimento real de um ano sideral (o tempo necessário para a Terra girar uma vez sobre o Sol)
# é na verdade de 365,2425 dias, um "ano bissexto" de 366 dias é usado uma vez a cada 4 anos para eliminar o erro
# causado por três anos normais (mas curtos). Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto:
# por exemplo, 1988, 1992 e 1996 são anos bissextos.
# Baseado nestas informações, faça um programa que leia o numero do ano e informe se é um ano bisexto
Ano = int(input('Digite o número para o programa calcular se é um ano Bisexto :'))
Bisexto = (Ano % 4)
print (Bisexto)
if Bisexto > 0:
    print('O ano de {}, não é um ano Bisexto'.format(Ano))
else:
    print('Sim, o ano de {} é um ano Bisexto'.format(Ano))