#Faça um programa que calcule a área de um terreno:
#Lembrando que na solução do exercicio o programa terá que utilizar uma função para fazer isso.
from math import sqrt

def quadrado(a):
    ret = a * a
    print(f'\033[7;30;44m A área de um terrreno quadrado de {a} x {a} é de {ret}')


def retangulo(a, b):
    ret = a * b
    print(f'\033[7;30;44m A área de um terrreno retangular de {a} x {b} é de {ret}')


def equilatero(a):
    t = a
    c = a
    c = c * c
    a = a/2
    a = a * a
    b = c - a
    b = b**(1/2) # Guanabara ensinou isso também, outra forma de achar a raiz quadrada é elevar a 1/2 ou 0.5
    A = ((1/2)*t)*b
    print(f'\033[7;30;45m A área de um Triângulo Equilátero (3 lados iguais) a x b x c medindo {t} cm a base é {t} a Altura é de {b:.2f} e sua área é: {A:.2f}')


def isosceles(a, b):
    if a < b:
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
        print(f'\033[7;30;43m O Triângulo Isósceles (2 lados iguais) a:{t} x b:{t} x c:{B} e Altura {h:.2f} a área é de {A:.2f}')
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
        print(f'\033[7;30;43m O Triângulo Isósceles (2 lados iguais) a:{t} x b:{t} x c:{B} e Altura {h:.2f} a área é de {A:.2f}')


def escaleno(a, b, c):
        # P = a+b+c (Perímetro = P (Onde a e b e c são os lados)
        # SP = (a+b+c)/2 (Semi Perímetro = SP (Onde a e b e c são os lados)
        # A = √ SP*(SP-a)*(SP-b)*(SP-c)    => (Onde A = Área,  √ = Raiz quadrada, SP = Semi Perímetro, a,b,c são os lados)
        P = a + b + c
        SP = (a + b + c) / 2
        D = SP * (SP - a) * (SP - b) * (SP - c)
        A = sqrt(D)
        print(
            f'\033[7;30;46m O Triângulo Escaleno (3 lados diferentes) a:{a} x b:{b} x c:{c} o Perímetro é de {P} Semi Perímetro de {SP} a Área é de {A:.2f}, \n '
            f'Lembrando que a área de Triângulo escaleno a fórmula é A = √ SP*(SP-a)*(SP-b)*(SP-c) \n => (Onde A = Área,  √ = Raiz quadrada, SP = Semi Perímetro, a,b,c são os lados \n'
            f'a fórmula de perímetro é P = a+b+c e a fórmula de Semi Perímetro é SP = (a+b+c)/2')


area = 0
resp = 'L'

while True:
    area = int(input('\033[7;30;42m Informe a opção de cálculo da área desejada:\n [1] Quadrado \n [2] Retângulo \n [3] Triângulo Equilátero (3 lados iguais)'
                     '\n [4] Triângulo Isósceles (2 Lados iguais) \n [5] Triângulo Escaleno (3 lados diferentes) \n informe a opção:'))
    if area not in [1,2,3,4,5]:
        print('\033[4;30;41m ERRO !!! Digite somente uma das opções 1,2,3,4 ou 5 :')
    if area == 1:
        a = float(input('Informe o comprimento de um lado do terreno quadrado :'))
        quadrado(a)
    elif area == 2:
        a = float(input('Informe o Comprimento do terreno retangular :'))
        b = float(input('Informe o Largura do terreno retangular :'))
        retangulo(a, b)
    elif area == 3:
        a = float(input('Informe o Comprimento do lado do Triângulo equilátero :'))
        equilatero(a)
    elif area == 4:
        a = float(input('Informe o Comprimento do lado que se repete no Triangulo Isósceles:'))
        b = float(input('Informe o Comprimento do outro lado :'))
        if a == b:
            print("\033[4;30;41m Este triângulo é equilátero, utilize a opção 3, ou informe os lados diferentes !!!")
            break
        isosceles(a,b)
    elif area == 5:
        a = float(input('Informe o Comprimento do lado 1 do Triangulo Escaleno :'))
        b = float(input('Informe o Comprimento do lado 2 do Triangulo Escaleno :'))
        c = float(input('Informe o Comprimento do lado 3 do Triangulo Escaleno :'))
        # Primeiro temos que verificar a possibilidade de existencia de um triângulo onde: a soma dos lados menores tem que ser maior que o lado que restou.
        if a == b or a == c or b == c:
            print('\033[7:30:41m O Triangulo informado é Isósceles, use a opção [4] para estas dimensões')
        elif a > c and a > b and (c + b) > a:
            print('Sim, existe um triângulo, onde (c + b) > a onde este é o lado maior')
            escaleno(a, b, c)
        elif b > a and b > c and (a + c) > b:
            print('Sim, existe um triângulo, onde (a + c) > b onde este é o lado maior')
            escaleno(a, b, c)
        elif c > a and c > b and (a + b) > c:
            print('Sim, existe um triângulo, onde (a + b) > c onde este é o lado maior')
            escaleno(a, b, c)
        else:
            print('\033[7:30:41m Não existe possibilidade de triângulo com estas dimensões')
    while True:
        resp = str(input('Deseja continuar [S/N] ?:')).strip().upper()[0]
        if resp not in 'SN':
            print('\033[4;30;41m ERRO !!! Digite somente uma das opções S ou N :')
        if resp in 'SN':
            break
    if resp == 'N':
        break
    area = int(input(
        '\033[7;30;42m Informe a opção de cálculo da área desejada:\n [1] Quadrado \n [2] Retângulo \n [3] Triângulo Equilátero (3 lados iguais)'
        '\n [4] Triângulo Isósceles (2 Lados iguais) \n [5] Triângulo Escaleno (3 lados diferentes) \n informe a opção:'))
print('Programa ENCERRADO !!!')
