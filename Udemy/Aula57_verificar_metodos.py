# dir, hasattr e getattr em Python
from Auxiliar import modulo
modulo.nomeprograma('VERIFICAÇÃO DE MÉTODOS:')


string = 'Luiz'
metodo = 'lower'

if hasattr(string, metodo):
    print(f'Existe: {metodo}')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)


print(60*'-')