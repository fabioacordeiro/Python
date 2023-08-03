#Faça um programa que o usuáio informe o Nome, Ano de nascimento, CTPS, Ano de Contratação e salário e cadastre-os com a idade
# em um dicionário, Calcule e acrescente com quantos anos a pessoa vai se aposentar se a CTPS for diferente de zero:
#O programa vai mostrar no final:
#Nome:
#Idade:
#CTPS:
#Contratação:
#Salário:
#Aposentadoria
from datetime import date
atual=date.today().year
dados = {}
print('\033[7;30;42m='*50)
dados['Nome'] = str(input('Nome: ')).strip().upper()
nasc = int(input('Ano de nascimento:'))
dados['idade'] = (atual - nasc)
dados['ctps'] = int(input('CTPS (0 = não tem):'))
if dados['ctps'] !=0:
    dados['contratação'] = int(input('Ano de Contratação:'))
    dados['salário'] = float(input('Salário R$:'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação']+35) - atual)
print('\033[7;30;42m='*50)
print(f'{"PROJEÇÃO":^50}')
for k, v in dados.items():
    if k == 'idade':
        print(f'==>{k}: {v} anos')
    elif k == 'salário':
        print(f'==>{k}: R$ {v}')
    elif k == 'aposentadoria':
        print(f'==>{k}: {v} anos')
    else:
        print(f'==>{k}: {v}')
print('='*50)

