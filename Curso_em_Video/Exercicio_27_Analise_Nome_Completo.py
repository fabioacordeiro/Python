#Faça um programa que analise o nome completo e mostre:
#Qual o primeiro nome;
#Qual o ultimo nome
nome = str(input('Qual o seu nome completo :')).strip().upper()
nome1 = nome.split()
print('O primeiro nome é {} '.format(nome1[0]))
print ('Seu último nome é {} :'.format(nome1[len(nome1)-1]))
#print('O ultimo nome é {} '.format(nome1.[::]))
#print('A ultima posição da letra A é {}'.format(frase.rfind('A')))