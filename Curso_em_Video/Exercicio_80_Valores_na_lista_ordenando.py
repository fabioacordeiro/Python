#Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre como uma lista
#O programa deve colocar os números já na posicão crescente correta;
#mostre no final a lista em ordem na tela sem usar o comando sorter
valores = []
cont = 0
regra = 1

'''
valores4 = [8,2,2,4,7,2,1,3,5,9]
for posicao, valor in enumerate(valores4):
    print(f'Na posição {posicao} encontrei o valor {valor} !!')
print('Cheguei ao final da lista.')
print('='*50)
'''
while regra < 5:
#for v, valor in enumerate(valores):
    regra = regra + 1
    cont = cont+1
    Digitado = int(input(f'Digite um valor :'))
    if cont == 1:
        valores.append(Digitado)
        print(f'O valor {Digitado} foi inserido na posicao 0')
    elif cont == 2:
        if Digitado <= valores[0]:
            valores.insert(0,Digitado)
            print(f'O valor {Digitado} foi inserido na posicao 0')
        else:
            valores.append(Digitado)
            print(f'O valor {Digitado} foi inserido na posicao 1')
    elif cont ==3:
        if Digitado <= valores[0]:
            valores.insert(0,Digitado)
            print(f'O valor {Digitado} foi inserido na posicao 0')
        elif Digitado <= valores[1]:
            valores.insert(1,Digitado)
            print(f'O valor {Digitado} foi inserido na posicao 1')
        else:
            valores.insert(2,Digitado)
            print(f'O valor {Digitado} foi inserido na posicao 2')
    elif cont ==4:
        if Digitado <= valores[0]:
            valores.insert(0,Digitado)
            print(f'O valor {Digitado} foi inserido na posicao 0')
        elif Digitado <= valores[1]:
            valores.insert(1,Digitado)
            print(f'O valor {Digitado} foi inserido na posicao 1')
        elif Digitado <= valores[2]:
            valores.insert(2,Digitado)
            print(f'O valor {Digitado} foi inserido na posicao 2')
        else:
            valores.insert(3,Digitado)
            print(f'O valor {Digitado} foi inserido na posicao 3')
print(f'Lista : {valores}')

