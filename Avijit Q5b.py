from scipy.interpolate import *
import matplotlib.pyplot as plt
import numpy as np
theta =  np.loadtxt("D:/New folder/data.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (0))
d = np.loadtxt("D:/New folder/data.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (1))
f = lagrange(theta,d)
plt.plot(theta, d, 'ro', ms=5)
thetas = np.linspace(0.1,10,100 )
plt.xlabel("Theta")
plt.ylabel("d")
plt.title("Plotting of the theorist's data and curve")
plt.plot(thetas, f(thetas), color = (0.2,0.5,0.7), ls = '-',lw=2, alpha=0.7,label = 'interpolated data')
plt.grid()
plt.show()