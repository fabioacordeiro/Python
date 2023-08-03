#Faça um programa que gere 4 números aleatório de um dado (1 a 6) e coloque em ordem de quem tirou o maior número;
#Nenhuma informação será imputada neste exercicio;
from random import randint
from time import sleep
from operator import itemgetter
#**************Inicio da PROGRAMAÇÃO do Gif****************************
import pyglet

animation = pyglet.image.load_animation('Dado.gif')
animSprite = pyglet.sprite.Sprite(animation)
w = animSprite.width
h = animSprite.height
window = pyglet.window.Window(width=w, height=h)
r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
pyglet.gl.glClearColor(r, g, b, alpha)

@window.event
def on_draw():
    window.clear()
    animSprite.draw()


pyglet.app.run(time(2))
print('Fim gif')
#**************Fim da PROGRAMAÇÃO do Gif****************************
#time_duration = 3.5
#sleep(time_duration)
print('\033[7;30;41m='*50)
print(f'\033[7;30;41m {"DADOS LANÇADOS":^50}')
print('='*50)
sleep(4)
j4 = j1 = j2 = j3 = 0
dado = {}
lista = {}
ranking = {}
j1 = randint(1,6)
print(f'O jogador1 tirou {j1}')
sleep(1)
lista[0] = j1
j2 = randint(1,6)
print(f'O jogador2 tirou {j2}')
sleep(1)
lista[1] = j2
j3 = randint(1,6)
print(f'O jogador3 tirou {j3}')
sleep(1)
lista[2] = j3
j4 = randint(1,6)
print(f'O jogador4 tirou {j4}')
sleep(1)
print('='*50)
lista[3] = j4
#print(lista)
print(f'{"ORDEM DOS GANHADORES":^50}')
dado = {'Jogador1':j1,'Jogador2':j2,'Jogador3': j3,'Jogador4': j4}
#{lista: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
sorted(dado,reverse=True)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
contar = 0
print('='*50)
for pos, v in enumerate(ranking):
    sleep(1)
    contar = contar+1
    print(f'o {contar}ºlugar: {v[0]} com: {v[1]}')
print('='*50)
print(f'{"OUTRA FORMA DE FAZER":^50}')
for i, v in enumerate(ranking):
    print(f'{(i+1)}ºlugar: {v[0]} com {v[1]}.')
print('='*50)

