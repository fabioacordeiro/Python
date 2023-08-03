'''
Podemos formatar as Strings de várias maneiras
> alinhar a esquerda
< alinhar a direita
^ alinhar no centro
+ mostrar o sinal de positivo ou negativo
Fatiamento de String
[i:f:p] [::]
i = inicio
f = fim
p = passo (por exemplo de 2 em 2, para retroceder é -1)
Obs: a função len retorna a quantidade
de caracter da string
'''

texto = "Fábio"
print (f'{texto: ^50}')
print(f'{texto: >50}')
print(f'{texto: <50}')
valor = 275.5478654
print(f'{valor:0=+8,.2f}')
texto2 = "Olá mundo infinito !!!"
print(f'{texto2[10:18]}')
print(f'{texto2[-1:]}')
print(len(texto2))#Qtde de caracter
cont = len(texto2)
print('A quantidade de caracter do texto2 é:{}'. format(cont))
print (f'{texto2[-5:-13:-1]}')#retroceder -1
print(50*'-')
print (f'{texto2[-12:-4]}')
print (f'{texto2[-12:-4:2]}')
