#Crie um programa que leia o valor de vários produtos e ele deve perguntar se o
#usuário quer continuar, no final de cada produto e mostre no final:
#Qual é o valor total de gastos na compra ?
#Quantos produtos custao mais de 1000 ?
#Qual o nome do produto mais barato;
ver = 'L'
nproduto = 'L'
Cont_valor = 0
soma = 0
Barato = 0
NBarato = ''
Qtsprodutocaros =0
mm = 0
while ver not in 'N':
    nproduto = 'L'
    nproduto = str(input('Qual o nome do produto ?:'))
    vlrproduto = float(input('Qual o valor do produto ? R$ :'))
    Cont_valor = Cont_valor +1
    soma = soma + vlrproduto
    if vlrproduto >= 1000:
        Qtsprodutocaros = Qtsprodutocaros + 1
    if Cont_valor == 1:
        NBarato = nproduto
        Barato = vlrproduto
    if vlrproduto < Barato:
        NBarato = nproduto
        Barato = vlrproduto
    ver = 'L'
    while ver not in 'SN':
        ver = str(input('Quer continuar [S/N]:')).strip().upper()[0]
print('O total da compra foi de R$ {:.2f}'.format(soma))
print('Temos {} produto custando mais de R$ 1000.00'.format(Qtsprodutocaros))
print('O produto mais barato foi {} que custa R$ {}'.format(NBarato, Barato))
