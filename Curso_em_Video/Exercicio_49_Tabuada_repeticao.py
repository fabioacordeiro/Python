#Refazer o exercicio 9 com laço de repetição
a = int(input('Digite um número para ver a Tabuada :'))
print ('\033[7;30;41m-'*20)
print (' TABUADA DO {} '.format(a))
print ('-'*20)
#cont = 0
for cont in range(1, 10):
    #Na segunda tentativa eu tinha feito o programa com as linhas de comentário, mas o python é sensacional
    #cont = cont + 1
    #result = result * a
    #print(' {} x {} = {}'.format(a, cont, result))
    print(' {} x {} = {}'.format(a, cont, a*cont))
print ('-'*20)