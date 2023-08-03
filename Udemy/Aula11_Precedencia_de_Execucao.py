#Qual a ordem de execução do Python ?
#Vamos colocar em ordem
# 1) (2+2) => São os parenteses
# 2) ** => É a exponenciação
# 3) * // / % => Multiplicação, divisão, divisão inteira, resto
# 4) + - => Soma e Subtração
Conta1 = 1+1**5+5
print("Conta 1:" , Conta1)
Conta2 = (1+1)**5+5
print("Conta 2:" , Conta2)
Conta3 = (1+1)**(5+5)
print("Conta 3:" , Conta3)
Conta4 = 1+(1**5)+5
print("Conta 3:" , Conta4)