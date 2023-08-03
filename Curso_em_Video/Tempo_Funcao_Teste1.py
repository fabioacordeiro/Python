import time
import sched
import random
#name = list()
name = ("Fabio", "Lucas", "Luciene", "Tatiane", "Priscila")
scheduler = sched.scheduler(time.time, time.sleep)

def sorteio():
    aleatori = random.choice(name)
    print(f'Sorteado:{aleatori} => Data: {time.ctime()}')
    scheduler.enter(1,1, sorteio, ())

sorteio()
scheduler.run()
