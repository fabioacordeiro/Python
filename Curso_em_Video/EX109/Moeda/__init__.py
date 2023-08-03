def moeda(vlr=0, sifrao='R$'):
    """
    Função para formatação de número float para R$ (Real)
    :vlr: É o valor Float a ser transformado
    :sifrao: Informar 'R$' neste campo, ou não informe nada, o padrão já é o sifrão
    :return: Exemplo: Entrada 100.45 return R$ 100,45
    """
    return f'{sifrao}{vlr:>4.2f}'.replace('.', ',')


def dobro(a=0, formato=False):
    """
    Função para multiplicar o número por 2
    :Parâmetro a: É o valor a ser multiplicado
    :Parâmetro formato: Caso for informado "True" será formatado como moeda, senão retorna sem formatação.
    :return: Exemplo: Entrada 100.00 return R$ 200,00
    """
    v = a * 2
    return v if formato is False else moeda(v)


def triplo(b=0, formato=False):
    """
    Função para multiplicar o número por 3
    :Parâmetro b: É o valor a ser multiplicado
    :Parâmetro formato: Caso for informado "True" será formatado como moeda, senão retorna sem formatação.
    :return: Exemplo: Entrada 100.00 return R$ 300,00
    """
    vlr = b * 3
    return vlr if formato is False else moeda(vlr)


def metade(a=0, formato=False):
    """
    Função para dividir um valor pela metade
    :Parâmetro a: É o valor a ser dividido
    :Parâmetro formato: Caso for informado "True" será formatado como moeda, senão retorna sem formatação.
    :return: Exemplo: Entrada 100.00 return R$ 50,00
    """
    vlr = a / 2
    return vlr if formato is False else moeda(vlr)


def aumentar(a=0, num=0, formato=False):
    """
    Função para aumentar um número percentualmente
    :Parâmetro a: É o valor a ser aumentado
    :Parâmetro num: Valor percentual de aumento
    :Parâmetro formato: Caso for informado "True" será formatado como moeda, senão retorna sem formatação.
    :return: Exemplo: Entrada 100.00 e 10 return R$ 110,00
    """
    vlr = num * (a/100)
    vlr = vlr + a
    return vlr if formato is False else moeda(vlr)


def diminuir(a, num, formato=False):
    """
    Função para diminuir um número percentualmente
    :Parâmetro a: É o valor a ser diminuido
    :Parâmetro num: Valor percentual de redução
    :Parâmetro formato: Caso for informado "True" será formatado como moeda, senão retorna sem formatação.
    :return: Exemplo: Entrada 100.00 e 10 return R$ 90,00
    """
    vlr = num * (a / 100)
    vlr = a - vlr
    return vlr if formato is False else moeda(vlr)


