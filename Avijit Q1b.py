
from numpy import *
from scipy import integrate
def f(x):
    return 10*4 * pi * x * x

x = arange(0,10,0.0001)
y = f(x)
A= integrate.simps(y,x)
print('The value of the mass enclosed in a sphere of radius 10m is =', A)