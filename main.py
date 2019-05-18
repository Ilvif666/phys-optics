#график зависимости интенсивности света от координаты для интерференционной схемы юнга
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
from math import cos,pi

def I(x):# анализируемая функция
    lambd, d, L, I0 = 0.65E-6, 0.2E-3, 1.3E0, 10
    return 4*I0*(cos(pi*x*d/(L*lambd)))**2

x = np.arange(-2E-2,2E-2,0.1E-3)
y = [I(each) for each in x]
yy = np.arange(0,4*10+1,1)
yAlt = [str(round(each/10,1))+"I0" for each in yy]
yDic = dict(zip(yAlt, y))
ax = plt.axes()
plt.plot(x, y)
plt.xlabel("x, м")
plt.ylabel("I, интенсивность")
plt.grid(True)
plt.yticks(range(len(yDic)),list(yDic.keys()))

plt.show()
