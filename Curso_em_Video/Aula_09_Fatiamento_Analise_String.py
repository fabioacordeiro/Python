#Vamos entender como o Python trabalha com as cadeias de Caracteres
#Curso em Vídeo Python
#0123456789
#
Frase = 'Curso em Vídeo Python'
Frase2 = '   Aprenda Python    2022    '
print('Exemplo 1:', Frase)
print('Exemplo 2:',Frase[0])#Somente o caracter número 0, ele inicia a contagem em 0
print('Exemplo 3:',Frase[0:10])#Comece com o caracter 0 até 9, ele sempre desconsidera o ultimo caracter, mas no inicio ele considera exato;
print('Exemplo 3:',Frase[9:14])#Comece com o caracter 9 até 13
print('Exemplo 5:',Frase[9])#Print o caracter 9
print('Exemplo 6:',Frase[9:])#Comece considerando a partir do caracter 9 até o final
print('Exemplo 7:',Frase[9:21])#Começa no 9 mas ele considera somente até o 20, lembrando que não temos o caracter 21
print('Exemplo 8:',Frase[0::2])#Comeca em 0 e pula de 2 em 2 até o final
print('Exemplo 9:',Frase[:2])#Começar do inicio Terminar no segundo caracter
print(len(Frase))#Len vem de comprimento e conta quantos caracteres tem na variável Frase
print(Frase.count('o'))#Exemplo 10:' Ele vai contar quantas letras 'o' dentro da variável Frase
print(Frase.find('Vídeo'))#O Python procurou dentro da variável Frase a palavra Vídeo e te informa qual caracter começa a palavra
print(Frase.find('Fábio'))# O Resultado deste exemplo deve ser -1 porque a palavra Fábio não existe dentro de Frase
print('Curso'in Frase)#O Python vai procurar pela palavra 'Curso' em Frase, mas o código 'in' retorna 'Verdadeiro' ou 'Falso', True or False
print(Frase.replace('Python','Mamba Negra'))#O comando replace substitui a palavra 'Python' por 'Mamba Negra'
print(Frase.upper())#Colocar todas as letras em Maiúsculas
print(Frase.lower())#Colocar todas as letras em Minúsculas
print(Frase.capitalize())#Colocar somente a letra em Maiúscula
print(Frase.title())#Colocar somente a primeira letra em Maiúscula de cada palavra
print('Ultimo: {}'.format(Frase))
print(Frase2)#Print Frase2
print(Frase2.strip())#Retirar os espaços da direita e esquerda
print(Frase2.rstrip())#Retirar os espaços da direita
print(Frase2.lstrip())#Retirar os espaços da esquerda, não foi visível neste exemplo
print(Frase.split())#O comando split divide uma cadeia de palavras e várias
print('-'.join(Frase))#Coloca um caracter '-' separando cada caracter da variável