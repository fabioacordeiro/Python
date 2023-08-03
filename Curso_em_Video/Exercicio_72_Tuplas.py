#Faça um programa que tenha uma tupla e leia os números do 0 ao 20, ao ler o número digitado informe o número por extenso
#Validar a digitação de 0 a 20
n1 = (0, 'Zero', 1, 'Um',2, 'Dois',3,'Três',4,'Quatro', 5, 'Cinco', 6 ,'Seis', 7, 'Sete', 8, 'Oito', 9,'Nove', 10,'Dez')
n2 = (11, 'Onze',12, 'Doze',13,'Trese',14,'Catorze', 15, 'Quinze', 16, 'dezesseis', 17, 'Dezessete', 18, 'Dezoito', 19,'Dezenove', 20,'Vinte')
cont = ('Zero','Um','Dois','Três','Quatro', 'Cinco','Seis', 'Sete', 'Oito','Nove','Dez',
        'Onze', 'Doze','Trese','Catorze', 'Quinze','dezesseis',  'Dezessete', 'Dezoito', 'Dezenove','Vinte')
ver = 'S'
while ver not in 'N':
    while True:
        num = int(input('Qual o número:'))
        if 0<= num <=20:
            break
        print('Tente novamente ! ',end='')
    print(f'Você digitou {cont[num]}')
    ver = str(input('Quer continuar [S/N] ? :')).strip().upper()
print('Fim')

