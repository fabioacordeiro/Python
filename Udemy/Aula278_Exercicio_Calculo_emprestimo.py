# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime, timedelta

emprestimo = 1000000
parcela = round((emprestimo/60), 2)
dt_ini = ('2020-20-12 11:20:33')
dt_inicio = datetime.strptime(dt_ini, '%Y-%d-%m %H:%M:%S')
print(f'Data início:{dt_inicio}')
dt_f = ('2025-20-12 11:20:33')
dt_fim = datetime.strptime(dt_f, '%Y-%d-%m %H:%M:%S')
print(f'Data Fim:{dt_fim}')
delta = (dt_fim - dt_inicio)
dia = timedelta(days=1)
dt = dt_inicio + dia
print(dt)
print(f'Tempo em dias:{(delta.days)}')
print(f'Tempo em meses:{(delta.days)/30}')
print(f'Valor total:{parcela}')
count = 0
tt = 0
while True:
    dt = dt + dia
    dtv = datetime.strftime(dt, '%d')
    dti = datetime.strftime(dt, '%d/%m/%Y')
    if dtv == '20':
        print(f'Data de pagamento:{dti} valor: {parcela}')
        count += 1
        tt = tt + parcela
    if dt >= dt_fim:
        break
print(f'Total de parcelas {count} e valor tt recebido {tt}')

# data = datetime(2023, 11, 4, 18, 42, 33)
