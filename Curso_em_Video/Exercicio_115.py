import urllib.request
site = str(input('Insira o site: '))
try:
    site1 = urllib.request.urlopen('https://www.'+site+'/')
    #site1 = urllib.request.urlopen('https://www.jadlog.com.br/jadlog/home')
except urllib.request.URLError:
    print('\033[4;30;41mO Site não está acessível no momento\033[m')
else:
    print('\033[7;30;45mConsegui abrir o site com sucesso!\033[m')
finally:
    print('\033[7;30;46mVolte sempre !!!\033[m')