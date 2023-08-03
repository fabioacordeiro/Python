#Calcule o preço de uma passagem de onibus com os critérios abaixo:
#0,50 para até 200km
#0,45 para para acima de 200km
D = float(input("Digite a distância da viagem para calcularmos o valor da Passagem :"))
if D >200.1:
    Vlr = (D*0.45)
    print('Para viagens de {} km o valor da passagem é de R$ {:.2f} '.format(D,Vlr))
else:
    Vlr = (D*0.50)
    print('Para viagens de {} km o valor da passagem é de R$ {:.2f}'.format(D,Vlr))