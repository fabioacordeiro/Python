# Veja o arquivo Aula74_Classes_Inicio para entender essa é continuação
# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
#Não se utiliza parenteses para atributos
#Exemplo correto: print(p1.nome)
#Exemplo errado: print(p1.nome())

# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
# Diferença de parâmetros e argumentos
# Parâmetro é a variável que irá receber os argumentos
# Argumento é o valor que você passa para a função (ou método).
# Abaixo temos a classe Pessoa
# toda função dentro de uma classe é um método
# Ao criarmos o classe o primeiro parâmetro padrão é o self
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        


print(60*'-')
#Para ver se a variável nome é uma instância da classe str
# Se for ela retorna True ou False caso negativo
p1 = Pessoa('Luiz', 'Otávio')
p2 = Pessoa('Maria','Joana')
print(p1)

print(p1.nome)
print(p1.sobrenome)
'''
print(60*'-')

print(p2.nome)
print(p2.sobrenome)

'''