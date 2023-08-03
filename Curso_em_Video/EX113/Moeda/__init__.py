def leiaInt(num=0):
    Ok = False
    while Ok is False:
        vlr = num
        # print('Passo 1')
        # print(f'vlr passo 1: {vlr}')
        if vlr.isnumeric():
        #    print('Passo 2, OK')
            Ok = True
            vlr = int(num)
         #   print(f'vlr passo 2:{vlr}')
        else:
            num = ':'
            print('ERRO !!!! Digite um valor válido')
           # print('Passo 3')
            vlr = str(input(num))
            num = vlr
            #print(f'vlr passo 3: {vlr}')
        if Ok == True:
            break
    return vlr


def leiaFloat(num=0):
    return num


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[7;30;41mERRO!! Por favor digite um valor válido !\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\033[7;30;41mEntrada de dados interrompida pelo usuário. \033[m')
            return n
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[7;30;41mERRO!! Por favor digite um valor válido !\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\033[7;30;41mEntrada de dados interrompida pelo usuário. \033[m')
            return n
        else:
            return n