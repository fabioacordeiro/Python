'''
Vamos fazer um jogo de Forca, ou seja o usuário deve advinhar a 
a palavra secreta.
O usuário deve digitar apenas uma letra cada tentativa
Deve ser contada as tentativas
O jogo deve conferir a letra digitada se está na palavra secreta
Exibir a quantidade de caracteres com um Asterisco e a letra
que o usuário acertou em sua posição original

'''
import random
import os
forca = ['Perfume', 'Quadro', 'Netflix','Leao', 'Karate', 'Furadeira', 'Praia','Automovel', 'Internet']
forca1 = ['Leao']
sorteio = random.choice(forca).upper()
#print(sorteio)
apresentacao = 'Sejam bem vindos ao jogo'.upper()
tentativa = 0
acertou = 0
Palavra = ''
qtde = len(sorteio)
print(50*'-')
print(f"{apresentacao:^50}")
print(f'{"FORCA":^50}')
print(50*'-')
print(f'_'*qtde)
while acertou < qtde:
    Digito = input('Digite uma letra qualquer :')[0].upper()
    tentativa += 1
    Palavra = Palavra + Digito
    acertou = 0
    #Analise 1 se o digito esta em sorteio verificando cada letra
    for letra in sorteio:
        for Pal in Palavra:
            if letra == Pal:
                print(f'{letra}', end='')
                acertou = acertou + 1
                break
        else:
            print('*',end='')
    #acertou = 0
    print()
    if acertou >= qtde:
        os.system('cls')
        print(f"Parabéns você conseguiu a palavra é:{sorteio}")
        break
    print()
    print(f'Acertou:{acertou} letras')
    #print(f'Qtde:{qtde}')
    if acertou == qtde:
        break
print(f'Na tentativa número:{tentativa}')






