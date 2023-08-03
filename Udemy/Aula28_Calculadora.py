'''
Criar uma calculadora com while
onde o usuário informa 2 números e o operador
'''
Programa = "Calculadora"
operador = 0
print(50*'-')
print(f'{Programa:^50}')
print(50*'-')
while True:
    valor1 = input('Digite o primeiro número :')
    while True:
        if str.isalpha(valor1):
            print('Digite um número válido')
            break
        elif '.' in (valor1):
            valor = float(valor1)
            print(f'Valor validado float: {valor}')
            break
        else:
            valor = int(valor1)
            print(f'Valor validado int: {valor}')
            break
    while True:
        valor2 = input('Digite o segundo valor:')
        if str.isalpha(valor2):
            print('Digite o segundo valor válido')
        elif '.' in valor2:
             valor_2 = float(valor2)
             print(f'Valor 2 validado float: {valor_2}')
             break
        else:
            valor_2 = int(valor2)
            print(f'Valor 2 validado int: {valor_2}')
            break
    while operador not in (1,2,3,4):
        print('Digite o número do Operador a seguir:')
        print('[1] SOMAR')
        print('[2] DIVIDIR')
        print('[3] MULTIPLICAR')
        print('[4] SUBTRAIR')
        operador = int(input(':'))
        if operador == 1:
            print(f'A soma de {valor} e {valor_2} é: ({valor+valor_2}')
            operador = 0
            break
        elif operador == 2:
            print(f'A divisão de {valor} e {valor_2} é: ({valor/valor_2}')
            operador = 0
            break
        elif operador == 3:
            print(f'A multiplicacao de {valor} e {valor_2} é: ({valor*valor_2}')
            operador = 0
            break
        elif operador == 4:
            if valor >= valor_2:
                TT = valor - valor_2
            else:
                TT = valor_2 - valor
            print(f'A subtração {valor} e {valor_2} é: ({TT}')
            operador = 0
            break
        else:
            print('Digite um numero para o operador válido:')
    senha = input('Deseja sair [S] ou [N]').upper().lstrip()
    if senha == 'S':
        break
    '''    
    if not str.isnumeric(valor1):
    #if not str.isdigit(valor1) and not str.isdecimal(valor1):
        print('Digite um número válido')
    elif not str.isdigit(valor1):
        print('Digite um número válido')
    elif not str.isdecimal(valor1)
        print('Valor digitado não é decimal')
    else:
        break
'''
print(f'Valor 1 digitado:{valor1}')
print(f'Valor 2 digitado:{valor2}')
print(f'Obrigado por usar a calculadora Python do Fábio')
print(f'Volte sempre')