#Faça um programa que leia o nome e a média e informe a situação.
boletim = []
nome = {}
nome['Nome:'] = str(input('Nome: ')).strip().upper()
nome['Media:'] = float(input(f'A Média de {nome["Nome:"]}: '))
if nome['Media:'] >= 7:
    print('Aprovado')
elif nome['Media:'] >= 5:
    print('Recuperação')
else:
    print('Reprovado')
for key, value in nome.items():
	print(f'{key}', value)
print('values',nome.values())
print('keys',nome.keys())
print('items',nome.items())