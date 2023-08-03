#Crie uma tupla peenchida com os 20 primeiros colocados da tabela do Brasileirão na ordem de colocação.
#Mostre:
#Os 5 primeiros
#Os ultimos 4 colocados;
#Times em ordem alfabética;
#Em que posição está o time da Chapecoense
Times = ('Corinthians', 'Palmeiras','Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético PR', 'Bahia', 'São Paulo',
         'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('='*50)
print(f'Lista de time: {Times}')
print('='*50)
print(f'Os 5 primeiros são: {Times[:5]}')
print('='*50)
print(f'Os 4 últimos são: {Times[-4:]}')
print('='*50)
print(f'Times em ordem alfabética :',sorted(Times))
print('='*50)
print(f'Os 5 primeiros são: {Times[:5]}')
print('='*50)
print(f'O Chapecoense está na posição : {Times.index("Chapecoense")+1}')
print('='*50)
print('Classificação Geral BRASILEIRÃO')
for pos, t in enumerate(Times):
    print(f'{pos+1} => {t} # ')
