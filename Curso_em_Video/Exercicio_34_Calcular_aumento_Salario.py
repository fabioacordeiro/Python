Salario = float(input('Qual o salário atual ? R$:'))
if Salario > 1250:
    Salnovo =Salario + (Salario * 0.10)
    print('O novo salário com reajuste de 10% é de R$ {:.2f}'.format(Salnovo))
else:
    Salnovo = Salario + (Salario * 0.15)
    print('O novo salário com reajuste de 15% é de R${:.2f}' .format(Salnovo))