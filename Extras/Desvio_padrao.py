import math

def calcularMedia(lista):
    soma = 0
    for valor in lista:
        soma += valor
        return float(soma/len(lista))


def calcularDesvioPadrao(lista):
    n = len(lista)
    m = calcularMedia(lista)
    soma = 0
    for valor in lista:
        soma = soma + math.pow(valor - m, 2)
        return math.sqrt((1/(n-1))*soma)



lista = [3,6,2,9,10,45,36,78,42,100]
print(calcularDesvioPadrao(lista))

