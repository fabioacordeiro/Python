'''
Testando as classes, para isso inserir e retirar os comentários dos métodos 
abaixo e veja os resultados para as heranças
como pesquisar a ordem das classes com o MRO '''

class Arvore:
    def quem_sou(self):
        print('Dionizio Cordeiro')
       
class Tronco(Arvore):
    def quem_sou(self):
        print('Fábio Alves Cordeiro')
    
class Galho(Tronco, Arvore):
    def quem_sou(self):
        '''print('Lucas da Silva Cordeiro')'''

class Fruto(Galho, Tronco, Arvore):
    '''def quem_sou(self):
        print ('Maximus da Silva Cordeiro')'''

bebeHomem = Arvore()
bebeHomem.quem_sou()

print(60*'-')
bebeMulher = Fruto()
bebeMulher.quem_sou()

bebeNovo = Tronco()
bebeNovo.quem_sou()
print(60*'-')
print(Fruto.mro())