#Crie um programa que leia vários valores coloque em uma lista com a pergunta se deseja continuar ou não.
#Depois o programa cria mais duas listas auxiliares uma par e outra impar
#Mostre:
#O conteudo das 3 listas geradas separadamente a Geral, Par e Impar;
Geral = []
Par = []
Impar = []
valores = 'L'
Digitado = 0
while valores not in 'N':
    Digitado = int(input('Digite um valor :'))
    Geral.append(Digitado)
    valores = str(input('Quer continuar [S/N] ?:')).strip().upper()
for pos, valor in enumerate(Geral):
    if valor % 2 == 0:
        Par.insert(0,valor)
    else:
        Impar.insert(0,valor)
print(f'\033[7;30;41m Lista completa: {Geral}')
print(f'\033[7;30;42m A lista de números pares são: {Par}')
print(f'\033[7;30;46m A lista de números impares são: {Impar}')