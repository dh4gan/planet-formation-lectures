# Written 7/6/17 by dh4gan
# Shows the radial velocity of dust grains as a function of stopping time (grain size)
import numpy as np
import matplotlib.pyplot as plt

npoints = 100
ts = np.logspace(-3,3,num=npoints) # stopping time
n = 1.0 # Radial gas pressure gradient
aspect = 0.05 # h/r
eta = n*aspect*aspect# Parameter representing disc radial gas pressure gradient

vr = eta/(ts + 1.0/ts)

print eta

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.set_ylabel(r'$\left|v_r/v_K\right|$',fontsize=22)
ax1.set_xlabel(r'$\tau_{\rm fric}$',fontsize=22)
ax1.set_xscale('log')
ax1.set_yscale('log')

ax1.plot(ts, vr)



# Now attempt to calculate this as a function of grain size (at 1AU)
# (units are cgs)

rhogas = 5e-10
rhodust = 3
vtherm = 2.4e5

yr = 3.15e7
AU = 1.496e13

omega = 2.0*np.pi/yr
vk = omega*AU

a = np.logspace(-4,3)

ts = omega*rhodust*a/(rhogas*vtherm)

vr = vk*eta/(ts + 1.0/ts)

tdrift = AU/(vr*yr)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_ylabel(r'Radial Drift Timescale (years)',fontsize=22)
ax2.set_xlabel(r'$a$ (cm)',fontsize=22)
ax2.set_xscale('log')
ax2.set_yscale('log')

ax2.plot(a, tdrift)

fig1.savefig('radial_drift_velocity.png')
fig2.savefig('radial_drift_timescale.png')

