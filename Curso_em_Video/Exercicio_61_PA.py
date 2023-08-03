#Refazer o exercicio 51 lendo o primeiro termo e razao de uma PA mostrando os 10 primeiros resultados com a estrutura While
#Retirando os comentários também dá ....
print ('='*50)
print ('   10 TERMOS DE UMA PA - estrutura WHILE')
print ('='*50)
Termo = int(input('Primeiro termo :'))
Razao = int(input('Razão :'))
decimo = Termo + (11-1) * Razao
cont = 0
#Result = Termo
while cont != 10:
      print('{}'.format(Termo), end='->')
     # print('{}'.format(Result), end='->')
      cont = cont + 1
      Termo += Razao
      # ou Result = Result + Razao
print('Finalizado')