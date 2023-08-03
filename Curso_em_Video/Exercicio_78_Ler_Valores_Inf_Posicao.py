#Faça um programa que leia 5 valores digitados mostre:
#A lista digitada:
#O maior valor e todas as posições caso foi digitado mais de uma vez:
#O menor valor e todas as posições caso foi digitado mais de uma vez:
cont =0
valores = []
for v in range(0,5):
    cont = cont + 1
    Digitado = int(input(f'Digite um valor para Posição {v}:'))
    valores.append(Digitado)
print(f'Você digitou os valores:{valores}')
menor = min(valores)
maior = max(valores)
print(f' O menor valor é {menor} na(s) posição(ões)', end='')
for pos, v in enumerate(valores):
    #print(f'O menor valor é:{menor}')
    if v == menor:
        print(f' {pos}',end='...')
print(f'\n O maior valor é {maior} na(s) posição(ões)' ,end='')
for pos, v in enumerate(valores):
    #print(f'O menor valor é:{menor}')
    if v == maior:
        print(f' {pos}',end='...')

