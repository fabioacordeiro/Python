'''
Usando o replace e expressão regular (Regular Expression)

'''
import re

valor_CPF = '167.055.018-47'
print(f'CPF: {valor_CPF}')
CPF = valor_CPF.replace('.','')
print(f'CPF: {CPF}')
CPF = valor_CPF.replace('-','')
print(f'CPF: {CPF}')
valor_CNPJ = '43.283.811/0066-03' 
print(f'CNPJ: {valor_CNPJ}')
cnpj = valor_CNPJ.replace('.','').replace('/','').replace('-','')
print(f'CNPJ: {cnpj}')
valor2 = '1-b_2-3ç4/o5+6[7]8...9'
print(f'Valor:{valor2}')
# substituir todos os valores de valor2 que não seja um número
# '0-9' => de 0 a 9
# '^' => que não seja um número
# '' => Substituir para nada, poderia ser '*' substituir para asterisco
valor = re.sub(r'[^0-9]','','1-b_2-3ç4/o5+6[7]8...9')
valor1 = re.sub(r'[^0-9]','',valor2)
print(f'Valor:{valor}')
print(f'Valor:{valor1}')