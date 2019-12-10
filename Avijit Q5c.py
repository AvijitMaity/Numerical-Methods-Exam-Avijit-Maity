from scipy.interpolate import *
from scipy.optimize import *
import matplotlib.pyplot as plt
import numpy as np
def f(x):
	theta =  np.loadtxt("D:/New folder/data.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (0))
	d = np.loadtxt("D:/New folder/data.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (1))
	d0 = 370.4
	A = lagrange(theta,d)
	return A(x)-d0
root = bisect(f,f(0.1),f(0.73))
print("The Value of theta at which d = 370.4 is = ",root)