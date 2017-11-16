# Written 30/05/17 by dh4gan
# Evolves the standard solution for a viscous annular ring
#

import numpy as np
from scipy.special import iv
import matplotlib.pyplot as plt


R0 = 1
m = 1

def sigmafunction(x,t):
    sigma = m/(np.pi*R0*R0)*np.power(x,-0.25)*np.power(t,-1)*np.exp(-(1+x*x)/t)*iv(0.25,2.0*x/t)
    return sigma
    
# Set up range of positions

nx = 200
x = np.linspace(0.001,2, num=nx)

# Set number of timesteps to plot at
nt = 15
t = np.linspace(1.0e-4,0.2,num=nt)

sigma = np.zeros(nx)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.set_xlabel('$R/R_0$', fontsize=22)
ax1.set_ylabel(r'$\Sigma/\Sigma_0$',fontsize=22)

for it in range (nt):
    print "Plotting t=",t[it]
    
    # Colour shade gradually goes from red to blue with time
    color_shade = [1-float(it+1)/float(nt),0,float(it+1)/float(nt)]
    
    for ix in range(nx):
        sigma[ix] = sigmafunction(x[ix],t[it])
    
    ax1.plot(x,sigma, color = color_shade)
    
plt.show()
fig1.savefig('viscous_ring.png')
    
    


