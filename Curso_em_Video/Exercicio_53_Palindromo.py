#Exercicio não funcionou e ainda não sei porque o join não funciona, preciso ver isso mais pra frente
#acho que esta versão precisa ser importada alguma biblioteca do join
frase = str(input('Digite uma frase :')).strip().upper()#separando as palavras e colocando em maiusculas
palavras = frase.split()
print('{}'.format(palavras))
junto = ''.join.[palavras]
inverso = ''
inverso = junto[::-1]
'''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
'''
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')
print('{} {}'.format(junto, inverso))