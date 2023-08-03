#Faça um programa que Leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Ex: 1834
#unidade:4
#Dezena:3
#Centena:8
#Milhar:1
#cont2=0
num = (int(input('Digite um número :')))
cont = str(num)
cont2 = len(cont)
if cont2 == 1:
    print('Unidade :{}'.format(cont[0]))
if cont2 == 2:
    print('Unidade :{}'.format(cont[0]))
    print('Dezena :{}'.format(cont[1]))
if cont2 == 3:
    print('Unidade :{}'.format(cont[0]))
    print('Dezena :{}'.format(cont[1]))
    print('Centena :{}'.format(cont[2]))
if cont2 == 4:
    print('Unidade :{}'.format(cont[0]))
    print('Dezena :{}'.format(cont[1]))
    print('Centena :{}'.format(cont[2]))
    print('Milhar :{}'.format(cont[3]))
#print(cont2)
print('Fim')