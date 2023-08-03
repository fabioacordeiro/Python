import time
import sched
import random
from datetime import datetime, date

data_atual = date.today()


print('Aguarde !!!!')
name = ("Fabio", "Lucas", "Luciene", "Tatiane", "Priscila")
scheduler = sched.scheduler(time.time, time.sleep)

def sorteio():
    aleatori = random.choice(name)
    print(f'Sorteado:{aleatori} => Data: {time.ctime()}')
    scheduler.enter(1,1, sorteio, ())


def sche():
    scheduler.enterabs(datetime(year=2022, month=3, day=17, hour=11, minutes=49),1,sorteio, ())



sche()
scheduler.run()
