from dataclasses import dataclass


@dataclass
class Pessoa():
    nome: str
    sobrenome: str
    idade: int

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome} => {self.idade}'
        return print(self.nome_completo)


'''
    def __post_init__(self):
        self.nome_completo = f'({self.nome} {self.sobrenome})'
        return print(f'POST INIT', {self.nome_completo})'''


print(60*'-')
if __name__ == '__main__':
    turma = Pessoa('Fábio', 'Alves Cordeiro', 30)
    print(turma)
print(60*'-')
