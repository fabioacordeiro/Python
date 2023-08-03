from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pytz import timezone

data = datetime(2023, 11, 4, 18, 42, 33)
data1 = '1975-12-20 09:30:33'
data2 = datetime.strptime(data1, '%Y-%m-%d %H:%M:%S')
data_machine = datetime.now()
# é o número de segundos preciso de 1970 até o momento
segundos = data.timestamp()
ts = datetime.fromtimestamp(segundos)
print(f'data:{data}')
print(f'data2:{data2}')
print(f'Data_sistema:{data_machine}')
print(
    f'Número de segundos exato de 1970 até agora que representa uma data:{ts}')
rest = (data_machine - data2)
print(f'diferença entre duas datas:{rest}')
print(
    f'diferença entre duas datas:{rest.days, rest.seconds, rest.microseconds}')
print(f'total de segundos{rest.total_seconds()}')
print(60*'-')
print(f'{"Criando um Time Delta ou diferença de tempo":.^60}')
deltad = timedelta(days=10)
umdia = timedelta(days=1)
umano = timedelta(days=365)
deltaW = timedelta(weeks=1)
umdiah = timedelta(hours=24)
deltaf = data_machine + deltad
delta = deltaf - relativedelta(dt1=data_machine)
dt = '2132-04-04'
dt2 = datetime.strptime(dt, '%Y-%m-%d')
dt3 = dt2 + relativedelta(days=20)
dt4 = dt2 + relativedelta(weeks=1)
delta1 = relativedelta(data_machine, data2)
dfy = delta1.years
dfd = delta1.days
dfw = delta1.weeks
print(f'Diferença de datas {dt2} e {data_machine}:{dt2 - data_machine}')
print(f'Somando mais 20 dias em {dt2} :{dt3}')
print(f'Somando mais 1 semana em {dt2} :{dt4}')
print(f'Tempo restante em 10 dias: {deltaf}')
print(f'Tempo restante em 1 semana: {deltaW}')
print(f'Diferença entre 2 datas: {delta}')
print(f'Diferença em anos entre 2 datas: {data2} e {data_machine}: {dfy}')
print(f'{"Observe que ele traz somente a diferença de um mês para outro":.^80}')
# Observe que ele traz somente a diferença de dias considerando o ano
print(f'Diferença de dias entre 2 datas: {data2} e {data_machine}: {dfd}')
print(f'Diferença de semanas entre 2 datas: {data2} e {data_machine}: {dfw}')
