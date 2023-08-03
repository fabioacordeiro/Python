'''
Vamos criar um programa que:
1 crie as opçoes de comando: Desfazer, Fazer e Listar
'''
import sys

Desfazer = []
Fazer = []
Listar = []

while 'SAIR' not in Listar:
    print('Comandos: Desfazer, Fazer, Listar')
    resp = input(':')
    if resp == 'Sair' or resp == 'SAIR' or resp == 'sair':
        break
    elif resp == 'Desfazer' or resp =='DESFAZER' or resp == 'desfazer':
        Desfazer.append(Listar[-1])
        if len(Listar) >= 1:
            del(Listar[-1])
        else:
            print('Não há nada para deletar na Lista')
            print('Lista', Listar)
            print('Desfazer', Desfazer)
        for palavra in Desfazer:
            print(palavra)
        #print('Desfazer:', Desfazer)
    elif resp == 'fazer' or resp == 'FAZER' or resp == 'Fazer':
        print('Tamanho do fazer:', len(Fazer))
        print('Tamanho do Desfazer:', len(Desfazer))
        if len(Desfazer) >= 1:
            Fazer.append(Desfazer[-1])
            Listar.append(Fazer[-1])
            del(Desfazer[-1])
        elif len(Fazer) < 1:
            print('Não há nada para Fazer')
            #print('Desfazer:', Fazer)
        else:
            print('Não há nada para Desfazer')
            #print('Desfazer:', Desfazer)
        #print('Fazer:', Fazer)
        for palavra in Fazer:
            print(palavra)
        #print('Fazer:', Fazer)
    elif resp == 'Listar' or resp == 'listar' or resp == 'LISTAR':
        print('Listar')
        for palavra in Listar:
            print(palavra)
        #print('Listar:', Listar)
    elif resp == 'Clear' or resp == 'clear' or resp == 'CLEAR':
        os.system('clear')
    else:
        Listar.append(resp)
        #print('Listar')
        for palavra in Listar:
            print(palavra)
        #print(Listar)


