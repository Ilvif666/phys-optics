import matplotlib.pyplot as plt
import numpy as np
from math import cos,pi,sin
def I(x):# анализируемая функция
    return 4*I0*(cos(pi*x*d/(L*lambd)))**2
def Ialt(x,lambd):
    return 2*I0*(1+cos(2*pi*x*d/(lambd*L)))
def V(x):
    return abs(cos((pi*x*d/L)*(1/lambd-1/lambd2)))
def I22(x):
    return 2*I0*(2+cos(2*pi*x*d/(lambd*L))+cos(2*pi*x*d/(lambd2*L)))
def I4(x):
    arg = pi*dx*d/(lambd*l)
    return I0*(1+sin(arg)*cos(2*pi*x*d/(lambd*L))/(arg))
lambd2, lambd, d, L, I0 = 0.68E-6, 0.65E-6, 0.2E-3, 1.3E0, 10
###task1
x = np.arange(-1E-2,1E-2,0.1E-3)
y = [I(each) for each in x]
plt.figure()
plt.plot(x, y)
plt.xlabel("x, м")
plt.ylabel("I, Вт/м^2")
plt.grid(True)
delta = lambd*L/d
print("delta="+str(delta))
###end of task1
###task2p1+p2
x = np.arange(-1E-1,1E-1,0.1E-3)
i22 = [I22(each) for each in x]
v = [V(each) for each in x]
xMin = L/(d*(1/lambd+1/lambd2))
print("xmin="+str(xMin))
plt.figure()
plt.plot(x,v)
plt.xlabel("x, м")
plt.ylabel("V")
plt.grid(True)
plt.figure()
plt.plot(x, i22)
plt.xlabel("x, м")
plt.ylabel("I, Вт/м^2")
plt.grid(True)
###end of task2p1+p2
###task 3
lambdStep, i3, x = 5E-9, np.zeros(2000), np.arange(-1E-1,1E-1,0.1E-3)
while lambd<=lambd2:
    i3 = i3 + np.array([Ialt(each,lambd) for each in x])
    lambd+=lambdStep
plt.figure()
plt.plot(x, i3)
plt.xlabel("x, м")
plt.ylabel("I, Вт/м^2")
plt.grid(True)
###end of task3
###task4
dx, l, x = 1E-3, 0.5, np.arange(-6e-2,6e-2,0.1e-3)
i4 = [I4(each) for each in x]
plt.figure()
plt.plot(x, i4)
plt.xlabel("x, м")
plt.ylabel("I, Вт/м^2")
plt.grid(True)
###end of task4
plt.show()
