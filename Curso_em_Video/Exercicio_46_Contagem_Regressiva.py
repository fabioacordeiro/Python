from time import sleep
for cont in range(10,-1, -1):
    print('\033[4;30;43m {} '.format(cont))
    sleep(0.5)
print('BOOM !!!!')
