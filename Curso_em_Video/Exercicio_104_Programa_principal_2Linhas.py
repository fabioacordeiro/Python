#Faça um programa que no programa principal tenha somente 2 linhas:
#Onde ele pergunte qual um número ? após a digitação ele deve validar se de fato
# é um número e gere uma mensagem de erro

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[7;30;41m ERRO!!! Digite um número inteiro válido !!!')
        if ok == True:
            break
        else:
            print(' Please')
    return valor



#Programa Principal
n = leiaInt(' Digite um número:')
print(f' Você acabou de digitar o número: {n}.')