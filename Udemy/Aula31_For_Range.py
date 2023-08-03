'''
Vamos aprender a interação de For e Range
O For não precisa da informação do início e fim como o while
exemplo na programação abaixo não definimos a
variável 'letra' o For já entendi o while tem que ser definido

'''
Letras = 'Fabio Alves Cordeiro'
for letra in Letras:
    print(f'{letra}', end='')
print()
print(50*'-')
#veja que letra não foi definido, mas o For
# reconheceu o início e fim
''''
Agora vamos ver o 'range'
range ->range(start, stop, step)
start => início
stop => parada
step => passso (contar de 2 em 2 por exemplo)
'''
numeros = range(2,20,2)
for num in numeros:
    print(num)
print('Fim For1')
print()
print(50*'-')
print()
numeros = range(10)#Quando informado somente 1 valor o For considera que seja a parada.
for num in numeros:
    print(num)
print('Fim For 2')