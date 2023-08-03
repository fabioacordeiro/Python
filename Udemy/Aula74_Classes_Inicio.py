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
class Pessoa:
    def ___init___(sef, nome, sobrenome):



print(60*'-')
#Para ver se a variável nome é uma instância da classe str
# Se for ela retorna True ou False caso negativo
nome = 'Luiz'  # str
print(nome.upper())
print(60*'-')
print(isinstance(nome, str))
print(60*'-')
p1 = Pessoa()
#A linha abaixo é um objeto
p1.nome = 'Luiz'
#A linha abaixo é um outro objeto
p1.sobrenome = 'Otávio'

p2 = Pessoa()
p2.nome = 'Maria'
p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(60*'-')

print(p2.nome)
print(p2.sobrenome)

