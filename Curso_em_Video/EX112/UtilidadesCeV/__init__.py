def leiadinheiro(msg):
    válido = False
    while válido == False:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f'\033[0;31mERRO!!!:\"{entrada}\" é um preço inválido !\033[m ')
        else:
            válido = True
            return (entrada)