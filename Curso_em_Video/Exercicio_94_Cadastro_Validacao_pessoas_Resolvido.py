#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
pessoa = {}
galera = list()
soma = media = 0
print('\033[7;30;41m='*50)
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome:')).strip().upper()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]:')).strip().upper()[0] #Sem espaços, tudo maiusculo e somente a primeira letra
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!!! Por favor, digite apenas M ou F:')
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    #print(f'Print pessoa: {pessoa}')
    galera.append(pessoa.copy())
    #print(f'Print galera: {galera}')
    while True:
            resp = str(input('Quer continuar [S/N]:')).strip().upper()[0]
            if resp in 'SN':
                break
            print('ERRO!!! Por favor, digite apenas S ou N:')
    if resp == 'N':
        break
media = (soma/len(galera))
print('='*50)
#print(galera)
print(f'A) Total temos {len(galera)} pessoas cadastradas')
print('B) A média de idade é de {:.2f} anos'.format(media))
print(f'C) As mulheres cadastradas foram:', end='')
for v in galera:
    if v["sexo"] in 'F':
        print(f'{v["Nome"]}, ', end='')
print(f'\nD) A lista das pessoas que estão acima da média:')
for v in galera:
    if v["idade"] >= media:
        print(f'    => {v["Nome"]} do sexo {v["sexo"]} com {v["idade"]}')