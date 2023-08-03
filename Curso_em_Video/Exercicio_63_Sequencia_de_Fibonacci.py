#Desenvolver um programa que faça a sequencia de Fibonacci
#A sequencia de Fibonacci sempre começa com 0 e 1, e o proximo numero soma-se os ultimos dois e acrescenta na sequencia
#0-1-1-2-3-5-8-13-21
print('-'*30)
print(' SEQUENCIA DE FIBONACCI ')
print('-'*30)
n = int(input('Quantos termos você quer mostrar ? :'))
t1 = 0
t2 = 1
print('~'*30)
print ('{}->{}'.format(t1,t2), end= '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('->{}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print (' Mostramos {} Termos'.format(n))