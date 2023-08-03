#Nem sempre 3 retas são capazes de formar um triangulo este programa calcula se é possível
#Refazer exercicio 35 e colocar as informações de Tipos de triângulo:
#Equilátero = Todos os lados iguais
#Isósceles = 2 lados iguais
#Escaleno = Todos os lados diferentes
print('       . ')
print('       |\ ')
print('       | \ ')
print('       |  \ ')
print('Lado a |   \ ')
print('       |    \ ')
print('       |     \  lado b ')
print('       |      \ ')
print('       |       \ ')
print('       |        \ ')
print('       |         \ ')
print('       |          \ ')
print('       |           \ ')
print('       |____________\ ')
print('          lado c ')
n1 = float(input('Digite o valor do lado a :'))
n2 = float(input('Digite o valor do lado b :'))
n3 = float(input('Digite o valor do lado c :'))
if n1 >= n2 and n1 >= n3 and n1<(n2+n3):
    print ('\033[7;30;44m Sim, as dimensões de abc formam um triângulo',end='')
    if n1 == n2 and n1 == n3:
        print('\033[7;30;44m : EQUILÁTERO (3 lados iguais)')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('\033[7;30;44m : ESCALENO (Os 3 lados diferentes)')
    else:
        print('\033[7;30;44m : ISÓSCELES (2 lados iguais)')
elif n2>=n1 and n2>= n3 and n2<(n1+n3):
    print ('\033[7;30;44m Sim, as dimensões de abc formam um triângulo' ,end='')
    if n1 == n2 and n1 == n3:
        print('\033[7;30;44m : EQUILÁTERO (3 lados iguais)')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('\033[7;30;44m : ESCALENO (Os 3 lados diferentes)')
    else:
        print('\033[7;30;44m : ISÓSCELES (2 lados iguais)')
elif n3>n1 and n3>n2 and n3<(n1+n2):
    print ('\033[7;30;44m Sim, as dimensões de abc formam um triângulo',end='')
    if n1 == n2 and n1 == n3:
        print('\033[7;30;44m : EQUILÁTERO (3 lados iguais)')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('\033[7;30;44m : ESCALENO (Os 3 lados diferentes)')
    else:
        print('\033[7;30;44m : ISÓSCELES (2 lados iguais)')
else:
    print('\033[7;30;41m Não as dimensões informadas de abc, não formam um triângulo')

print('Lado a:{}'.format(n1))
print ('Lado b:{}'.format(n2))
print('Lado c:{}'.format(n3))