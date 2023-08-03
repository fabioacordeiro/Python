vlr = 0
resultado = 0
for soma in range (1,7):
   # print('Contador:{}'.format(soma))
    result = int(input('\033[7;30;41m digite o valor do número {} :'.format(soma)))
  #  print('vlr:{}'.format(vlr))
    if result % 2 == 0:
    #     print('result:{}'.format(result))
         resultado = result
         vlr= (vlr + resultado)
    else:
        print(end='')
print('O valor da soma dos números pares é {}'.format(vlr))
