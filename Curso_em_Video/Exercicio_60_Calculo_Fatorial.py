from math import factorial
n = int(input('Digite um número par Cálculo Fatorial :'))
f = factorial(n)
print ('O cálculo fatorial de {} é {}'.format(n,f))
c = n
print ('Calculando {}! = '.format(n), end='')
while c>0:
    print ('{}'.format(c), end='')
    print(' x ' if c>1 else ' = ', end='')
    c = c-1
print('{}'.format(f))