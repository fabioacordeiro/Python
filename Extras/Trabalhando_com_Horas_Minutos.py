#Em Python, uma duração é representada por timedelta,
#  enquanto datas e horas são representadas por datetime.
'''
Ou seja, você precisa transformar a primeira string em data,
usando strptime em vez de strftime 
(repare no "p" em vez de "f" no nome 
- isso porque parsing é o processo de transformar uma string em uma data,
 e formatação é o processo oposto).
'''
import time
from pathlib import Path
from datetime import timedelta, datetime
'''
Hora = {time.strftime("%H:%M")}
print(f'Agora são: {Hora}')
print('Informe até que horas deseja gravar:')
hora = input('Hora: ')
minuto = input('Minutos: ')
Horafim1 = 
Horafim = hora+':'+minuto
Horafim = datetime.strptime(Horafim, "%H:%M")
Horafim1 = (time.strptime(Horafim, format)[-8:5])
print(Horafim1)
print(Horafim)
'''
###########################################################################
#Data e hora atual
print(60*'-')
print(f'{"Data e Hora do sistema com - datetime.now() biblioteca datetime ":^60}')
print(datetime.now())
print(60*'-')
print(f'{"Formatando a variavel com - datetime.strftime(hora, %D/%M/%Y %H:%M) biblioteca datetime ":^60}')
hora = datetime.now()
hora = datetime.strftime(hora, "%d/%m/%Y %H:%M")
print(f'Agora são: {hora} do tipo {type(hora)} variável hora')
hora1 = datetime.strptime(hora, "%d/%m/%Y %H:%M")
print(f'Agora são: {hora1} do tipo {type(hora1)} variável hora1')
print(60*'-')
#Hora do sistema
print(f'{"Hora do sistema com - {time.strptime(%H:%M)} biblioteca datetime ":^60}')
Hora = {time.strftime("%H:%M")}
print(Hora)
print(f'Agora são: {Hora} do tipo {type(Hora)} variável Hora')
print(60*'/')
print(f'Agora são:\033[0;33;44m: {hora1} \033[0m :do tipo {type(hora1)} variável hora1')
print('Informe o tempo de gravação em horas e minutos (formato Horas:Minutos).')
h = int(input('Informe primeiro a quantidade de horas:'))
m = int(input('Informe primeiro a quantidade de minutos:'))
segundos = 30
fim = timedelta(hours=h, minutes=m, seconds=segundos)
Tfinal = hora1 + fim
print(f'Tfinal:{Tfinal.strftime("%H:%M:%S")}')
print(f'Tipo do Tfinal:{type(Tfinal)}')
print(f'Valor completo do Tfinal:{Tfinal}')


inicio = input('Informe o horario de inicio do experimento (formato Horas:Minutos:Segundos): ')
data_inicio = datetime.strptime(inicio, "%H:%M:%S") # transforma a string em data

duracao = input('Quanto tempo durara o experimento (formato Horas:Minutos:Segundos): ')
horas, minutos, segundos = map(int, duracao.split(':'))
# transforma a string em timedelta
duracao = timedelta(hours=horas, minutes=minutos, seconds=segundos)

# soma a data à duração

termino = data_inicio + duracao
print(f'Agora: {data_inicio} do tipo {type(data_inicio)} data_inicio')
print(f'Agora: {duracao} do tipo {type(duracao)} variável duracao')
print(f'Agora: {termino} do tipo {type(termino)} variável termino')
#termino = Hora + duracao

# formata o resultado
print(f'Término:{termino.strftime("%H:%M:%S")}')
print(f'Tipo do termino:{type(termino)}')

#####################Fazendo um looping #######################################3
'''
from datetime import datetime, timedelta

while True:
    try:
        inicio = input('Informe o horario de inicio do experimento (formato Horas:Minutos:Segundos): ')
        data_inicio = datetime.strptime(inicio, "%H:%M:%S")
        break
    except ValueError:
        print('Não foi digitada uma data válida no formato hh:mm:ss')

while True:
    try:
        duracao = input('Quanto tempo durara o experimento (formato Horas:Minutos:Segundos): ')
        horas, minutos, segundos = map(int, duracao.split(':'))
        duracao = timedelta(hours=horas, minutes=minutos, seconds=segundos)
        break
    except ValueError:
        print('Não foi digitada uma duração no formato hh:mm:ss')

termino = data_inicio + duracao
print(termino.strftime('%H:%M:%S'))

'''