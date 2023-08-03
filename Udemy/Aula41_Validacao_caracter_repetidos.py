'''
Tem usuário que quer trolar o desenvolvedor
Vamos identificar se o usuário está digitando caracteres respetidos
importando o método sys que sai do Python
'''
import sys
valor = input('Digitar o número de CPF:')
print(f'CPF digitado:{valor}')
primeiro_caracter = valor[0] 
entrada_repetida = primeiro_caracter * (len(valor))
print(f'Primeiro caracter:{primeiro_caracter}')
if valor == entrada_repetida:
    print(f'Você digitou números repetidos')
    sys.exit()
else:
    print(f'Valores digitados: {valor} diferentes de repetidos {entrada_repetida}')
print('Fim programa')