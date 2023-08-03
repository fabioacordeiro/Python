from datetime import datetime


time_1 = datetime.strptime('05:00:00',"%H:%M:%S")
time_2 = datetime.strptime('10:00:00',"%H:%M:%S")

time_interval = time_2 - time_1
print(time_interval)

#data_program = ('17/03/2022 16:47')
data_program = datetime.strptime('17/03/2022 16:47', "%d/%m/%Y %H:%M")
data_programada = data_program

print(data_programada)