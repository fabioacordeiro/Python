# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
'''
formato de arquivo
# .env
VARIAVEL_DE_AMBIENTE_1=valor
VARIAVEL_DE_AMBIENTE_2=valor
VARIAVEL_DE_AMBIENTE_3=valor
exemplo:
BD_USER="fcordeiro"
BD_PASSWORD="Aprenda"
BD_PORT=557
BD_HOST="10.121.175"
'''
import os

from dotenv import load_dotenv  # type: ignore

load_dotenv()

print(os.environ)
print(os.getenv('BD_PASSWORD'))
