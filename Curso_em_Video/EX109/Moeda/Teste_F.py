def moeda(vlr=0):
    return f'{vlr:>8.2f}'.replace('.', ',')


vlr = 100.45
print(moeda(vlr))



def dobro(a=0, formato=False):
    v = a * 2
    return v if formato is False else moeda(v)


def triplo(b=0, formato=False):
    vlr = b * 3
    return vlr if formato is False else moeda(vlr)


def metade(a=0, formato=False):
    vlr = a / 2
    return vlr if formato is False else moeda(vlr)


def aumentar(a=0, num=0, formato=False):
    vlr = num * (a/100)
    vlr = vlr + a
    return vlr if formato is False else moeda(vlr)


def diminuir(a, num, formato=False):
    vlr = num * (a / 100)
    vlr = a - vlr
    return vlr if formato is False else moeda(vlr)


