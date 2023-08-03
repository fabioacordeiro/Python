'''
Abrir o terminal do Python
instalar o selenium webdriver_manager
pip install selenium
pip install webdriver_manager
EMPRESAS COM CUSTO TWILIO 
Sem custo WHATSAUTO sem muita personalização
Whatsapp B = Business
empresas com acessoa a API 'ZENVIA, WAVY, take Blip e Smarters'
'''
'''
Passos 
1) Importar as bibliotecas
2) Navegar até o Whatsapp web
3) Buscar contatos/grupos
4) Enviar mensagens para o contato/grupo
'''
# 1) Importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# 2) Navegar até o Whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(40)
# 3) Buscar contatos/grupos
contatos = ['Lembrete','ENTRE AMIGOS','Luciene']
mensagem = "Boa tarde !!!"

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)




def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()# Esta informação[1] é para pegar dentro os elementos com o mesmo nome o segundo item
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)



# 4) Enviar mensagens para o contato/grupo
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)