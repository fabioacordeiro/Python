#Aula de funções
# Exemplo

def l():
    print('='*50)

def AP():
    print(f'{"Estou aprendendo PYTHON !!!":^50}')


l()
print(f'{"Olá Mundo !!!":^50}')
l()
AP()
l()

def men(txt):
    print('=' * 50)
    print(txt)
    print('=' * 50)


men("SISTEMA DE ALUNOS")
men('CURSO EM VÍDEO')

def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A e B é: {s}')


soma(55, 32)

def contador(*núm):
    for valor in núm:
        print(f'{valor}, ', end='')
    print('FIM')


contador(3, 2, 1)
contador(50, 201, 83)
contador(80, 21, 8)

def contador1(*núm):
    tam = len(núm)
    print(f'Recebi os valores:{núm} e são ao todo {tam} números, ', end='')
    print('FIM')


contador1(3, 2, 1)
contador1(50, 201, 83)
contador1(80, 21, 8)

def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos = pos + 1


valores = [110, 15, 20, 34, 63]
dobra(valores)
print(valores)

