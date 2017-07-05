# Written 28/6/17 by dh4gan
# Computes the isolation mass (in Earth masses) as a function of distance from the star

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size']=15
plt.rcParams['lines.linewidth']=2

npoints = 100
msol = 1.99e33
mearth = 5.972e27
AU = 1.496e13

mstar = 1.0 # solar masses
asnow = 2.7 # Snow line (AU)

C = 2.0*np.sqrt(3.0) # Feeding zone width in Hill Radii (Lissauer 1993)

ap = np.logspace(-1, 2, num=npoints)
sigmap = np.zeros(npoints)
miso = np.zeros(npoints)



for i in range(npoints):
    
    # Compute minimum mass solar nebula (Hayashi 1981)
    
    sigmap[i] = np.power(ap[i],-1.5)
    if(ap[i] <asnow):
        sigmap[i] = 7.1*sigmap[i]
    else:
        sigmap[i] = 30.0*sigmap[i]
        
    # Compute isolation mass (equation 201 of Armitage, arxiv:astro-ph/0701485)
    
    miso[i] = 8.0/np.sqrt(3) *np.power(np.pi*C*sigmap[i],1.5)*np.power(mstar*msol,-0.5)*np.power(ap[i]*AU,3)
    


miso = miso/mearth

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax2 = ax1.twinx()
ax1.plot(ap,miso)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel('Semimajor axis (AU)')
ax1.set_ylabel('Isolation Mass ($M_{\oplus}$)', color='blue')

ax2.plot(ap,sigmap, color='red', alpha=0.3)
ax2.set_yscale('log')
ax2.set_xscale('log')
ax2.set_ylabel(r'Surface Density (g cm$^{-2}$)', color='red')

ax1.axvline(asnow, linestyle='dashed', color='black')
ax1.annotate('Snow Line', xy=(asnow,5.0e1), xytext=(asnow+0.5,5.0e1))

plt.show()
fig1.savefig('isolation_mass.png')