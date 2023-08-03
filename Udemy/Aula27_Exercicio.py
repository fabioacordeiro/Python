
nome = 'Fabio Alves Cordeiro'
cont = 0
valor = 1
while cont <= valor:
    try:
        valor = len(nome)
        print(f'{nome[cont]}*',end='')
        cont = cont +1
    except:
        print('')
        break
print('Fim while')
