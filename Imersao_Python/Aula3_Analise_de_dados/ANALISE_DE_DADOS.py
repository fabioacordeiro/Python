import pandas as pd
import plotly_express as px
dados = pd.read_excel('vendas.xlsx')
print(60*'-')
print(f'{"-----Informações do describe() -----":^40}')
print(dados.describe())
print(60*'-')
print(f'{"-----Informações do info() -----":^40}')
print(dados.info())
print(60*'-')
print(f'{"-----Acessando os dados da Loja-----":^40}')
print(dados['loja'])
print(60*'-')
print(f'{"-----Acessando os dados da Loja com unique() -----":^40}')
print(dados['loja'].unique())
print(60*'-')
print(f'{"-----Contagem de valores .value_counts() -----":^40}')
print(dados['loja'].value_counts())
print(60*'-')
print(f'{"-----Contagem de valores .value_counts(normalize=True) -----":^40}')
print(dados['loja'].value_counts(normalize=True))
print(60*'-')
print(f'{"-----Agrupando a soma de preço por regiao dados.groupby().sum() -----":^40}')
print(dados.groupby(['regiao']).sum('preco'))
print(60*'-')
print(f'{"-----Agrupando o valor medio por loja dados.groupby().mean() -----":^40}')
print(dados.groupby(['loja']).mean('preco'))
print(60*'-')
grafico = px.histogram(dados,x=['loja'], color='regiao', text_auto=True)
grafico.write_html(f'faturamento.html')
grafico.show()

colunas = ['loja', 'cidade', 'estado', 'tamanho', 'local_consumo']
for coluna in colunas:
    fig = px.histogram(dados, x=coluna, y='preco', color='forma_pagamento', text_auto=True)
    fig.write_html(f"faturamento por {coluna}.html")
    fig.show()

print(60*'-')
print(f'{"-------- Gráfico Animado --------":^40}')
#Agrupando os dados
agrupado = dados.groupby(['loja', 'ano_mes'])
#Resetando os índices
agrupado.reset_index(inplace=True)
#Cria uma coluna com o valor acumulado
agrupado['acumulado'] = agrupado.groupby('loja').cumsum()
# Gerando o gráfico
fig = px.bar(agrupado,
            x='acumulado',
            color='loja',
            text_auto = True,
            range_x = [0,16000],
            animation_frame='ano_mes'
            )
fig.show()
# Exportando o gráfico para um arquivo
fig.write_html('grafico_animado.html')



