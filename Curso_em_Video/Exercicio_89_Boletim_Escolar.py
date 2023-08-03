#Crie um programa que leia o nome e duas notas de vários alunos, Perguntar se quer continuar e guarde tudo em uma lista composta.
#No final mostre:
#O boletim com a média de cada um;
#Pergunte, Quer ver a nota de algum aluno individualmente ?
#Permite que o usuário possa mostrar as notas de cada aluno individualmente.
#Ao digitar o número do índice do aluno, mostre os dados do aluno individualmente.
boletim = []
boletimv = []
nomev = ''
n1v = n2v = cont = 0
nome =[]
n1 = []
n2 = []
while True:
    opcao = ''
    nomev = str(input('\033[7;30;46mNome:')).strip().upper()
    nome.append(nomev)
    n1v = float(input('Nota 1:'))
    n1.append(n1v)
    n2v = float(input('Nota 2:'))
    n2.append(n2v)
    nomev = ''
    n1v = 0
    n2v = 0
    boletimv.insert(0,str(nome[0]))
    boletimv.insert(1,float(n1[0]))
    boletimv.insert(2,float(n2[0]))
    boletim.append(boletimv[:])
    boletimv.clear()
    nome.clear()
    n1.clear()
    n2.clear()
    opcao = str(input('Quer continuar [S/N] ? :').strip().upper())
    if opcao == 'N':
        break
    else:
        print('',end='')
print('='*50)
print(f'{"BOLETIM MÉDIAS BIMESTRE":^50}')
print('='*50)
print(f'{"Nº."} {"NOME":^20}   {"MÉDIA":^10}')
print('='*50)
for pos, v in enumerate(boletim):
    print(f'{pos}    {v[0]:^20}  {(v[1]+v[2])/2:^10.2f}')
print('='*50)
nota =0
nota = int(input('Mostrar1 notas de qual aluno ? (999 interrompe):'))
while nota != 999:
    for pos, v in enumerate(boletim):
        if pos == nota:
            print(f'As notas de {v[0]} são [{v[1]}, {v[2]}]')
        else:
            print('', end='')
    print('=' * 50)
    nota = int(input('Mostrar notas de qual aluno ? (999 interrompe):'))
print('Fim')