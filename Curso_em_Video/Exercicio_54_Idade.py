from datetime import date
atual = date.today().year
maior = 0
menor = 0
for cont in range (1,6):
        nasc = int(input('Digite o Ano de Nascimento da pessoa {} :'.format(cont)))
        idade = (atual - nasc)
        if idade < 18:
            menor = menor + 1
        else:
            maior = maior + 1
print('\033[030;41m De acordo com as datas de nascimento temos \n {} pessoa(s) Maior de Idade e \n {} pessoa(s) Menor de idade'.format(maior, menor))
