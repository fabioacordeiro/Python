#gsfasfaf
n = 0
Result = 0
Cont = 0
n = int(input('Digite um número [9999 para parar] :'))
while n != 9999:
      Cont = Cont +1
      Result = Result + n
      n = int(input('Digite um número [9999 para parar] :'))
print('A soma é {}, você somou {} números'.format(Result,Cont))