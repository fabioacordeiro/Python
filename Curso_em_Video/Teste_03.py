#Estrutura de repetição
#Perguntar se quer continuar ?

while True:
    digi = str(input('Quer continuar [S/N] ? :')).strip().upper()[0]
    if digi in 'SN':
        break
    print('<<<ERRO!!!>> Favor digitar somente S ou N:')
