# as duas formas de fazer importando a biblioteca inteira e importando somente a biblioteca necessária
'''
import math
Angulo = float(input('Digite um angulo qualquer :'))
Seno = math.sin(math.radians(Angulo))
print ('O ângulo de {} tem o seno de {:.2f}'.format(Angulo,Seno))
Cosseno = math.cos(math.radians(Angulo))
print ('O angulo de {} tem o Cosseno de {:.2f}'. format (Angulo,Cosseno))
Tangente = math.tan(math.radians(Angulo))
print ('O ângulo de {}, tem a tangente de {:.2f}'. format(Angulo,Tangente))
'''

from math import sin,cos,tan,radians
Angulo = float(input('Digite um angulo qualquer :'))
Seno = sin(radians(Angulo))
print ('O ângulo de {} tem o seno de {:.2f}'.format(Angulo,Seno))
Cosseno = cos(radians(Angulo))
print ('O angulo de {} tem o Cosseno de {:.2f}'. format (Angulo,Cosseno))
Tangente = tan(radians(Angulo))
print ('O ângulo de {}, tem a tangente de {:.2f}'. format(Angulo,Tangente))