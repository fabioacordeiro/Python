#from time import sleep
for n in range(0, 50, 2): # Essa ultima opção ",2" pedi para o laço de repetição acontecer de 2 em 2
    result = (n % 2)
   #print('\033[4;30;41m .{}'.format(n))
    if result == 0:
          print(end='\033[4;30;44m {}'.format(n))
    else:
          print('')

    #sleep(0.5)
print('      Programa Finalizou')