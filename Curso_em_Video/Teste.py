result = int(input('Par ou ímpar [P/I]:'))#Strip retirar espações e Upper para colocar em maiúscula [0] para considerar a primeira letra
if result == 3:

     print('par')
elif result % 2 == 0:

     print('Impar')
else:
    print('Erro')