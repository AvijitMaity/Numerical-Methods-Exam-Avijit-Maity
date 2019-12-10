'''
This program shows the Graph of the mass as a function of distance from the center out to 10.
If we consider a elementary shell of radius x and thickness dx then mass of the element is = 4*pi*p*x^2* dx
Then if we integrate this we will get the desired result.
'''
from scipy.integrate import *
from numpy import *
import matplotlib.pyplot as plt

p = 10.0  # Here p is the density of the spherically mass distribution of matter


def f(x):
    return  10*4 * pi * x * x


x = linspace(0, 10, 1000)
M = []
for i in x:
    m = romberg(f, 0, i)
    M = append(M, m)

plt.plot(x, M, color=(1.0,0.0,0.0))
plt.xlabel("Distance in meter from the centre of the distribution(x)")
plt.ylabel("mass in kg")
plt.title("Graph of mass distribution as a function of x")
plt.grid()
plt.show()


