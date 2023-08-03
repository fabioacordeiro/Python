soma = 0
cont = 0
print('\033[4;30;41m='*75)
for n in range(1, 501, 2): # Essa ultima opção ",2" pedi para o laço de repetição acontecer de 2 em 2
    if n % 3 == 0:
          soma = soma + n
          cont = cont + 1
     #     print(end= '\033[4;30;44m ')
    else:
         print(end='\033[4;30;44m')
    #sleep(0.5)
print( end='\033[4;30;41m A soma de todos {} valores solicitados é {}'.format(cont, soma))
print('      Programa Finalizou')
print('='*75)