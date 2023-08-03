#Aula de funções
#interactive Help
#docstrings
#argumentos opcionais
#Escopo de variáveies
#Retorno de resultados
#help(print)
##print(input)


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :i: início da contagem
    :f: fim de contagem
    :p: passo de contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f' {c}', end='')
        c += p
    print(' Fim !!!!')



def contador2(ini, fim, pas):
    """
    -> Faz uma contagem e mostra na tela.
    :i: início da contagem
    :f: fim de contagem
    :p: passo de contagem
    :return: sem retorno
    """

    for v in range(ini, fim, pas):
        print(f' {v}', end='')
        v = v + pas
    print(' Fim !!!!')


def somar(a=0, b=0, c=0): # Se caso o valor não for informado o valor padrao a ser executado será 0 e não dá erro
    soma = a+b+c
    print(f'A soma de a={a}, b={b} e c={c} é: {soma}')


def teste(n1, n2, n3):
    n1 = 10
    n2 = 20
    n3 = 30
    print(f'n1 dentro vale: {n1}')
    print(f'n2 dentro vale: {n2}')
    print(f'n3 dentro vale: {n3}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False



contador(0, 100, 10)
help(contador)
contador2(0, 100, 10)

somar(20)
somar(b=50, c=30)
teste(20, 20, 20)

n1 = 2
print(f'n1 fora vale: {n1}')

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

num = int(input('Digite um número, para ver se é par ou ímpar: '))
if par(num):
    print('É par ')
else:
    print('É ímpar')