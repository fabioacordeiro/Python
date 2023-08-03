#Desenvolva um programa de cálculo de IMC (ÌNDICE DE MASSA CORPÓREA) de acordo com as faixas abaixo
#Cálculo IMC = peso (em quilos) ÷ altura² (em metros)

#Baixo peso muito grave = abaixo de 16 kg/m².
#Baixo peso grave = entre 16 e 16,99 kg/m².
#Baixo peso = entre 17 e 18,49 kg/m².
#Peso normal = entre 18,50 e 24,99 kg/m².
#Sobrepeso = entre 25 e 29,99 kg/m².
#Obesidade grau I = entre 30 e 34,99 kg/m².
#Obesidade grau II = entre 35 e 39,99 kg/m².
#Obesidade grau III (obesidade mórbida) = maior que 40 kg/m².


peso = float(input('Qual o seu Peso ? (kg):'))
altura = float(input('Qual a sua Altura ? (m):'))
imc = peso/(altura ** 2)
i1 = 18.50*(altura ** 2)
i2 = 24.99*(altura ** 2)

print('\033[7;30;44m O seu IMC é de {:.2f} kg/m'.format(imc))
if imc < 16:
    print('\033[7;30;41m Você está com Baixo peso muito grave')
elif imc <= 16.99:
    print('\033[7;30;41m Você está com Baixo peso grave')
elif imc <= 18.49:
    print('\033[7;30;43m Você está com Baixo peso')
elif imc <= 24.99:
    print('\033[7;30;44m Você está com Peso normal')
elif imc < 29.99:
    print('\033[7;30;43m Você está com Sobrepeso')
elif imc < 34.99:
    print('\033[7;30;45m Você está com Obesidade grau I')
elif imc < 39.99:
    print('\033[7;30;41m Você está com Obesidade grau II')
else:
    print ('\033[7;30;41m Você está com Obesidade grau III (obesidade mórbida)')

if imc <= 18.49:
    p1 = i1-peso
    p2 = i2-peso
    print(' Você precisa ganhar entre {:.2f} e {:.2f}kg'.format(p1, p2))
elif imc >= 18.50 and imc <=24.99:
    p1 = i1 - peso
    p2 = i2 - peso
    print ('Você pode perder {:.2f} ou ganhar {:.2f}kg'.format(p1, p2))
else:
    p1 = i1 - peso
    p2 = i2 - peso
    print (' Precisa emagracer entre {:.2f} e {:.2f}kg'.format (p2, p1))

print ('\033[7;30;44m Para a sua altura o Peso ideal é entre {:.2f} e {:.2f}kg'.format(i1, i2))