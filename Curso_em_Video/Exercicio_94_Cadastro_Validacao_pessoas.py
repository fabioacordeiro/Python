#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
media = idade = TT = Cont = vlr = 0
sexo = 1
Vidade = 2
pessoas = {}
mulheres = []
lista = list()
listaful = []
ver = ver1 = 'S'
while True:
    digitado = str(input('Nome:').strip().upper())
    lista.append(digitado)
    pessoas['Nome'] = digitado[:]
    #print(lista)
    while True:
        ver1 = str(input('Sexo [M/F]:').strip().upper())
        if ver1 in 'MF':
            if ver1 == 'M':
                lista.append(ver1)
                pessoas['Sexo'] = ver1[:]
                vlr = int(input('Idade:'))
                lista.append(vlr)
                pessoas['Idade'] = vlr
                TT = TT + vlr
                Cont = Cont+1
                digitado = 0
                break
            elif ver1 == 'F':
                lista.append(ver1)
                pessoas['Sexo'] = ver1[:]
                vlr = int(input('Idade:'))
                lista.append(vlr)
                pessoas['Idade'] = vlr
                mulheres.append(digitado)
                mulheres.append(ver1)
                mulheres.append(vlr)
                TT = TT + vlr
                Cont = Cont + 1
                digitado = 0
                break
        print('ERRO!!! Digite apenas M ou F:')
    listaful.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar [S/N] ?:')).strip().upper()[0]
        if resp in 'SN':
            break
        elif resp not in 'SN':
            print('ERRO!!! Digite apenas S ou N:')
    if resp in 'N':
        break
#print(f'Pessoas:{pessoas}')
#print(f'Lista full:{listaful}')
print('='*50)
media = (TT/Cont)
#print(mulheres)
#pessoas['Idade'] = int(input('Idade:'))
#print(lista)
print(f'A) Total temos {Cont} pessoas cadastradas')
print('B) A média de idade é de {:.2f} anos'.format(media))
print(f'C) As mulheres cadastradas foram:')
#print(f'Pessoas: {pessoas}')
''' O LOOPING ABAIXO SOMENTE COMENTADO TAMBÉM DÁ CERTO, PORÉM MOSTRA O NOME E IDADE
for pos, pes in enumerate(mulheres):
    if pos % 2 == 0:
        print(f'{pes}, ', end='')
print('')
'''
for pes in listaful:
    if pes["Sexo"] in 'F':
        print(f'{pes["Nome"]:^4},', end='')
print(f'\nD) A lista das pessoas que estão acima da média:')
for pes in listaful:
    if pes["Idade"] >= media:
        print(f'{pes}, ')
print()
