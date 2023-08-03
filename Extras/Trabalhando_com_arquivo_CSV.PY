# Opções de abertura de arquivo CSV
import csv
import urllib.request
from datetime import datetime

# import numpy as np
import pandas as pd
import requests

# Abrindo arquivo direto com o python sem o pandas

with open('c:\Fabio\Python\Extras\CTE.csv', mode='r') as cte:
    leitor_csv = csv.reader(cte)
    '''
    #interando com o for e lendo linha a linha
    for valor in leitor_csv:
        print(valor)
'''
# Abrindo com o enumerate
    for indice, linha in enumerate(leitor_csv):
        if indice == 0:
            print(f'Cabeçalho: {linha[0]}')
        elif indice == 100:  # limitando a leitura de 100 linhas
            break
        else:
            print({indice}, {linha[0]})
print(60*'-')
# Abrindo agora com o pandas
'''
table = pd.read_csv('c:\Fabio\Python\Extras\CTE.csv', encoding='utf-8')
# table = pd.read_csv('c:\Fabio\Python\Extras\CTE.csv', encoding='latin1')
table.head()
'''
# Abrindo arquivos muito grandes
print(60*'-')
table = pd.read_csv('c:\\Fabio\\Python\\Extras\\Base_Final.csv',
                    encoding='utf-8', sep=';', low_memory=False, decimal=',', thousands='.', parse_dates=['Data', 'DT_Fim'])
print(f'{"Início da impressão com for":.^60}')
for linha in table:
    print(linha)
print(f'{"Início do table.info() ":.^60}')
table.info()
print(f'{"Início do sort_values":.^60}')
print(table.loc[:, 'Qtde Vendas'].sort_values())
print(f'{"Início do filtro > 300.000":.^60}')
print(table.loc[table['Vlr Total'] > 300000, 'Vlr Total'].sort_values())
print(f'{"Início do tratamento de campo data":.^60}')
# table2 = pd.read_csv(table, parse_dates=['Data', 'DT_Fim'])
# Verificando se o pandas entendeu que a coluna data é uma data
table['Data'].dt.strftime('%d/%m/%Y')
print(table['Data'].dt.strftime('%d/%m/%Y'))
print(f'{"Lendo 10 linhas de arquivos gigantes com o chunksize=10":.^60}')
dados = pd.read_csv('c:\Fabio\Python\Extras\CTE.csv', sep='|', chunksize=15)
# Fazendo agora um looping de 10 em 10
for valor in dados:
    valor.info()
    break  # parando a execução do programa nos 10 primeiros

cont = 0
dados1 = pd.read_csv('c:\Fabio\Python\Extras\CTE.csv', sep='|', chunksize=34,
                     encoding='utf-8', low_memory=False, decimal=',', thousands='.', parse_dates=['emissao   ', 'faturamento', 'entrega', 'coleta'])
print(f'{"Lendo 1 linha de arquivos gigantes com o for":.^60}')
for valor in dados1:
    cont = 1
    valor.info()
    print(valor)
    break

print(dados1['entrega'].dt.strftime('%d/%m/%Y'))
# table.['ultima_Entrada'].dt.strftime('%Y/%m/%d')
# table.loc[table['Vlr Total'].sort_values('.'), 'Vlr Total']
# table.loc[table['Vlr Total'].str.contains('.'), 'Vlr Total']
print(f'{"Criando uma coluna com retirando 1 caracter":.^60}')

table['Vlr Total'] = table['Vlr Total'].str[1:]
print(table['Vlr Total'])

'''
dados = urllib.request.urlopen(list(table))
for linha in dados:
    print(linha)
    break
'''
# Para visualizar os dados principais
# dados.head()
print(60*'-')
