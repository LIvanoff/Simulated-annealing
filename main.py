import time
import matplotlib.pyplot as plt
import numpy as np
import random
import math
from scipy.interpolate import interp1d

def func(x):
    return (79/13440*x**7 - 1301/8064*x**6 + 23189/13440*x**5 - 72623/8064*x**4 + 26133/1120*x**3 - 53843/2016*x**2 + 2747/280*x +4)

def print_func():
    plt.clf()
    plt.plot(xnew, f(xnew), '--')
    plt.plot(x, y, 'bo')
    if i > 1:
        plt.plot(last_x, last_y, 'co', label='подходившие точки', markersize=9)

    if i != 10:
        plt.plot(x[i + 1], y[i + 1], 'ro', label='проверяемая точка', markersize=9)

    plt.plot(target_x, target_y, 'go', label='подходящая точка', markersize=9)
    plt.legend(loc='best', fancybox=True, shadow=True)
    plt.draw()
    plt.gcf().canvas.flush_events()


x = np.array([0, 0.8, 1.2, 2, 3, 4, 5.1, 6, 7, 7.57, 8])
y = func(x)
last_x = []
last_y = []
f = interp1d(x, y, kind='cubic')
xnew = np.linspace(0, 8, num=100, endpoint=True)

T = 100
delta_y = 0
target_x = x[0]
target_y = y[0]

plt.ion()
for i in range(11):
    print_func()
    time.sleep(2)
          #алгоритм отжига
    ##############################
    if i !=10:
        delta_y = y[i + 1] - y[i]
        T = T / (i + 1)
        if delta_y > 0 and (random.randint(1, 100)) < (100 * math.e ** (-delta_y / T)):
            target_x = x[i + 1]
            last_x.append(x[i + 1])
            target_y = y[i + 1]
            last_y.append(y[i + 1])
        else:
            target_x = x[i + 1]
            last_x.append(x[i + 1])
            target_y = y[i + 1]
            last_y.append(y[i + 1])
    ###############################

plt.ioff()
plt.show()
