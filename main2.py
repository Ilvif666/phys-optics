import matplotlib.pyplot as plt
import numpy as np
from math import cos,pi,sin,sqrt
def I(x):# анализируемая функция
    sin_phi = x/sqrt(x**2+L**2)
    u = pi*b*sin_phi/lambd
    return I0*(sin(u)/u)**2
def I2(x):
    sin_phi = x/sqrt(x**2+L**2)
    return I(x)*((sin(N*pi*d*sin_phi/lambd))/(sin(pi*d*sin_phi/lambd)))**2
def I4(x):
    arg = pi*dx*d/(lambd*l)
    return I0*(1+sin(arg)*cos(2*pi*x*d/(lambd*L))/(arg))
N, lambd, b, L, I0, d = 3, 0.5E-6, 0.02E-3, 1.5E0, 10, 50E-6
###task1
x = np.arange(-12E-2,12E-2,1E-3)
y = [I(each) for each in x]
plt.figure()
plt.plot(x, y)
plt.title("I(x)")
plt.xlabel("x, м")
plt.ylabel("I, Вт/м^2")
plt.grid(True)
#ширина полосы
delta  = lambd*L/b
print("delta="+str(delta))
###end of task1
###task2
x = np.arange(-1E-1,1E-1,0.1E-3)
i2 = [I2(each) for each in x]
#Определяем отношение интенсивностей главных и побочных максимумов
print("Igl/Ipob="+str(N**2))
plt.figure()
plt.plot(x,i2)
plt.title("I(x)")
plt.xlabel("x, м")
plt.ylabel("I, вт/м^2")
plt.grid(True)
###end of task2
###task 3
lambd, d, b = 500E-9, 10E-6, 2E-6
i3 = [I2(each) for each in x]
plt.figure()
plt.plot(x, i3)
plt.title("I(x)")
plt.xlabel("x, м")
plt.ylabel("I, Вт/м^2")
plt.grid(True)
###end of task3
plt.show()
