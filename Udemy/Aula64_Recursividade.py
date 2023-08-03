'''
Funções recursivas ou loops
Vamos ver o fatorial como exemplo
Calcular o fatorial de um número é multiplicá-lo pelos seus 
antecessores maiores que zero.
Por exemplo, o fatorial do número 5 é 5!, que é a multiplicação de 5 
pelos seus antecessores, ou seja, 5⋅4⋅3⋅2⋅1
Onde: 5!=5x4x3x2x1= 120
O fatorial de um número é representado pelo número seguido de um 
ponto de exclamação, ou seja, n!.
vamos criar a função de fatorial
Esta função tem um limite também, exemplo fatorial de 1000 vai gerar erros
quando ultrapassado gera o erro: maximum recursion depth exceeded
mas para contornarmos isso podemos usar outras opções
importando o sys e definindo o limite
'''
import sys
sys.setrecursionlimit(1004)

def fatorial(n):
    #Removendo os números menores e iguais a 1:
    if n <= 1:
        return 1
    else:
        return n*fatorial(n-1)


print(60*'-')
print(fatorial(5))
print(60*'-')
print(fatorial(1000))
print(60*'-')