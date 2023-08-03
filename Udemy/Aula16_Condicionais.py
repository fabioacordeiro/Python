#Vamos aprender as condicionais
# if / elif / else
# Se / se nao se / então
opcao = input ("Digite um valor entre 1 e 10: ")
if opcao in("1,2,3,4,5"):
    print("O valor é menor que 6")
elif opcao in("6,7,8,9,10"):
    print("O valor digitado é maior que 5")
else:
    print("Você digitou um valor diferente do solicitado.")