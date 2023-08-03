'''
Para validar um CPF devemos saber como funciona os números gerados do CPF
EXEMPLO: 
**********************************************
Cálculo do primeiro dígito do CPF
**********************************************
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.: 746.824.890-70 (746824890)
   10 9 8 7 6 5 4 3 2
* 7 4 6 8 2 4 8 9 0
   70 36 48 56 12 20 32 27 0
Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obtenha o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
'''
"""
***********************************************************
Cálculo do segundo dígito do CPF
***********************************************************
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.: 746.824.890-70 (7468248907)
   11 10 9 8 7 6 5 4 3 2
* 7 4 6 8 2 4 8 9 0 7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36 0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obtenha o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
import random

nomeprograma = 'Gerador de CPF'
print(50*'_')
print(f'{nomeprograma:^50}')
print(50*'_')
CPF = 0
CPFV = 0
listaCPF = []
listaCPF2 = []
listavalmult =[]
listavalmult2 =[]
valorDigitofinal = 0
valorDigitofinal2 = 0
cont = 10
cont2 = 11
cont3 = 0
valor = 0
valor2 = 0
D1 = 0
novedigitos = ''

for _ in range(100):
    cont3 +=1
    print(f'Qtde:{cont3}')
    for i in range(9):
        novedigitos += str(random.randint(0,9))
    #print(novedigitos)
    CPF = novedigitos
    for num in CPF:
        listaCPF.append(int(num))
    #print('Incluso na lista CPF')
    #print(listaCPF)
    # Calcular valor do dígito 1
    for num in listaCPF:
        if cont <= 1:
            cont = cont - 1
        else:
            listavalmult.append((num)*cont)
            cont-=1
    valor = ((sum(listavalmult)*10) % 11)
    valorDigitofinal = valor if valor < 9 else 0
    #Fim cálculo Dígito 1
    ###################################################
    # Calcular valor dígito 2
    #print(f'Lista CPF2:{listaCPF2}')
    for num in listaCPF:
        if cont2 <= 1:
            break
            cont2 = cont2 - 1
        else:
            if cont2 == 2:
                break
            listavalmult2.append((num)*cont2)
            cont2-=1
    #print(f'Lista multiplicada 2:{listavalmult2}')
    listavalmult2.append((int(valorDigitofinal))*2)
    #print(f'Lista multiplicada 2:{listavalmult2}')
    valor2 = ((sum(listavalmult2)*10) % 11)
    #print(f'Valor 2 fazer *10 / 11:{valor2}')
    valorDigitofinal2 = valor2 if valor2 < 9 else 0
    #print('Lista multiplicada')
    #print(f'Lista multiplicada 1:{listavalmult}')
    #print(f'Lista multiplicada 2:{listavalmult2}')
    #print(f'Valor Final dígito 1:{valorDigitofinal}') 
    #print(f'Valor Final dígito 2:{valorDigitofinal2}')
    CPFV = ((str(CPF[0:9]))+((str(valorDigitofinal))+(str(valorDigitofinal2))))
    print(f'CPF gerado:{CPFV}')
    listaCPF.clear()
    listaCPF2.clear()
    listavalmult.clear()
    listavalmult2.clear()
    valorDigitofinal = 0
    valorDigitofinal2 = 0
    novedigitos = ''
    cont = 10
    cont2 = 11
    #cont3 = 0
    valor = 0
    valor2 = 0
    #print(f'Valor CPF:{CPF}')
    '''
    if CPF == CPFV:
        print(f'\033[7;36m CPF OK, VÁLIDO\033[0;30m')
    else:
        print(f'\033[7;31m CPF INVÁLIDO\033[0;30m')
    break
    '''
print('\033[0;30mFim Validação')
print('\033[0;30m')


