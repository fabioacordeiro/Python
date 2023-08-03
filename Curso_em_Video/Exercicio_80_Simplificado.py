#Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre como uma lista
#O programa deve colocar os números já na posicão crescente correta;
#mostre no final a lista em ordem na tela sem usar o comando sorter
valores = []
pos = 0
for cont in range(0,5):
    Digitado = int(input(f'Digite um valor :'))
    if cont == 0:
        valores.append(Digitado)
        print(f'Adicionado no final da Lista')
    elif Digitado > valores[-1]:
        valores.append(Digitado)
        print(f'Adicionado no final da Lista')
    else:
        while pos < len(valores):
            if Digitado <= valores[pos]:
                valores.insert(pos,Digitado)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos = pos+1
print(f'Lista : {valores}')
