n1 = int(input("Digite um número qualquer para saber se é par ou ímpar :"))
Result = (n1 % 2)
if Result > 0:
    print ('O número {}, é um número ímpar'.format(n1))
else:
    print('O número {}, é um número Par'.format(n1))