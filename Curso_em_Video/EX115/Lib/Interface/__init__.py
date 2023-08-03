from EX113.Moeda import leiaint

def linha(tam=44):
    return '\033[36m=\033[m'*tam


def cabecalho(txt):
    print(linha())
    print(f'\033[4:30:45m',txt.center(42),'\033[m')
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[33m{c}\033[m=\033[34m{item}\033[m')
        c = c + 1
    print(linha())
    opc = int(input('Digite uma opção:'))
    return opc

