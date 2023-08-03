#Nem sempre 3 retas são capazes de formar um triangulo este programa calcula se é possível
n1 = float(input('Digite o valor do lado a :'))
n2 = float(input('Digite o valor do lado b :'))
n3 = float(input('Digite o valor do lado c :'))
if n1 >= n2 and n1 >= n3 and n1<(n2+n3):
    print ('Sim, as dimensões de abc formam um triângulo')
elif n2>=n1 and n2>= n3 and n2<(n1+n3):
    print ('Sim, as dimensões de abc formam um triângulo')
elif n3>n1 and n3>n2 and n3<(n1+n2):
    print ('Sim, as dimensões de abc formam um triângulo')
else:
    print('Não as dimensões informadas de abc, não formam um triângulo')
print('Lado a:{}'.format(n1))
print ('Lado b:{}'.format(n2))
print('Lado c:{}'.format(n3))
