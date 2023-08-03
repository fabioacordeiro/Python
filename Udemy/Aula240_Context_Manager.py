# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
'''
class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()


with MyOpen('aula149.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
'''
import time


print(60*'-')
print(f'{"Chamando a classe e imprimindo o nome da classe":^60}')
class MyContextManager:
    def __init__(self):
        print('Init --- o Início ---')

    def __enter__(self):
        print('Enter')

    def __exit__(self, class_expetion, excepetion_, traceback):
        print('Exit')


a = MyContextManager()
print(a.__class__.__name__)
print('Helloooouuuoooouu')
with a as l:
    ...

############################################################
#Podemos chamar a class direto com o with também como abaixo
print(60*'-')
print(f'{"Outra forma de chamar a classe":^55}')
with MyContextManager() as t:
    ...


print(60*'-')
print(f'{"Nova classe com novas funções escrevendo o código dentro do arquivo":^55}')
############################################################
#Podemos chamar a class direto com o with também como abaixo

class MyOpen:
    def __init__(self, caminho_do_arquivo, modo):
        self.caminho_do_arquivo = caminho_do_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo Arquivo')
        self._arquivo = open(self.caminho_do_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_expetion, excepetion_, traceback):
        print('Fechando o Arquivo')
        self._arquivo.close()



with MyOpen('Aula149.txt', 'w') as arquivo:
    arquivo.write('class MyContextManager1:\n')
    arquivo.write('    def __init__(self, caminho_do_arquivo, modo)\n')
    arquivo.write('        self.caminho_do_arquivo = caminho_do_arquivo\n')
    arquivo.write('        self.modo = modo\n')
    arquivo.write('        self._arquivo = None\n')
    arquivo.write('\n')
    arquivo.write('    def __enter__(self)\n')
    arquivo.write('        print("Abrindo Arquivo")\n')
    arquivo.write('        self._arquivo = open(self.caminho_do_arquivo, self.modo, encoding="utf8")\n')
    arquivo.write('        return self._arquivo\n')
    arquivo.write('\n')
    arquivo.write('    def __exit__(self, class_expetion, excepetion_, traceback):\n')
    arquivo.write('        print("Fechando o Arquivo")\n')
    arquivo.write('\n')
    arquivo.write('\n')
    arquivo.write('\n')
    arquivo.write('b = MyContextManager1("Aula149.txt", "w")\n')
    arquivo.write('with b as l:\n')
    arquivo.write('...\n')
    print(arquivo)
    
print(60*'-')
print(f'{"Imprimindo com o with":^55}')
with MyOpen('Aula149.txt', 'r') as arquivo:
    texto = arquivo.readlines()
    print(texto)

print(60*'-')
print(f'{"Imprimindo com o for":^55}')

for frase in texto:
    if len(frase) > 1:
        print(frase)