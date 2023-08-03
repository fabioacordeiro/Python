'''
Vamos dar inicio ao conteúdo de funções
definindo uma função no python
'''

def nomeapp(text):
    print(50*'-')
    print(f'{(text.upper()):^50}')
    print(50*'-')

def nomemin(text):
    print(50*'-')
    print(f'{text:^50}')
    print(50*'-')


nomeapp('Novas Funções')

nomeapp('Novos Tempos')


nomemin('Teste de Novas Funções')


def somando(a=None,b=None,c=0):
    print(f'A soma de {a} , {b} e {c} é: {(a+b+c)}')



somando(500, 45, 50)

somando(345, 378)

#Definindo uma função com vários argumentos (tuplas)
def somar(*args):
    TT = 0
    for num in args:
        TT = (TT + (int(num)))
    return print(f'O resultado de somar é:{TT}')



somar(400, 500, 660, 3.5, 789)


#Exercício crie uma função para multiplicar
#Vários números e trate se caso o usuário digitou 0

def multiplicar(*args):
    TT=1
    for num in args:
        if num == 0:
            continue
        elif num != 0:
            TT = TT * num
    return print(f'O resultado de multiplicar é:{TT}')


multiplicar(2, 4, 6, 7, 8, 9, 3.5 )
print(2* 4* 6* 7* 8 *9 * 3.5)

#Crie uma função que retorne se o número é par ou ímpar

def par_impar(a):
    if a % 2 == 0:
        return print('É par')
    return print('É impar')
    #repare que não precisamos do else aqui, poderíamos
    #inserir sem problema, mas seria redundante



par_impar(60)
