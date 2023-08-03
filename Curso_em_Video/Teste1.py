#import math
import math
from math import sqrt, pow
lista = ['Claudio', 35, 'M', 'Lucia', 53, 'F']
print(lista)
novo = 'M'
lista.append(novo)
print(lista)
#area = tt = altura = 0
a = 8
b = 5
c = 8
p = a+b+c
print(f'a+b+c:{p}')
tt = p*((p-a)*(p-b)*(p-c))
area = sqrt(tt)
print(f'Area com a formula de Heron é: {area}')
print(f'Outros forma ({b}x{c})/2 : {(b*c)/2}')
#Triangulo isósceles (2 lados iguais)
# Area é (base*altura)/2
# Teorema de Pithagoras
# Triangulo qualquer A=1/2bh (Onde A = Area, b = base e h = altura)
#Triangulo equilátero (3 lados iguais)
# Se h = a2+b2 Se h = hipotenusa que é igual a soma dos quadrados dos catetos, podemos cortar o triangula ao meio e
# ao fazer isso teremos um lado desconhecido o lado c onde será a altura e resolvemos com a formula a2+b2 = c (Onde c é a hipotenusa)
# A raiz de b será a altura:
#Vamos a prática
#Exemplo: triangulo a = b = c = 8
#cortando o triangulo ao meio fica assim na função:

'''[3 lados iguais]'''



def equilatero(a):
    t = a
    c = a
    c = c * c
    a = a/2
    a = a * a
    b = c - a
    b = b**(1/2) # Guanabara ensinou isso, outra forma de achar a raiz quadrada é elevar a 1/2 ou 0.5
    A = ((1/2)*t)*b
    print(f'O Triângulo Equilátero (3 lados iguais) a x b x c medindo {t} cm a base é {t} a Altura é de {b:.2f} e sua área é: {A:.2f}')
    #print(f'O Triângulo Equilátero raiz {raiz:.2f} área {ver:.2f} área2 {novo:.2f}')


equilatero(8)


F = (8*(math.sqrt(3)))

print(f'F:{F:.2f}')

'''[2 lados iguais] '''


def isosceles(a, b):
    if a == b:
        print("Este triângulo é equilátero, utilize a outra opção, ou informe os lados diferentes !!!")
    elif a < b:
        #a² = b² + h² (Onde a e b são os lados e h é a altura)
        t = a
        B = b
        Base = b / 2
        Base = Base * Base
        a = a * a
        d = a - Base
        h = (d ** (1/ 2))
        # A = (b * h)/2 (Onde A é a área, b é a base ou lado maior e h é a altura)
        A = (b * h)/2 # neste caso utilizamos 't' porque 'a' foi alterado no inicio;
        print(f'O Triângulo Isósceles (2 lados iguais) a:{t} x b:{t} x c:{B} e Altura {h:.2f} a área é de {A:.2f}')
    else:
        # a² = b² + h² (Onde a e b são os lados e h é a altura)
        t = b
        B = a
        Base = a / 2
        Base = Base * Base
        b = b * b
        d = b - Base
        h = (d ** (1 / 2))
        # A = (b * h)/2 (Onde A é a área, b é a base ou lado maior e h é a altura)
        A = (a * h) / 2  # neste caso utilizamos 't' porque 'a' foi alterado no inicio;
        print(f'O Triângulo Isósceles (2 lados iguais) a:{t} x b:{t} x c:{B} e Altura {h:.2f} a área é de {A:.2f}')



isosceles(30,22)

def escaleno(a, b, c):
        #Primeiro temos que verificar a possibilidade de existencia de um triângulo onde: a soma dos lados menores tem que ser maior que o lado que restou.
        if (a + b) > c:
            print('Sim, existe um triângulo, onde (a + b) > c')
        elif (a + c) > b:
            print('Sim, existe um triângulo, onde (a + c) > b')
        elif (b + c) > a:
            print('Sim, existe um triângulo, onde (b + c) > a')
        else:
            print('Não existe possibilidade de triângulo com estas dimensões')
        # P = a+b+c (Perímetro = P (Onde a e b e c são os lados)
        # SP = (a+b+c)/2 (Semi Perímetro = SP (Onde a e b e c são os lados)
        # A = √ SP*(SP-a)*(SP-b)*(SP-c)    => (Onde A = Área,  √ = Raiz quadrada, SP = Semi Perímetro, a,b,c são os lados)
        P = a + b + c
        SP = (a + b + c)/2
        D = SP*(SP-a)*(SP-b)*(SP-c)
        A = sqrt(D)
        print(f'O Triângulo Escaleno (3 lados diferentes) a:{a} x b:{b} x c:{c} o Perímetro é de {P} Semi Perímetro de {SP} a área é de {A:.2f}, \n '
              f'Lembrando que a área de Triângulo escaleno a fórmula é A = √ SP*(SP-a)*(SP-b)*(SP-c)    => (Onde A = Área,  √ = Raiz quadrada, SP = Semi Perímetro, a,b,c são os lados \n'
              f'e o resultado de uma raiz quadrada na maioria das vezes é semelhante a 12√5, então o número pode ser bem diferente mesmo')




escaleno(22, 4, 5)