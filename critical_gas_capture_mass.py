# Written 28/6/17 by dh4gan
# Sketches the critical core mass for rapid gas capture and gas giant planet formation
# See equation 235 of Armitage, arxiv:astro-ph/0701485 for details (and surrounds for derivation)


import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import fsolve,newton


def getTotalMass(Mcore,C):
    
    npoints = len(Mcore)
    minroot = []
    maxroot = []
    coremass = []
    
    for i in range(npoints):
        
        coeff = [C/np.power(Mcore[i],0.6666),0.0,0.0,-1.0,Mcore[i]]

        allroots = np.roots(coeff)
        #print allroots
        allroots = allroots[np.abs(allroots.imag) < 1.0e-30].real 
        #allroots = allroots[allroots.real>1.0e-30].real
        #print Mcore[i], allroots
    
        if allroots !=[]:
            coremass.append(Mcore[i])
            minroot.append(np.amin(allroots))
            maxroot.append(np.amax(allroots))
    
    return coremass, minroot,maxroot

plt.rcParams['font.size']=15
plt.rcParams['lines.linewidth']=2

npoints = int(1.0e5)

# Constant folds in all other physical parameters - 
# the first is tuned to give critical core mass that corresponds to more accurate calculations (~ 10 Earth masses)

C1 = 5e-4
C2 = 5e-3
label1 = 'High $\dot{M}$,$\kappa$'
label2 = 'Low $\dot{M}$,$\kappa$'

# State a core mass (in Earth masses)

Mcore = np.linspace(0.01,12, num=npoints)

# Solve for the total mass
# (C/Mc^2/3) Mt^4 -Mt +Mc = 0

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.set_xlabel('Total Mass ($M_{\oplus}$)')
ax1.set_ylabel('Core Mass ($M_{\oplus}$)')

coremass, minroot, maxroot = getTotalMass(Mcore,C1)
ax1.plot(minroot,coremass, color = 'blue')
ax1.plot(maxroot,coremass,color = 'blue',label=label1)

coremass, minroot, maxroot = getTotalMass(Mcore,C2)
ax1.plot(minroot,coremass, color = 'red')
ax1.plot(maxroot,coremass,color = 'red', label=label2)

ax1.legend(loc='upper left')

plt.show()
fig1.savefig('critical_gas_capture_mass.png')