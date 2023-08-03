#pip install yfinance
#pip install yfinance prophet
#pip install pyautogui

import yfinance
from prophet import Prophet
from prpphet.plot import plot_ploty

ticker = PETR4.SA
#Ano = y
#Mês = mo
#Dia = d
dados = yf.Ticker(ticker).history('2y')# 2 anos de dados
dados.Close.plot()
#Preparando os dados para treinamento
treinamento = dados.reset_index()
#Retirando o timezone (fuso horário) da coluna de data
treinamento["Date"]=treinamento["Date"].dt.tz_localize(None)
#Selecionando as colunas de data e valor de fechamento
treinamento = treinamento[['Date', 'Close']]
#Renomeando as colunas do arquivo para o prophet entender (O prophet precisa receber os dados com esse padrão)
treinamento.columns = ['ds', 'y']
#Treinando o nosso modelo
#Criando o modelo
modelo = Prophet()
#Treinando o modelo com os dados de treinamento
modelo.fit(treinamento)
#especificando o período das previsões (em dias)
periodo = modelo.make_future_dataframe(periods=90)
#Gerando as previsões
previsoes = modelo.predict(periodo)
#Gerando o gráfico de previsões
plot_ploty(modelo, previsoes, xlabel='período', ylabel='valor')


