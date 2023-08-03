#Crie um programa que leia vários valores com a pergunta se deseja continuar ou não.
#Mostre:
#Quantos números foram digitados;
#Ordenar a lista de forma decrescente;
#Se o valor 5 faz parte da lista e qual a posição;
cont = total = Digitado = 0
valores = []
while True:
    cont = cont+1
    Digitado = int(input('\033[7;30;42m Digite um valor :'))
    valores.append(Digitado)
    valor = str(input('\033[7;30;43m Deseja continuar [S/N] ? :')).strip().upper()
    if valor == 'N':
        break
if 5 in valores:
    print('\033[7;30;46m O valor 5 foi encontrado na lista')
else:
    print('\033[7;30;47m O valor 5 não foi encontrado na lista')
valores.sort(reverse=True)#Colocar na ordem inversa
print(f'\033[4;30;45m A lista em ordem decrescente é :{valores}')
print(f'\033[7;30;41m Foram digitados um total de {cont} números')
print(f'\033[7;30;41m Outra forma de trazer o total digitados {len(valores)} números')