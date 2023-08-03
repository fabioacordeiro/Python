from pathlib import Path
from shutil import rmtree 

print(60*'-')
print('\033[0;31m --- Criando pastas e arquivos---')
Novo_Caminho = Path()
Novo_Caminho = Novo_Caminho.absolute()
print(Novo_Caminho)
Novo_Caminho = Novo_Caminho / 'Teste'
Novo_Caminho.mkdir(exist_ok=True)

for i in range(1,11):
    Novo_arquivo = Novo_Caminho / f'arquivo{i}.txt'
    Novo_arquivo.touch()
    if Novo_arquivo.exists():
        Novo_arquivo.unlink()
    else:
        Novo_arquivo.touch()

    with Novo_arquivo.open('a+') as text_files:
        text_files.write('Fábio Alves Cordeiro 16/03/2023 18:34 \n \r \n')
        text_files.write(f'arquivo{i}.txt')

#Cuidado o comando abaixo apaga a pasta inteira
#rmtree(Novo_arquivo)

def rmtree(root: Path, remove_root=True):
    for Novo_arquivo in root.glob('*'): #informar o nome ou extensão do arquivo dentro do glob
        if Novo_arquivo is dir():
            print('Dir:', Novo_arquivo)
            rmtree(Novo_arquivo) # Isto é uma recursão
           #Novo_arquivo.rmdir()
        else:
            print(f'A função abaixo está comentada para não deletar os arquivos ou pastas :{Novo_arquivo}')
            #Novo_arquivo.unlink()

    #if remove_root:
    #    root.rmdir()
print(60*'-')
rmtree(Novo_Caminho)

print(60*'-')
print('Fim')