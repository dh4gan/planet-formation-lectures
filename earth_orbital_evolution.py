# Written 10/7/17 by dh4gan
# Reads in output from https://data.giss.nasa.gov/ar5/srorbpar.html
# From Berger (1978)'s solution for Earth's orbital parameters

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('Earth_orbital_parameters.txt', skiprows = 6)
print plt.rcParams.keys()

plt.rcParams['font.size']=18
plt.rcParams['lines.linewidth']=2

print plt.rcParams.keys()

time = data[:,0]
ecc = data[:,1]
obliq = data[:,2]
longper = data[:,3]


fig1,axarr = plt.subplots(3, sharex=True, figsize=(10,10))
axarr[0].set_ylabel('$e$')
axarr[0].plot(time,ecc, color='blue')

axarr[1].set_ylabel('$\psi$ (deg)')
axarr[1].plot(time,obliq, color='red')

axarr[2].set_ylabel('$\omega$  (deg)')
axarr[2].set_xlabel('Time (years)')
axarr[2].plot(time,longper,color = 'green')

plt.show()

fig1.savefig('earth_orbital_parameters.png')

