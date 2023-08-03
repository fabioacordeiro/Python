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
from datetime import datetime, timedelta

inicio = input('Informe o horario de inicio do experimento (formato Horas:Minutos:Segundos): ')
data_inicio = datetime.strptime(inicio, "%H:%M:%S") # transforma a string em data

duracao = input('Quanto tempo durara o experimento (formato Horas:Minutos:Segundos): ')
horas, minutos, segundos = map(int, duracao.split(':'))
# transforma a string em timedelta
duracao = timedelta(hours=horas, minutes=minutos, seconds=segundos)

# soma a data à duração
termino = data_inicio + duracao

# formata o resultado
print(termino.strftime('%H:%M:%S'))

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