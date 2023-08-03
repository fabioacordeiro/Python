#from emoji import emojize
#Faça um programa que simule o funcionamento de um caixa eletronico:
#Perguntar qual o valor do saque, número inteiro;
#Programa vai informar quantas cédulas de cada valor serão entregues;
#Considere que o caixa possui cédulas de:
# R$ 50,00
# R$ 20,00
# R$ 10,00
# R$  1,00
#print(emoji.emojize("Oi : earth_americas", use_aliases=True))
Qtd50 = Res50 = Qtd20 = Res20 = Qtd10 = Res10 = Qtd1 = Res1 = 0
print ('\033[7;30;44m=======================================================')
print ('                BANCO FAC         ')
print ('=======================================================')
Vlr = int(input('\033[7;30;44m Qual o valor do Saque ? R$'))
Qtd50 = Vlr // 50
Res50 = Vlr % 50
Qtd20 = Res50 // 20
Res20 = Res50 % 20
Qtd10 = Res20 // 10
Res10 = Res20 % 10
Qtd1 = Res10 // 1
Res1 = Res10 % 1
if Qtd50 > 0:
    print('Total de {} cédulas de R$ 50,00'.format(Qtd50))
if Qtd20 > 0:
    print('Total de {} cédulas de R$ 20,00'.format(Qtd20))
if Qtd10 > 0:
    print('Total de {} cédulas de R$ 10,00'.format(Qtd10))
if Qtd1 > 0:
     print('Total de {} cédulas de R$ 1,00'.format(Qtd1))
print('Volte sempre ao Banco do FAC! Tenha um ótimo dia')