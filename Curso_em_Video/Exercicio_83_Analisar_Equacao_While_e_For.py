#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#O programa deverá analisar se a expressão passada está aberto e fechado na ordem correta.
equacao = []
Digitado = 0
conta = 0
contf = 0
valor='L'
while valor not in 'N':
    Digitado = str(input('Digite a expressão :')).strip().upper()
    equacao.append(Digitado)
    print(f'equacao digitada:{equacao}')
   # valor = str(input('Deseja continuar [S/N] ? :')).strip().upper()
for v in equacao:
    print(f'\nNa equacao {v.upper()} temos :', end='')
    for letra in v:
        if letra in 'ABCDEFGHIJLMNOPQRSTUVXYZ0123456789{}[]()*/-+=':
            print(letra, end='-')
for v in equacao:
   # print(f'\nNa equacao {v.upper()} temos :', end='')
    for letra in v:
        if letra in '(':
            conta= conta+1
      #      print(letra, end='-')
        if letra in ')':
            contf= contf+1
         #   print(letra, end='-')
if conta == contf:
    print('\nEquação válida')
    print(f'Abriu {conta} vezes e fechou {contf} vezes')
else:
    print('\nEquação inválida')
    print(f'Abriu {conta} vezes e fechou {contf} vezes')

print(f'equacao digitada:{equacao}')
