# Funções decoradoras e decoradores com classes

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')


print(60*'-')
print(f'{"Funções com os decoradores":^60}')

print(brasil)
print(portugal)

print(terra)
print(marte)

print(60*'-')
print(f'{"Funções sem os decoradores - Sem o repr":^60}')

class Squad:
    def __init__(self, nome):
        self.nome = nome


class SistemaSolar:
    def __init__(self, nome):
        self.nome = nome

comercial = Squad('Comercial')
ti = Squad('Tecnologia da Informação')

Vlactea = SistemaSolar('Via Láctea')
umenor = SistemaSolar('Ursa Menor')

print(comercial)
print(ti)
print(Vlactea)
print(umenor)

print(60*'-')
print(f'{"Funções implementando os decoradores parcial":^60}')

class Equipe:
    def __init__(self, nome, qtde):
        self.nome = nome
        self.qtde = qtde
    
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

class Veiculo:
    def __init__(self, marca, tipo, modelo):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo



Ecom = Equipe('Comercial', '12')
Eti = Equipe('TI - Desenvolvimento', '15')

bmw1200 = Veiculo('BMW', 'Moto', '1250 Adventure')
azera = Veiculo('Honda', 'Carro', 'Azera')

print(Ecom)
print(Eti)
print(bmw1200)
print(azera)

print(60*'-')
print(f'{"Funções implementando os decoradores parcial 2 ":^60}')


def decorador (ver):
    def meu_decorador(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_decorador = f'{class_name}({class_dict})'
        return class_decorador
    ver.__repr__ = meu_decorador
    return ver

class Familia:
    def __init__(self, nome):
        self.nome = nome
    
class Carros:
    def __init__(self, marca, tipo, modelo):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo

Familia = decorador(Familia)
cordeiro = Familia('Fábio Luciene e Lucas')
Carros = decorador(Carros)
car = Carros('BMW', 'Moto', '1250 Adventure')
car2 = Carros('Honda', 'Carro', 'Azera')

print(cordeiro)
print(car)
print(car2)

print(60*'|')
print(f'{"Funções implementando os decoradores em si ":^60}')

#Decorador em si @nome_do_decorador
@decorador
class Parentes:
    def __init__(self, nome):
        self.nome = nome
@decorador
class TheCar:
    def __init__(self, marca, tipo, modelo):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo

familia = Parentes('Lucas, Fábio e Luciene')
car3 = TheCar('Mercedes', 'Caminhão', 'Actros Euro6')
car4 = TheCar('Honda', 'Carro', 'Civic Hibrido')

print(familia)
print(car3)
print(car4)


print(60*'|')
print(f'{"Funções implementando os decoradores em si outra maneira ":^60}')

def decoradormio(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def call_decoradormio(ver):
    ver.__repr__ = decoradormio
    return ver


@call_decoradormio
class MyCar:
    def __init__(self, nome, tipo, combustivel):
        self.nome = nome
        self.tipo = tipo
        self.combustivel = combustivel



@call_decoradormio
class MyMundo:
    def __init__(self, nome):
        self.nome = nome
       





sol = MyMundo('Sol')
print(sol)

carroca = MyCar('Carro de Boi', 'Movido a cavalo', 'Sem consumo de gasolina')

print(carroca)