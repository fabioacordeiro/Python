n1 = int(input('Digite um número :'))
tot = 0
for cont in range(1, n1+1):
    if n1 % cont == 0:
        tot = (tot + 1)
        print('\033[34m', end='')
    else:
        print('\033[m', end='')
    print('{} '.format(cont), end='')
if tot == 2:
    print('\n O número {}, é primo'.format(n1))
else:
    print('\n O número {}, não é primo, ele foi divisível {} vezes'.format(n1,tot))