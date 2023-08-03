import sched
import random
import operator
import time
#Vencedor = ""
v = ContF = ContL = ContLu = Ta = Pri = 0
Verificar = dict()
#name = dict()
name = ("Fabio", "Lucas", "Luciene", "Tatiane", "Priscila")
scheduler = sched.scheduler(time.time, time.sleep)

for v in range(0,10000):
    v = v + 1
    aleatori = random.choice(name)
    if aleatori == "Fabio":
        ContF = ContF + 1
    if aleatori == "Lucas":
        ContL = ContL + 1
    if aleatori == "Luciene":
        ContLu = ContLu + 1
    if aleatori == 'Tatiane':
        Ta = Ta + 1
    if aleatori == 'Priscila':
        Pri = Pri + 1
    #print(f'Sorteado:{aleatori}')
Verificar = {"Lucas":(ContL),"Fábio":(ContF) ,"Tatiane":(Ta),"Priscila":(Pri), "Luciene":(ContLu)}
Vencedor = (max(Verificar, key = Verificar.get))
#max_key = max(Verificar.items(), key=operator.itemgetter(1))[0]
max_key = max(Verificar.items(), key=operator.itemgetter(1))[1]
print(f'Vencedor(a) ==> {Vencedor}:{max_key}')
print(f'Lucas:{ContL}')
print(f'Fábio:{ContF}')
print(f'Luciene:{ContLu}')
print(f'Tatiane:{Ta}')
print(f'Priscila:{Pri}')
print("Fim")