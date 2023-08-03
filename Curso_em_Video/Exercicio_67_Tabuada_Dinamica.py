#Faça um programa que mostre a tabuada de quantos números forem solicitados
# um de cada vez
# parar quando usuário digitar um número negativo
print('\033[7;30;41mTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')

print('  TTTTTTTTTTTT       TTTT       TTTTTTTTTTTT   TT        TT       TTTT       TTTTTTTTTTT       TTTT    ')
print('       TT           TT  TT      TT        TT   TT        TT      TT  TT      TT        TT     TT  TT   ')
print('       TT        TTT      TTT   TT        TT   TT        TT   TTT      TTT   TT        TT   TTT    TTT    ')
print('       TT        TTTTTTTTTTTT   TTTTTTTTTTT    TT        TT   TTTTTTTTTTTT   TT        TT   TTTTTTTTTTT    ')
print('       TT        TTTTTTTTTTTT   TTTTTTTTTTT    TT        TT   TTTTTTTTTTTT   TT        TT   TTTTTTTTTTT    ')
print('       TT        TT        TT   TT        TT   TT        TT   TT        TT   TT        TT   TT       TT ')
print('       TT        TT        TT   TT        TT   TT        TT   TT        TT   TT        TT   TT       TT    ')
print('       TT        TT        TT   TTTTTTTTTTTT   TTTTTTTTTTTT   TT        TT   TTTTTTTTTTT    TT       TT    ')

print('TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
cont = 0
while True:
    n = int(input('Digite um número para gerar a Tabuada [Valor negativo para parar] :'))
    if n < 0:
        break
    vlr = 0
    total = 0
    while vlr != 10:
        vlr = vlr +1
        total = vlr*n
        print('{} x {} = {}'.format(n, vlr,total))

    #lista = (lista & (',',n))
    #print (f'lista {n}')
print('Fim de programa')

