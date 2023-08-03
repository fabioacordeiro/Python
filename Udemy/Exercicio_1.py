'''
Criar um programa que:
Peca ao usuário digitar seu nome
peca ao usuário digitar sua idade
Se seu nome for digitado exibir:
nome
nome invertido
Se tem espaços
a qtde de caracter
A primeira leta
A ultima letra
Se nada for digitado exibir:
Você deixou campos vazios
'''
cont = 0
ver = 0
while True:
    nome = str(input('Digite seu nome: ')).upper().strip()
    idade = int(input('Digite a sua idade:'))
    if nome and idade:
        print('Seu nome é :{}'.format(nome))
        print(f'Seu nome invertido é:{nome[::-1]}')
        if "" in nome :
              print("Seu nome tem espaços")
        else:
             print("Seu nome não tem espaços")
        print('Sua idade é :{}'.format(idade))
        print(f'Seu nome contem: {len(nome)} caracter(s)')
        print(f'A primeira letra do seu nome é: {nome[0]}')
        print(f'A ultima letra do seu nom é:{nome[-1]}')
    else:
        print("Você deixou campos vazios")
    break
print("Fim While")

