#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(num=0,show=True):
    """
    :num: É o número a ser fatoriado
    :return: n! = n . (n – 1). (n – 2). (n – 3) ... 2,1. exemplo: 5! = 5 . 4 . 3 . 2 . 1 = 120 outro 4! = 4. 3 . 2 . 1 = 24
    """
    f = 1
    for v in range(num, 0, -1):
        f = f * v
     #   print(f'O valor fatorial de {f}')
    print(f'O valor fatorial de {num} é: {f}')


while True:
    valor = int(input('Digite um número para o seu fatorial :'))
    while True:
        show = int(input('Deseja visualizar o processo de cálculo fatorial ?'
                         '\n 1 = [Sim]'
                         '\n 2 = [Não]'
                         '\n Opção:'))
        if show == 1:
            fatorial(valor,show=True)
            help(fatorial)
            break
        elif show == 2:
            fatorial(valor)
            break
        else:
            print('Favor digitar somenete uma das opções 1 ou 2 :')
    if show == 1 or show == 2:
        break
