n1 = int(input('Digite um número inteiro :'))
#binary = bin(n1)
#print (binary)
#temp = "{0:b}".format(5)
#print(temp)
print ('Escolha uma das bases para conversão:')
print ('[ 1 ] converter para BINÁRIO')
print ('[ 2 ] converter para OCTAL')
print ('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Digite sua opção :'))
if opcao == 1:
    result = "{0:b}".format(n1)
    print ('{} convertido para BINÁRIO é :{}'. format(n1,result))
elif opcao == 2:
    result = format(n1, "o")
    print('{} convertido para OCTAL é :{}'.format(n1, result))
elif opcao == 3:
    result = format(n1, "x")
    print ('{} convertido para HEXADECIMAL é:{}'.format(n1,result))
else:
    print('Desculpe, não temos esta opcao ainda disponível, favor contactar o desenvolvedor no \n Celular: (11)95456-7877, obrigado !!!!')

