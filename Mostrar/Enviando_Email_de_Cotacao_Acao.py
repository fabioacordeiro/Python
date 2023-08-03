import pyautogui
import pyperclip
import yfinance

print(60*'-')
# ticker = input('Digite o código da ação: ')
ticker = ('PETR4.SA')
dados = yfinance.Ticker(ticker)
print(dados.history())
# Ano=y
# Mes=mo
# Dia=d
tabela = dados.history("6mo")
print(tabela)
fechamento = tabela.Close
print(fechamento)
# fechamento.plot()
# print(fechamento.show())
maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

print(maxima)
print(minima)
print(atual)

'''
Enviando e-mail de forma automática
Processo de enviar um e-mail passo a passo:
abrir uma nova aba no navegador (clicar em + ou CTRL + T)
digitar o endereço do gmail (www.gmail.com) e digitar ENTER
clicar em Escrever
digitar o endereço de e-mail do destinatário
mudar para o campo Assunto (clicar no campo ou digitar tab)
digitar o Assunto
mudar para campo principal do e-mail (clicar no campo ou digitar tab)
escrever a mensagem
clicar em Enviar
'''

destinatario = "novosprojetosbr@gmail.com"
assunto = "Análise diária - Ação Petrobrás"

mensagem = f"""
Bom dia,

Segue abaixo as análises da ação {ticker} dos últimos seis meses:

Cotação máxima: R${round(maxima,2)}
Cotação mínima: R${round(minima,2)}
Cotação atual: R${round(atual,2)}

Atenciosamente,
Fábio Alves Cordeiro.
"""
print(destinatario)
print(assunto)
print(mensagem)

# configurar uma pausa entre as ações do pyautogui
pyautogui.PAUSE = 2

# alt + tab para sair da tela do console python
pyautogui.hotkey("alt", "tab")
# abrir uma nova aba
pyautogui.hotkey("ctrl", "t")

# copiar o endereço do gmail para o clipboard
pyperclip.copy("https://mail.yahoo.com/d/folders/1?reason=invalid_crumb")

# colar o endereço do gmail e dar um ENTER
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# clicando no botão Escrever
# pyautogui.click(x=132, y=176, clicks=1)
# pyautogui.moveTo(x=2034, y=218)
# pyautogui.press("enter")
pyautogui.click(x=103, y=213)
pyautogui.press("enter")

# Preenchendo o campo destinatário
pyperclip.copy(destinatario)
pyautogui.click(x=270, y=237)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
# pyautogui.press("enter")

# Preenchendo o assunto
pyperclip.copy(assunto)
pyautogui.press("tab")
pyautogui.click(x=274, y=365)
pyautogui.press("tab")
pyautogui.click(x=274, y=279)
pyautogui.hotkey("ctrl", "v")
# pyautogui.click(x=246, y=297)
pyautogui.press("tab")
# pyautogui.press("enter")

# Preenchendo a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Clicar no botão Enviar
pyautogui.click(x=271, y=689)
# pyautogui.click(x=288, y=639)
# fechar a aba do gmail
pyautogui.hotkey("ctrl", "f4")

# Imprimir mensagem de enviado com sucesso
print('E-mail enviado com sucesso!')
