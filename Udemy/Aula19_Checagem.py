variavel_a = 1 or 0
variabel_b = 0 or 1
print(variavel_a, variabel_b)
#nome = []
nome = input("Digite seu nome: ")
procurar = input("Qual o nome que deseja procurar ?:")
if procurar in nome:
    print(f'{procurar} está em {nome}')
else:
    print(f'{procurar} não está em {nome}')

if procurar not in nome:
    print("nome não localizado")
else:
    print("nome localizado com sucesso !!!")


print('-'*50)
for pos, v in enumerate(nome):
        print(f'Posição: {pos}' , end='')
        #print({v.values})
        print(f' Valor: {(v)}' , end='')
        print()
   
