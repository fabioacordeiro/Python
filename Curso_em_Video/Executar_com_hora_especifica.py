from datetime import datetime

#data_program = datetime.strptime('17/03/2022 16:47', "%d/%m/%Y %H:%M")

data_program = datetime.strptime('17/03/2022 17:49', "%d/%m/%Y %H:%M")
data_programada = data_program

print(f'data_programada:{data_programada}')

print(f'data_program:', type(data_program))
data_atual = datetime.now()
print(f'data_atual: {data_atual}')
#print(data_atual[0])
#print(f'data2: {data_atual}')
Data_System2 = datetime.strptime(data_atual,"%d/%m/%Y %H:%M")
print(f'data2:', type(Data_System2))


#Data_System = data_atual.strftime('%d/%m/%Y %H:%M')
#Data_System2 = datetime.strptime(data_atual, "%d/%m/%Y %H:%M")
#print(type(Data_System2))
#print(f'Data_System2:', type(Data_System2))

'''
while True:
    if Data_System >= Data_System:
        print(f'Executei às {Data_System},data e horário programado: {data_programada}')
        Dif_Time = Data_System - data_program
        print(f'Diferença {Dif_Time}')
        break
'''
print('Fim')


