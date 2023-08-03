#Faça um programa onde o usuário vai digitar vários valores numéricos, cadastrar em uma lista
#Não adicionar valores duplicados
#Mostrar a lista no final em ordem crescente
valores = []
while True:
    Digitado = int(input('Digite um valor :'))
    if Digitado in valores:
        print('Valor duplicado !! Não vou adicionar')
    else:
        valores.append(Digitado)
        print('Valor adicionado com sucesso !!!')
    Qtde = str(input('Deseja continuar [S/N] ?:')).strip().upper()
    if Qtde == 'N':
        break
print(f'Os valores digitados foram {sorted(valores)}')


