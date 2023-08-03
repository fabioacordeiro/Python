#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#O programa deverá analisar se a expressão passada está aberto e fechado na ordem correta.
equacao = []
Digitado = conta = contf = 0
Digitado = str(input('Digite a expressão :')).strip().upper()
equacao.append(Digitado)
for v in equacao:
   for letra in v:
        if letra in '(':
            conta= conta+1
        if letra in ')':
            contf= contf+1
if conta == contf:
    print('\nEquação válida')
    print(f'Abriu {conta} vezes e fechou {contf} vezes')
else:
    print('\nEquação inválida')
    print(f'Abriu {conta} vezes e fechou {contf} vezes')
print(f'equacao digitada:{equacao}')
