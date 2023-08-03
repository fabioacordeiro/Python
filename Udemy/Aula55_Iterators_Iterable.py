import sys

iterable = ['Eu', 'Tu', 'Ele', 'Nós', 'Vós', 'Eles']
iterators = iterable.__iter__() # tem __iter__e__next
# O iterator só sabe qual é o próximo valor ele não sabe qual o tamanho
# não sabe qual ultimo, somente o próximo e se navegar até o ultimo não tem
# como voltar, teríamos que salvar os valores em uma lista para uso posterior
print(next(iterators))
print(next(iterators))
print(next(iterators))
print(next(iterators))
print(next(iterators))
print(next(iterators))

def imprime_dicionarios(iterator):
    print(*list(iterator), sep=('-'))
    print()


print(60*'-')
imprime_dicionarios(iterable)
print(60*'-')



lista = [n for n in range(100)]
generator = (n for n in range(100))
print(f'Tamanho da lista:{(sys.getsizeof(lista))/1000000} megabytes')
print(f'Tamanho da lista:{sys.getsizeof(lista)} bytes')
print(f'Tamanho do generator: {sys.getsizeof(generator)} bytes')

# generator entrega um valor por vez como o iterators,
# também não está todo na memória e não conseguimos acessar os seus indices

for num in generator:
    print(num)

# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

print(50*'-')

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return


gen = generator(maximum=100)
for n in gen:
    print(n)

# Rendimento de
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print ('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen 
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1  =  gen2 ( gen1 ())
g2  =  gen2 ( gen3 ())
g3  =  gen2 ()
for numero in g1:
    print( numero )
print()
for numero in g2:
    print ( numero )
print()
for numero in g3:
    print ( numero )
print()