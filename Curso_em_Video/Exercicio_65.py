#Faça um programa onde ele leia um número ou vários, no final informe:
# a média
# o número menor
# o número maior
# o total de números digitados.

total = soma = media = menor = maior = vlr = 0
n = 'S'
while n not in 'Nn':
    vlr = int(input('Digite um número :'))
    total = total + 1
    soma = soma + vlr
    if total ==1:
        menor = vlr
        maior = vlr
    if vlr < menor:
        menor = vlr
    if vlr > maior:
        maior = vlr
    p = str(input('Quer continuar ? [S/N]:')).strip().upper()[0]
    n = p
print('Você digitou {} números'.format(total))
print ('A média foi de :{}'.format(soma/total))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))


