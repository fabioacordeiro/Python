#Faça um progrma que analise a frase e mostre:
#Quantas letras A parece na frase;
#Qual a posicão da primeira letra A
#Qual a localização da ultima letra A
frase = str(input('Digite uma frase qualquer para analisar :')).strip().upper()
#print('A letra A aparececeu  :', end='')
#print(frase.count('A'), end='')
#print(' vezes')
print('A letra A aparececeu {} vezes na frase'.format(frase.count('A')))
print('A primeira posição da letra A é {}'.format(frase.find('A')))
print('A ultima posição da letra A é {}'.format(frase.rfind('A')))