#Sabendo que um carro custa R$ 60,00 por dia e R$ 0,15 centavos por km rodado faça o cálculo
Dia = int(input('Quantos dias de aluguel do carro ? :'))
km = int(input('Quantos quilometros rodados ?:'))
Dia = Dia*60
km = km*0.15
pago = Dia + km
print ('O valor do aluguel do carro é de {:.2f}'.format(pago))