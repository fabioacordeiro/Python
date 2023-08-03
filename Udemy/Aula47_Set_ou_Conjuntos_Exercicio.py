'''
Usando o set
Muito eficiente para não incluir informações repetidas
'''

letras = set()

while True:
    digito = input('Digite uma letra: ').upper()
    letras.add(digito)
    print(letras)
    if digito not in 'L':
        continue
    else:
        print('Parabéns letra localizada !!!')
        break