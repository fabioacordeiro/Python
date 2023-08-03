# Podemos inverter a checagem de uma expressão com 
# o auxílio de "not"
#Exemplo
cont = 0
while True:
    valor = input("Digite a senha: ")
    print (type(valor))
    senha = ("123456")
    cont = cont+1
    print(cont)
    if valor == senha:
        print("Logado")
        break
    elif cont >= 3:
        print("Valor incorreto, mais de 3 vezes, usuário bloqueado")
        break
    elif valor != senha:
        print("valor incorreto, tente novamente")
if not (valor == senha):
    print(not False)
else:
    print (not True)
'''if cont >= 3:
    print ("Sair")
    exit
     '''
print('Fim While')
