#Faça um programa que tenha uma função chamada ficha(), que receba dois valores opcionais:
#O nome do jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
#mesmo que algum dado não seja informado corretamente:


def ficha(nome="desconhecido", gols=0):
    print(f'O jogador {nome} fez {gols} gols:')


#Programa Principal
nome = str(input('Digite o nome do Jogador :')).upper().strip()
gols = str(input('Digite a quantidade de gols que ele marcou:'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
