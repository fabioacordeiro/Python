import schedule
import time

def f():
    print("Hello World")

schedule.every().hour.do(f)

while True:
    schedule.run_pending()
    time.sleep(1)