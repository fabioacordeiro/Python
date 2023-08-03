#Aula 18 - listas dentro de listas
#Formas de criar uma lista
frutas = []
sucos = list()
dados = []
pessoas = list()
dados1 = ['Lucas',3]
dados2 = ['Fabio',46]
dados3 = ['Luciene',44]
print(f'Lista dados3 {dados3}')
#Criando listas dentro de listas
pessoas = [['Lucas',3],['Fabio',46],['Luciene',44],['Princila', 20],['Tatiane', 24]]
print(f'Lista pessoas {pessoas}')
print(f'Print pessoas [0][0:2] {pessoas[0][0:2]}')
print(f'Print pessoas [1][1] {pessoas[1][1]}')
print(f'Print pessoas [2][0] {pessoas[2][0]}')
print(f'Print pessoas [1] {pessoas[1]}')
print(f'Print pessoas [:6][1] {pessoas[0:6][1]}')
print(f'='*60)
print(f'{"Estrutura de repetição FOR":^60}')
print(f'='*60)
for cadaposicao in pessoas:
    print(f'Posicão:{cadaposicao}')
    print(f'Posicão:{cadaposicao[0]}')
    print(f'Posicão:{cadaposicao[1]}')
print(f'='*60)
print(f'{"INSERINDO DADOS COM FOR":^60}')
print(f'='*60)
copiapessoas = []
for c in range(0,3):
    copiapessoas.append(str(input('Nome :')).strip().upper())
    copiapessoas.append(int(input('Idade:')))
    pessoas.append(copiapessoas[:])
    copiapessoas.clear()
print(f'=' * 60)
print(f'Print copiapessoas:{copiapessoas}')
print(f'Print pessoas:{pessoas}')
print(f'='*60)
print(f'{"VISUALIZANDO NOMES E IDADES COM FOR":^60}')
print(f'='*60)
maior = menor = 0
for cadaposicao in pessoas:
    if cadaposicao[1] >=21:
        print(f'O {cadaposicao[0]} tem {cadaposicao[1]} anos, é maior de idade')
        maior = maior +1
    else:
        print(f'O {cadaposicao[0]} tem {cadaposicao[1]} anos, é menor de idade')
        menor = menor +1
print(f'='*60)
print(f'Temos {maior} maiores e {menor} menores de idade')
