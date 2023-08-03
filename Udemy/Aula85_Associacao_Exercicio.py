class Eletricista:  
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentasDeCorte:
    def __init__(self, nome) -> None:
        self.nome = nome

    def trabalhando(self):
        return f'{self.nome} está cortando'



eletricista = Eletricista('Fábio Alves Cordeiro')
alicate = FerramentasDeCorte('Alicate')
serra = FerramentasDeCorte('Serra mármore')

eletricista.ferramenta = alicate
print(60*'-')
print(alicate.trabalhando())
print(serra.trabalhando())

