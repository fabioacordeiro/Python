import calendar

print(70*'-')
mes = calendar.month(2023, 2)
print(mes)
mes1 = calendar.monthrange(2023, 2)
print(70*'-')
print(f'Qtde de dias do Mês Fevereiro/2023:{mes1}')
mes2 = calendar.monthrange(2024, 2)
print(f'Qtde de dias do Mês Fevereiro/2024:{mes2}')
print(70*'-')
calendario = calendar.calendar(2023)
print(calendario)
print(70*'-')
print(list(enumerate(calendar.day_name)))
print(70*'-')
for week in calendar.monthcalendar(2023, 4):
    print(week)
