"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
Resto = 0
while True:
    num = input('Digite um número inteiro:')
    if '.' in num:
        print('Digite um número inteiro, sem ponto')
        print(type(num))
        print(num)
    elif ',' in num:
        print('Digite um número inteiro, sem vírgula')
        print(type(num))
        print(num)
    elif num in '0123456789':
        print('Número válido')
        print(num)
        break
    elif type(num) != int:
        print('Not OK')
        print(type(num))
        print(num)
    else:
        print(type(num))
        print(num)
print('Fim while')
Resto = (int(num)) % 2
if Resto >= 1:
    print('O número digitado é um número Ímpar')
else:
    print('O número digitado é um número par')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
while True:
    hora = int(input('Digite a hora:'))
    if hora >= 18:
        print('Boa Noite !!!')
        break
    elif hora >= 12 or hora <= 17:
        print('Boa tarde !!!')
        break
    elif hora >= 0 or hora <= 11:
        print('Bom dia !!!')
        break
    else:
        print('Digite um número válido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite o seu nome:')
cont = len(nome)
print(f'Qtde de letras do seu nome:{cont}')
if cont >=7:
    print('Seu nome é muito grande')
elif cont >= 5:
    print('Seu nome é normal')
else:
    print('Seu nome é curto')