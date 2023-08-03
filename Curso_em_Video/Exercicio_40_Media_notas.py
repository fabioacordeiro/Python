#Crie um programa que leia 2 notas, mostra a média com os critérios abaixo:
#média abaixo de 5.0 está reprovado
#media entre 5 e 6.9 Recuperação
#média 7 ou superior Aprovado
n1 = float(input('Informe a primeira nota :'))
n2 = float(input('Informe a segunda nota :'))
media = (n1+n2)/2
if media >= 7.0:
    print('\033[4;30;44m A sua média final foi de {:.2f}, Aprovado !!!'.format(media))
elif media < 5.0:
    print('\033[4;31m A sua média não foi suficiente, média {:.2f}, REPROVADO !!!'.format(media))
else:
    print ('\033[7;30;43m A sua média foi de {:.2f}, infelizmente não foi suficiente, RECUPERAÇÃO !!!'.format(media))