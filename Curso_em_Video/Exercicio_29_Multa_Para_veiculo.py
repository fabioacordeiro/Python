from random import choice
V = [40,45,50,60,70,80,85,90,95,100,110,120,130,140,150,200]
Velocidade = choice(V)
if Velocidade >= 81:
    Multa = (Velocidade - 80)*7
    'P = 1-(Velocidade/80)'
    P =((Velocidade * 100) / 80) - 100
    print ('Já que a velocidade foi {}% superior ao permitido, \n onde a velocidade apurada foi de {}km/h \n '
           'o valor da multa a ser paga é de R$ {:.2f}' .format(P,Velocidade,Multa))
else:
    print ('Parabéns continue andando dentro dos limites de velocidades permitidos pela via. \n a velocidade apurada foi de {}'.format(Velocidade))

