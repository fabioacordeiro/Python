import requests

print ("Segue os valores de cotação atual")

def pegar_cotacoes():
  requisicao = requests.get('http://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL/')
 #print(requisicao)
 #print(requisicao.json())
  requisicao_dic = requisicao.json()

  cotacao_DOLAR = requisicao_dic['USDBRL']['bid']
  cotacao_EURO = requisicao_dic['EURBRL']['bid']
  cotacao_btc = requisicao_dic['BTCBRL']['bid']

  texto= f'''

  DOLAR:{cotacao_DOLAR}
  EURO:{cotacao_EURO}
  BTC:{cotacao_btc}'''

  texto_cotacoes = {}
  texto_cotacoes["text"] = texto

  return texto
  print(["texto"])

print(pegar_cotacoes())
