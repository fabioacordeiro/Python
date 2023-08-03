def fatorial(n):
    f = 1
    for v in range(1, n+1):
        f = f * v
    return f


def dobro(a):
    v = 0
    v = a * 2
    return v


def triplo(b):
    vlr = 0
    vlr = vlr * 3
    return vlr


def metade(a):
    vlr = 0
    vlr = a / 2
    return vlr


def aumentar(a, num):
    vlr = 0
    vlr = num * (a/100)
    vlr = vlr + a
    return vlr


def diminuir(a, num):
    vlr = b = 0
    vlr = num * (a / 100)
    vlr = a - vlr
    return vlr

