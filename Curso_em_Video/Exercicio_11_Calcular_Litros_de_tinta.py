#Sabendo que cada 1 litro de tinta pinta 2 metros quadrados de parede
#Vamos calcular a área da parede e litros de tinta necessários para pintar
comp = float(input ('Informe qual o comprimento :'))
Altura = float(input ('Informe qual a Altura:'))
Area = comp * Altura
print ('O total da área a ser pintada é de :', Area,'metros')
Litros = Area / 2
print ('Você vai precisar de',Litros,'Litros de tinta')
Balde = Litros / 18
Baldinho = Litros / 3.5
#print ('Equivale a %.2f:',Balde,'Baldes de 18 litros e a ', Baldinho,'Baldes de 3,5')
print ('Equivale a {:.2f} Baldes de 18 litros e a \n {:.2f} Baldes de 3,5' .format (Balde, Baldinho))