# Retira as vogais da palavra esse bloco pode ser lido como :palavras
# para cada palavra na tupla de palavras, mostre a palavra;
# para cada letra da palavra se a letra for uma vogal, mostre a vogal da palavra.
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
print('='*50)
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos :', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
print('\n ')
print('='*50)
print('Fim')