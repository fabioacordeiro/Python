'''
Aula 26
While
continue
break
'''
contador = 0
while contador <= 20:
    contador = contador +1
    if contador >= 3 and contador <=10:
        continue
    elif contador in (4,5,6):
        continue
    print(contador)
    if contador == 18:
        break
print("Fim while")

print(50*'=')
#Outro programa
TT_linha = 5
TT_coluna = 5
linha = 0
while linha <= TT_linha:
    linha = linha +1
    coluna = 1
    while coluna <= TT_coluna:
        print(f'L{linha}:C{coluna} ',end='')
        coluna = coluna+1
    print('-')
print("Fim While2")
