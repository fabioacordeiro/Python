# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
# Criando um caminho
caminho = r'C:\\Fabio\Python\\Udemy\\' #Sempre usar 2 barras invertidas nos caminhos para não gerar erro no Python
caminho = caminho+'Teste.txt'
arquivo = open(caminho,'w+', encoding='utf8')# w para escrita, + para que o arquivo tenha mais funções além de ser escrito, no caso vamos ler o arquivo.
arquivo.write('Olá mundo !!!')
arquivo.write('Atenção !!!')
arquivo.write('Interação com a escrita dentro do arquivo \n    ')
arquivo.write('Seguindo na escrita da segunda linha \n')
arquivo.write('        Amo minha família !!!! \n')
arquivo.write('Hoje é 06/03/2023 11:14 \n')
arquivo.writelines(('Tupla 1 \n', 'Tupla 2 \n', 'Tupla 3 \n'))
arquivo.seek(0,0)#Movendo o cursor para o início do arquivo onde vai iniciar a leitura
print(arquivo.read())#Se ler o arquivo sem mover o cursor provavelmente a tela estará em branco
print(60*'-')
print('Readlines')
arquivo.seek(0,0)
for linha in arquivo:
    print(linha.strip())



arquivo.close()


with open(caminho_arquivo, 'w') as arquivo:# O with vai abrir e fechar o arquivo, o que é muito importante
    print('Olá mundo')
    print('Arquivo vai ser fechado')