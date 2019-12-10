import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dn/dt
def model(n,t):
    k = 1.5   #Here k is the decay constant
    dndt = -k * n
    return dndt

# initial condition
n0 = 10 # At t=0 number density of the patticles is n0=10 cm^-3

# time points
t = np.linspace(0,10)

# solve ODE
n = odeint(model,n0,t)

# plot results
plt.plot(t,n, color=(0.7,0.5,0.3))
plt.xlabel('time in s')
plt.ylabel('n(t) cm^-3')
plt.tick_params(labelsize=18)
plt.title('Radioactive Decay(Avijit Maity)', size=24)
plt.grid()
plt.show()

