from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pytz import timezone

data = datetime(2023, 11, 4, 18, 42, 33)
data1 = '1975-04-15 09:30:33'
data2 = datetime.strptime(data1, '%Y-%m-%d %H:%M:%S')
# Para formatar a data usamos o strftime
print(70*'-')
print(f'{" datetime.strptime":.^70}')
print(f'Data criada com datetime.strptime: {data2}')
print(70*'-')
print(f'{" datetime.strftime":.^70}')
dataf = datetime.strftime(data2, '%d/%m/%Y %H:%M:%S')
datahm = datetime.strftime(data2, '%d/%m/%Y %H:%M')
datay = datetime.strftime(data2, '%Y')
datadm = datetime.strftime(data2, '%d/%m')
datah = datetime.strftime(data2, '%H:%M')
print(70*'-')
print(f'Data formatada com datetime.strftime: {dataf}')
print(f'Lembrando que os dados formatados são Strings')
print(f'Data e hora: {datahm}')
print(f'Ano: {datay}')
print(f'Dia e mês: {datadm}')
print(f'Hora e minuto: {datah}')
print(f'{"Observe que ele traz somente a diferença de um mês para outro":.^80}')
# print(f'Diferença de semanas entre 2 datas: {data2} e {data_machine}: {dfw}')
