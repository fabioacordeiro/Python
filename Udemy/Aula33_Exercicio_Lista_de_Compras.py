'''
Crie um programa que faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar
valores da sua lista
Não permita que o programa quebre com valores de indices
inexistentes de sua lista.
'''
import os
lista = []
nome = 'LISTA DE COMPRAS'
saudacao = 'BEM VINDO AO PROGRAMA'
s = 'S'
ver = 'S'
Sair = 'N'
print(50*'-')
print(f'{saudacao:^50}')
print(f'{nome:^50}')
print(50*'-')
while True:
    print('O que deseja fazer com Produtos ?')
    print('[I] Inserir')
    print('[A] Apagar')
    print('[L] Listar')
    acao = input(':')[0].upper()
    if acao == 'I':
        s == 'S'
        while s == 'S':
            produtos = lista.append(input('Informe o nome do produto:').upper())
            print('Deseja inserir mais produtos ?')
            print('[S] sim [N] nao')
            s = input(':')[0].upper()
        print(lista)
    elif acao == 'A':
        ver = 'N'
        if len(lista) == 0:
            print('Sua lista está vazia')
        else:
            print()
        print('Informe o número do indice do produto a ser apagado:')
        print('Índice Produto')
        for l in enumerate(lista):
            print(l)
        while True:
            d = int(input('Digite o numero do índice:'))
            print('Índice Produto')
            if d <= (len(lista)):
                del(lista[d])
            elif d > (len(lista)):
                print(f'Último índice da lista é: {len(lista)-1}')
                print('Esse produto não existe, digite um índice válido.')
                for l in enumerate(lista):
                    print(l)
            print('Deseja deletar outro item ?')
            print('[S] sim ou [N] não')
            print(f'Último índice da lista é: {len(lista)-1}')
            ver = input(':')[0].upper()
            if ver == 'N':
                break            
    elif acao == 'L':
        if len(lista) == 0:
            print('Sua lista está vazia')
        else:
            os.system('cls')
            print(f'Sua lista tem {len(lista)} produtos:')
            for produto in lista:
                print(produto)
            print()
    print('Deseja sair do programa')
    print('[S] sim ou [N] nao')
    Sair = input(':')[0].upper()
    if Sair == 'S':
        break
print("Volte sempre")
