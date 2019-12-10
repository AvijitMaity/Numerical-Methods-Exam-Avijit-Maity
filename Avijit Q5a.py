from scipy.interpolate import *
import matplotlib.pyplot as plt
import numpy as np
theta =  np.loadtxt("D:/New folder/data.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (0))
d = np.loadtxt("D:/New folder/data.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (1))
x = int(input("Enter a point to find the value of d"))
print("The value of d is =",lagrange(theta,d)(x))
