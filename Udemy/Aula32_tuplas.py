'''
Introdução a tuplas
'''
#desempacotamento
# pegamos o primeiro valor e colocamos em uma variavel e 
# restante em outra variável
# se tivessemos 3 variáveis ele teria distribuido
# Se definir mais varivel do que itens ou vice versa o Python gera erro
n1, * resto = 'Maria','Helena','Luiz'
print(n1)
print(resto)
# Geram erros
'''
n1, n2 = ['Maria','Helena','Luiz']
n1, n2, n3, n4, n5 = ['Maria','Helena','Luiz']
'''
#OK
n1, n2, n3 = 'Maria','Helena','Luiz'
print(n1, n2, n3)
# Para descartar os valores das variáveis (_)
_, nome , _, *resto = 'Maria','Helena','Luiz'
print(nome)
print(_)