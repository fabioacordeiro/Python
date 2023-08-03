# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil
import time

HOME = os.path.expanduser('~')

# DESKTOP = os.path.join(HOME, 'Desktop')
# PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
# NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
PASTA_ORIGINAL = ('C:\\Fabio\\Python\\Udemy\\Teste_2\\Essenciais')
NOVA_PASTA = ('C:\\Fabio\\Python\\Udemy\\Teste_2\\Essenciais2')
print(PASTA_ORIGINAL)
print(NOVA_PASTA)
# time.sleep(500)
os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminnho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminnho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminnho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminnho_novo_arquivo)
