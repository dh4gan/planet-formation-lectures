# Written 7/6/17 by dh4gan
# Shows the radial velocity of dust grains as a function of stopping time (grain size)

import numpy as np
import matplotlib.pyplot as plt


# First, simply plot the relationship between vr/vk and stopping time for a given set of parameters

npoints = 100
ts = np.logspace(-3,3,num=npoints) # stopping time
n = 1.0 # Radial gas pressure gradient
aspect = 0.05 # disc aspect ratio: H/R
eta = n*aspect*aspect # Parameter representing disc radial gas pressure gradient

vr = eta/(ts + 1.0/ts)

# Now make the plot
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.set_ylabel(r'$\left|v_r/v_K\right|$',fontsize=22)
ax1.set_xlabel(r'$\tau_{\rm fric}$',fontsize=22)
ax1.set_xscale('log')
ax1.set_yscale('log')

ax1.plot(ts, vr)


#
# Now calculate dust radial velocity as a function of grain size (at 1AU)
# (units are cgs)
#

rhogas = 5e-10 # g cm^-3
rhodust = 3 # g cm^-3
vtherm = 2.4e5 # cm s^-1

yr = 3.15e7 # year in seconds
AU = 1.496e13 # AU in cm

omega = 2.0*np.pi/yr # Assuming a solar mass star, so orbital period at 1 AU = 1 year
vk = omega*AU

a = np.logspace(-4,3) # logarithmic range of grain sizes

ts = omega*rhodust*a/(rhogas*vtherm)  # Stopping time in the Stokes regime

vr = vk*eta/(ts + 1.0/ts) # Now use this stopping time to calculate vr

tdrift = AU/(vr*yr) # Drift timescale at this velocity from 1 AU (converting to years)

# Now plot it

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_ylabel(r'Radial Drift Timescale (years)',fontsize=22)
ax2.set_xlabel(r'$a$ (cm)',fontsize=22)
ax2.set_xscale('log')
ax2.set_yscale('log')

ax2.plot(a, tdrift)

# Save both figures
fig1.savefig('radial_drift_velocity.png')
fig2.savefig('radial_drift_timescale.png')

