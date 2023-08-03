#Refazer o exercicio 51 lendo o primeiro termo e razao de uma PA mostrando os 10 primeiros resultados com a estrutura While
#Retirando os comentários também dá ....
print ('='*50)
print ('   10 TERMOS DE UMA PA - estrutura WHILE')
print ('='*50)
Termo = int(input('Primeiro termo :'))
Razao = int(input('Razão :'))
decimo = Termo + (11-1) * Razao
cont = 1
total = 0
mais = 10
while mais != 0:
        total = total + mais
        while cont <= total:
              print('{}'.format(Termo), end='->')
              cont = cont + 1
              Termo += Razao
        print('PAUSA')
        mais = (int(input('Quantos termos você quer mostrar a mais ? :')))
print('Progressão finalizada com {} termos mostrados'.format(total))
