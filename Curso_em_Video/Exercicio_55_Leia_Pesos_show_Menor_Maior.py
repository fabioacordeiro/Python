maior = 0
menor = 0
for cont in range(1, 5):
    peso = float(input('\033[30;41m Digite o peso da {} pessoa :'.format(cont)))
    if cont == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido é de :{}'.format(maior))
print('O menor peso lido é de :{}'.format(menor))