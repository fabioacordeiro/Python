n1 = int(input('Digite o primeiro número :'))
n2 = int(input('Digite o segundo número :'))
n3 = int(input('Digite o terceiro número :'))
if n1 > n2 and n1>n3:
    print ('O número maior é {}.'.format(n1))
elif n2 > n1 and n2>n3:
    print ('O número maior é {}.'.format(n2))
else:
    print ('O maior número é {}.'.format(n3))

if n1 < n2 and n1<n3:
    print ('O número menor é {}.'.format(n1))
elif n2<n1 and n2<n3:
    print ('O menor número é {}.'.format(n2))
else:
    print ('O número menor é {}.'.format(n3))