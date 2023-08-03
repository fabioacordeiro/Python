from pathlib import Path

Caminho_do_Projeto = Path()
print(60*'-')
print(f'{"Caminho completo":^60}')
print(Caminho_do_Projeto.absolute())
#print('Início')
print()
print(60*'-')
ver = '\033[0;31m          --- Caminho completo com o nome do arquivo ---'
print(ver) 
Caminho_do_Projeto = Path(__file__)
print('\033[0;31m ')
print(Caminho_do_Projeto)
print('\033[0;30m ')
print(60*'-')
print('\033[7;44m --- Ver uma pasta acima ---')
Caminho_do_Projeto = Caminho_do_Projeto.parent
print(Caminho_do_Projeto)
print(60*'-')
print('\033[7;44m --- Ver outra pasta acima ---')
Caminho_do_Projeto = Caminho_do_Projeto.parent
print(Caminho_do_Projeto)
print(60*'-')
print('\033[7;44m --- Ver mais uma pasta acima ---')
Caminho_do_Projeto = Caminho_do_Projeto.parent
print(Caminho_do_Projeto)
print(60*'-')
print('\033[7;44m --- Ver mais uma pasta acima chamada de outra maneira ---')
print(Caminho_do_Projeto.parent)
print(60*'-')
print('\033[7;44m --- Ver mais uma pasta acima chamada de outra maneira ---')
print(Caminho_do_Projeto.parent.parent)
print(60*'-')
print('\033[7;44m --- Criando caminhos virtuais, porque ele não cria a pasta---')
Novo_Caminho = Path()
ideias = Novo_Caminho.absolute()
print(ideias)
ideias = ideias.parent / 'ideias'
print(ideias / 'arquivo.txt')
print(60*'-')
print('\033[7;42m --- Visualizando a pasta Home ---')
home = Path.home()
print(home)
print(60*'-')
print('\033[7;41m --- Criando caminhos e pastas de fato ---')
Nova_Pasta = Path()
Nova_Pasta = Nova_Pasta.absolute() / 'Teste'
print(Nova_Pasta)
Nova_Pasta.mkdir()
Nova_Pasta = Nova_Pasta / 'arquivo.txt'
Nova_Pasta.touch()
#Escrevendo dentro do arquivo

with Nova_Pasta.open('a+') as file:# a = append
    Nova_Pasta.write_text("Fábio A Cordeiro - Teste 16/03/2023 17:04 \n")
    Nova_Pasta.write_text("Luciene Almeida da Siva Cordeiro - Teste 16/03/2023 17:10 \n")
    Nova_Pasta.write_text("Lucas da Siva Cordeiro - Teste 16/03/2023 17:10 \n")

print(Nova_Pasta.read_text)
print('\033[7;44mFim')