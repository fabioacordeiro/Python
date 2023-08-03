import locale
loc = locale.getlocale()
locale.setlocale(locale.LC_MONETARY, 'pt_BR')
# para ver o valor local 'pt_BR'
#p2 = locale.currency(p)
#print(p2)

def vformatado(vlr):
    vlr = locale.currency(vlr)
    return vlr

def moeda(vlr=0,sifrao=R$):
    return f'{sifrao}{vlr:>8.:2f}'.replace('.',',')


def fatorial(n):
    f = 1
    for v in range(1, n+1):
        f = f * v
        f = locale.currency(f)
    return f


def dobro(a):
    v = 0
    v = a * 2
    v = locale.currency(v)
    return v


def triplo(b):
    vlr = 0
    vlr = vlr * 3
    vlr = locale.currency(vlr)
    return vlr


def metade(a):
    vlr = 0
    vlr = a / 2
    vlr = locale.currency(vlr)
    return vlr


def aumentar(a, num):
    vlr = 0
    vlr = num * (a/100)
    vlr = vlr + a
    vlr = locale.currency(vlr)
    return vlr


def diminuir(a, num):
    vlr = b = 0
    vlr = num * (a / 100)
    vlr = a - vlr
    vlr = locale.currency(vlr)
    return vlr
