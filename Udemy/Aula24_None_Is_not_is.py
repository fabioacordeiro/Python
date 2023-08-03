'''
Usando o Dbug a Bandeira para demarcar os locais de parada
is
is not
None
'''
condicao = True
passou_no_if = None

if condicao:
    print('Passo 0')
    print(f'Id na memoria:{id(condicao)}')

if condicao:
    print('passo 1')
    passou_no_if = True
    print(f'condicao:{condicao}')
    print(f'passou_no_if:{passou_no_if}')
else:
    print('Passo 10')
print('Fim if')