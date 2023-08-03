Adicao = 10 + 10
Multiplicacao = 10 * 5
Subtracao = 10 - 8
Divisao = 113 / 2
Divisao_Int = 113//2
Exponenciacao = 4 ** 4
Resto = 5 % 2 #Para saber se um número é divisível por
# por outro é interessante saber;
A = 50
B = 3
Resto_1 = A % B
Divisivel = Resto_1 == 0 #O sinal de comparação igual "=="
print("Adição: ", Adicao)
print("Multiplicacao: ", Multiplicacao)
print("Subtraçao: ", Subtracao)
print("Divisão: ", Divisao)
print("Divisão Inteira: ", Divisao_Int)
print("Exponenciação: ", Exponenciacao)
print("Resto da divisão: ", Resto)
print("Resto da divisão entre {} e {} é {}".format(A,B,Resto_1))
print("O número {} é divisível por {} ? Resposta:{}". format(A, B, Divisivel))
