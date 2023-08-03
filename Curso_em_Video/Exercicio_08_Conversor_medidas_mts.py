#Faça um programa que converta metros em:
#km, hm, dam, dm, cm, mm
m = float(input('Uma distância em metros :'))
print('{}km'.format(m/1000))
print('{}hm'.format(m/100))
print('{}dam'.format(m/10))
print('{}dm'.format(m*10))
print('{}cm'.format(m*100))
print('{}mm'.format(m*1000))