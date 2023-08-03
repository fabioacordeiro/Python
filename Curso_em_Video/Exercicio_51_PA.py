#Faça um programa que leia o "0 primeiro termo" e a "Razão" de uma PA e escreva 10 resultados;
print ('='*50)
print ('   10 TERMOS DE UMA PA - estrutura FOR ')
print ('='*50)
Termo = int(input('Primeiro termo :'))
Razao = int(input('Razão :'))
decimo = Termo + (11-1) * Razao
for cont in range (Termo,decimo, Razao):
    print ('{}'.format(cont),end='->')
print('Finalizado')
