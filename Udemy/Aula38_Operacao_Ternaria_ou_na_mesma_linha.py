'''
Operação ternária (condicional) de uma linha
<valor> if <condição> else <outro valor>
'''
print(f'Valor se Verdadeiro' if True else 'Outro Valor se Falso')
print(f'Valor se Verdadeiro' if False else 'Outro Valor se Falso')

A = 1
B = 20
print(f'Valor maior:A' if A > B else 'Valor maior: B')
condicao = A > B
variavel = 'Valor 1' if condicao else 'Valor 2'
print(variavel)
dig = 50
digito = dig if dig <= 9 else 0
print(f'Dígito vale:{digito}')
print('Valor1' if True else 'Valor2' if False else 'Valor3')
print('Valor1' if False else 'Valor2' if True else 'Valor3')
print('Valor1' if False else 'Valor2' if False else 'Valor3')