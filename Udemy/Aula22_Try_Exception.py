'''
Vamos utilizar o try exception que é executar um código
até a ultima linha sem erro e informa o erro
'''
'''
numero = input(
"Digite um número qualquer que retornarei o seu dobro: "
)
try:
    print(f'O número digitado foi : {numero}')
    numero_float = float(numero)
    print(f'O dobro de {numero} é {numero_float * 2}')
except:
    print(f"'{numero}' Não é um número válido.")
'''


####################################################################################
#Podemos ter várias except, por exemplo
try:
    a = 18
    b = 0
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Nome b não está definido')
except(TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('MSG:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')
else:
    print('Não deu erro')
finally:
    print('Fechar arquivo')

print('Continuar')
