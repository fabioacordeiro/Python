'''
Interpolação basica de Strings
s-string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''
nome = "Fábio"
preco = 150.2546984
variavel = '%s preço é R$%f' % (nome,preco)
print(variavel)
print('o Hexadecimal de %d é %X' % (1500,1500))
variavel2 = '%s preço é R$%.2f' % (nome,preco)
print(variavel2)
print('o Hexadecimal de %d é %08X' % (1500,1500))
