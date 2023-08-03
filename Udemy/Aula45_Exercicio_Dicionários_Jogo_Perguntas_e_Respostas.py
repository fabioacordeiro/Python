'''
Criar um Jogo de perguntas e respostas com dicionários
Contar quantas perguntas e respostas o usuário acertou
'''
import os
import time
from Auxiliar import modulo
TT = 0
Questions = [{'Pergunta':'Qual a raiz quadrada de 64 ?',
'Opções':['6', '4', '8', '24', '32'],
'Resposta':'8'},
{'Pergunta':'De quantos em quantos anos o cometa Halley pode ser visto na terra ?',
'Opções':['6-7', '14-15', '25-30', '28-29', '75-76'],
'Resposta':'75-76'},
{'Pergunta':'Quantos ossos tem no corpo humano ?',
'Opções':['34', '96', '148', '206', '320'],
'Resposta':'206'},
{'Pergunta':'Quantos músculos tem no corpo humano ?',
'Opções':['88', '148', '320', '440', '600'],
'Resposta':'600'},
{'Pergunta':'A Bíblia Sagrada tem diferença entre a Católica, Evangélica, Protestante e Hebraica qual delas considerou mais livros ?',
'Opções':['Católica', 'Evangélica', 'Protestante', 'Hebráica'],
'Resposta':'Católica'},
]
Qtde = 0
cont = 0
for dado in Questions:
    if dado['Pergunta']:
        cont = cont + 1
TT = cont
modulo.nomeprograma('Perguntas e Respostas')
print(f'Qtde de questões:{TT}', end='')
for dado in Questions:
    print(f'   Acertos:{Qtde}')
    print(f'Pergunta:',*{dado['Pergunta']})
    for i, opcao in enumerate(dado['Opções']):
        print(f'{i}) {opcao}')
    #print(dado['Opções'])
    print('')
    escolha = int(input('Digite o número da opção:'))
    escolha_int = None
    acertou = False
    valor = dado['Opções'][escolha]
    print(f'Valor:{valor}')
    if valor == dado['Resposta']:
        acertou = True
        Qtde = Qtde + 1
        print('Parabéns ! Resposta certa:')
        #print(escolha)
        print(f'Você acertou: {Qtde} resposta(s)')
    else:
        print('Que pena, resposta errada !!!')
        #print(escolha)
        print(f'Resposta correta:',{dado['Resposta']})
    print('Deseja sair do programa ?')
    print('[S] Sim')
    print('[N] Não')
    sair = input(':').upper()
    if sair == 'S':
        print(f'Você acertou: {Qtde} de {TT}')
        break
    time.sleep(4)
    os.system('cls')
print(f'Fim de perguntas, até a próxima !!!!')
print(f'Obrigado por usar o programa de perguntas e respostas do Python !!!!')