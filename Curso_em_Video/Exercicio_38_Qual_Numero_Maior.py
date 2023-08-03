n1 = int(input('\033[4;30;41m Qual o PRIMEIRO número :'))
n2 = int(input('\033[4;30;41m Qual o SEGUNDO número :'))
if n1>n2:
    print('\033[4;30;41m O PRIMEIRO número é maior')
elif n2>n1:
    print ('\033[7;30;41m O SEGUNDO número é maior')
else:
    print ('\033[4;30;46m Os números são iguais')
