#from math import *
#print('cosseno de 0: ', cos(0))
# this sets up the Matplotlib interactive windows:
#%matplotlib widget
# this changes the default date converter for better interactive plotting of dates:
#plt.rcParams['date.converter'] = 'concise'

from matplotlib import pyplot as plt
x = []
y = []
for i in range(100):
    if i != 0:
       if 100/i !=1:
         x.append(i)
         y.append(x[i-1]**2)
plt.plot(x,y)
plt.show()

