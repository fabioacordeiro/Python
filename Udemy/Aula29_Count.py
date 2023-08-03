'''
Vamos criar um programa que conte quantas
palavras ou letras tem em determinada frase
'''
Texto = 'O Python é uma linguagem de '\
    'Programação multiparadigma que foi criada '\
    'por Guido Van Rossum.'.upper()
# upper() para todas maiúsculas
# lower() para todas minúsculas
resp = 'S'
print(f'{Texto}')
while resp != 'N':
    print('Digite uma palavra ou letra para busca no texto acima.')
    busca = input(':').upper()
    print(f'Localizado: {Texto.count(busca)} vezes')
    while resp != 'N' or resp != 'S':
        resp = input ('Deseja fazer nova busca ? [S] sim ou [N] não :')[0].upper()
        if resp == 'N':
            break
        elif resp == 'S':
            print('OK, vamos continuar')
            break
        else:
            print('Digite somente [S] para Sim ou [N] para não:')
print('Obrigado por utilizar o sistema de busca Python')
print('Fim busca')


