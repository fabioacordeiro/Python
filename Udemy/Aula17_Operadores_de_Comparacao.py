"""
Operadores de comparação relacionais
OP......Significado.........Exemplo(True)
> .....maior...............2>1
>= ....maior igual ........2>=2
< .....menor...............2<3
<= ....menor igual ........3<=3
== ....igual ..............3==3
!= ....diferente ..........3!=4

"""
a = 1
b = 2
c = 3
if a > b:
    print(f'a é maior que b')
elif a < b:
    print('b é maior que a onde b vale {} e a vale {}' .format(b,a))
elif a == b:
    print(" a e b são iguais e valem".format(a))
else:
    print("Não foi possível a comparação")

if a >= b:
    print("Os valores de a são maiores ou iguais a b")
elif a <= b:
    print("Os valores de a são menores ou iguais a b")

if a != b:
    print("Os valores de a e b são diferentes")
else:
    print("Os valores são confusos")
print("Fim")
