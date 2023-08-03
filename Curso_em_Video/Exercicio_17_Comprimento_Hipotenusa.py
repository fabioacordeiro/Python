from math import hypot
co = float(input('Digite o valor do Cateto Oposto :'))
ca = float(input('Digite o valor do Cateto Adjacente :'))
h = hypot(co,ca)
print ('O valor da hipotenusa é de {:.2f}'.format(h))


