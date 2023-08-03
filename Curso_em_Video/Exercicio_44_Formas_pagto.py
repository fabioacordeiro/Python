#De acordo com as condições de pagamento faça um programa analisando o valor do produto
#A vista dinheiro/cheque = 10% desconto
#A vista Cartão = 5% Desconto
#Parcelado 2x = Normal sem desconto
#Parcelado 3x = Juros 20%
print ('{:=^40}'.format(' LOJAS CORDEIRO '))
preço = float(input('Preço das compras :R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista (Dinheiro / CHEQUE)
[ 2 ] á vista no Cartão (CRÉDITO/DÉBITO)
[ 3 ] Parcelamento 2 X (CRÉDITO)
[ 4 ] Parcelamento + 3X (CRÉDITO)
''')
formas = int(input('Opção :'))
if formas == 1:
    preco1 = (preço*0.9)
    print ('\033[7;30;44m O Valor do produto é de R$ {} pagto á vista (Dinheiro / CHEQUE) 10 % de desconto total da compra é de R$ {}'.format(preço, preco1))
elif formas == 2:
    preco1 = (preço*0.95)
    print('\033[7;30;44m O Valor do produto é de R$ {:.2f} pagto á vista no Cartão 5% de desconto o total da compra é de R$ {:.2f}'.format(preço, preco1))
elif formas == 3:
    print ('\033[4;30;43m O Valor do produto é de R$ {:.2f} pagto Parcelado sem desconto'.format(preço))
elif formas == 4:
    preco1 = (preço*1.2)
    print('\033[7;30;41m O Valor do produto é de R$ {:.2f} pagto Parcelamento + 3X com acréscimo de 20% o valor da compra é de R$ {:.2f}'.format(preço, preco1))
else:
    print('Prezado cliente, esta opção ainda não está disponível, Obrigado pela PREFERÊNCIA !!!')
    print ('\033[4;30;43m O Valor do produto é de R$ {:.2f} sem desconto'.format(preço))