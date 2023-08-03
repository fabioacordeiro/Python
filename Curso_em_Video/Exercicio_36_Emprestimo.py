#Faça um progama que calcule se é possível o emprestimo para compra de imovel.
#Pergunte o valor do imóvel;
#Salario do comprador
#Tempo para pagamento do emprestimo
#O valor da prestacao não pode ser maior que 30% do salário ou então o emprestimo será negado;
imovel = float(input('Qual o valor do imóvel R$ :'))
salario = float(input('Qual o valor do salário ? R$:'))
salariofinal = salario*0.7882 # Calculei mais ou menos o que de fato recebemos em conta
# e não o salario registrado em carteira, trazendo mais proximo da realizadade financeira
# para não comprometer as prestações
Tempo = int(input('Qual o tempo de pagamento do empréstimo em anos ? :'))
prestacao = imovel / (Tempo*12)
if prestacao > (salariofinal*0.3):
    print('Financiamento negado')
    salario2 = str(salariofinal*0.3)
    print('O valor da prestacao precisa ficar abaixo de R$ {}'.format(salario2.replace('.',',',2)))
else:
    print('Valor de financiamento APROVADO !!! PARABÉNS, UM SONHO VAI SE REALIZAR !!!')
print('Para pagar uma casa de R$ {:.2f} em {} anos '.format(imovel,Tempo))
print('O valor da prestacao será de R$ {:.2f}'.format(prestacao))