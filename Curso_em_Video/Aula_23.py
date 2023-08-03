#Vamos gerar alguns erros e estudá-los esses erros são chamados de excessões:

#print(x)
# Gera o erro de Nome na linha 3, pois o 'x' não foi definido
# NameError: name 'x' is not defined
####################################################################
#a = int(8)
#b = int(0)
#r = a / b
#print(f'O valor de a/b é : {r}')
#Gera o erro de divisão por zero
#ZeroDivisionError: division by zero
###################################################################
r = 0
try:
    a = int(8)
    b = int()
    r = a / b
except (ValueError):
    print('Tivemos um problema com os tipos de dados que você digitou !!!')
except(ZeroDivisionError):
    print('O número não é divisível por Zero !!!')
except(KeyboardInterrupt):
    print('O usuário preferiu não digitar os dados')
except Exception as erro:
    print(f'O erro foi {erro.__class__}')
else:
    print(f'O valor de a/b é : {r:.0f}')
finally: #Esse código sempre vai ser digitado ...
    print('Obrigado Volte Sempre !!!!')
#Gera o erro de divisão por zero
#ZeroDivisionError: division by zero