# Written 30/05/17 by dh4gan
# Evolves the solution for a viscous ring

import numpy as np
from scipy.special import iv
import matplotlib.pyplot as plt


R0 = 1
m = 1

def sigmafunction(x,t):
    sigma = m/(np.pi*R0*R0)*np.power(x,-0.25)*np.power(t,-1)*np.exp(-(1+x*x)/t)*iv(0.25,2.0*x/t)
    return sigma
    

nx = 200
nt = 15


#t = [0.004,0.016,0.064,0.256]
#nt = len(t)

x = np.linspace(0.001,2, num=nx)
t = np.linspace(1.0e-4,0.2,num=nt)

sigma = np.zeros(nx)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.set_xlabel('$R/R_0$', fontsize=22)
ax1.set_ylabel(r'$\Sigma/\Sigma_0$',fontsize=22)

for it in range (nt):
    print t[it]
    color_shade = [1-float(it+1)/float(nt),0,float(it+1)/float(nt)]
    #print color_shade
    
    for ix in range(nx):
        sigma[ix] = sigmafunction(x[ix],t[it])
    
    ax1.plot(x,sigma, color = color_shade)
    
plt.show()
fig1.savefig('viscous_ring.png')
    
    


