#! /usr/bin/env python

import argparse
from subprocess import *
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import special
from scipy.interpolate import UnivariateSpline
from scipy.optimize import curve_fit

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.markersize'] = 10
# comment the below line because it also change the circle edge width
#mpl.rcParams['lines.markeredgewidth'] = 3 # plus cross marker
mpl.rcParams['axes.labelsize'] = 22
mpl.rcParams['axes.titlesize'] = 22
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
#legend
#mpl.rcParams['legend.fancybox'] = True
mpl.rcParams['legend.numpoints'] = 2 #default 2
mpl.rcParams['legend.fontsize'] = 18
#figure width or height
mpl.rcParams['figure.subplot.left'] = 0.175 #default 0.125
mpl.rcParams['figure.subplot.bottom'] = 0.15 #default 0.1
mpl.rcParams['figure.figsize'] = 10, 7.5 #default 8, 6

datafail = [3.4]*4
datafaily = [0.85, 0.7, 0.3, 0.5]

datax = np.array([ 3.6, 3.8, 4.0, 4.2, 4.0, 4.0, 4.2, 4.0, 3.8,4.2, 3.6, 3.6, 3.8, 4.0, 3.8, 3.4])
datay = np.array([0.85]*4+[0.75, 0.9, 0.7, 0.7, 0.75,0.6, 0.75]+[1.0]*3+[0.7, 1.0])

data_gel = [ 4.4,  5,  4.4, 4.2, 4.4, 4.4]
data_gely = [ 0.85, 0.85, 0.7, 1.0, 0.3, 0.5]

data_samosa = np.array([3.8, 3.8, 3.6,4.2,4.0, 3.6, 4.2,3.8, 3.8, 4.2])
data_samosay = np.array([0.5, 0.3, 0.3,0.6, 0.6, 0.6, 0.5, 0.6, 0.7, 0.3])

data_cyl = [3.6, 3.6,4.0, 4.0, 4.0, 4.0, 4.2, 3.8, 3.6, 3.8, 4.2]
data_cyl_y = [0.5, 0.7, 0.5, 0.6,0.3, 0.7, 0.5, 0.75, 0.75, 0.3, 0.3]



print datax
fig1 = plt.figure()


plt.plot(datafail, datafaily, marker='v', markersize=20, label='no assembly', linestyle='None', color='blue')

plt.plot(data_gel, data_gely, marker='^', markersize=20, label='gel', linestyle='None',color='m')
plt.plot(data_samosa, data_samosay, marker='s', markersize=20, label='"samosa"', linestyle='None')
plt.plot(data_cyl, data_cyl_y, marker='o', markersize=20, label='cylinders', linestyle='None')
plt.plot(datax, datay, marker='*', markersize=24, label='BMC', linestyle='None', color='gold')
axes = plt.gca()
#axes.set_xlim([0, 3.4])
plt.legend(loc=0)
plt.xlabel(r'$\epsilon_{hh}$')
plt.ylabel(r'$\epsilon_{ph}/\epsilon_{hh}$')
plt.savefig('phase_diag.png')
plt.show()
'''
fig2 = plt.figure()
plt.plot(data[:,0], data[:,1]/data[:, 3], linestyle='--', marker='s', markersize=10, label='DHBj')
plt.show()

start = 10
end = 400
x = data1[0][start:end, 0]
y1 = []
y2 = []
for i in range(num_files):
    y1.append(data1[i][start:end, 1])
    y2.append(data2[i][start:end, 1])


# Four axes, returned as a 2-d array
salt_label=['0.3M', '0.5M', '1M-no spline', '1M-spline', '1M-SPCE', '3M']
f, axarr = plt.subplots(1, 2, sharey=True, sharex=True)
for i in range(num_files):
    axarr[0].plot(x, y1[i], linewidth=2, label=salt_label[i])
    axarr[1].plot(x, y2[i], linewidth=2, label=salt_label[i])

axarr[0].set_title('A')
axarr[1].set_title('B')
axarr[0].set_ylim(-2, 8)
axarr[0].set_ylabel('Potential Energy/kT')
axarr[0].set_xlabel('Distance (nm)')
h_legend1 = axarr[0].legend(prop={'size': 18})
h_legend2 = axarr[1].legend(prop={'size': 18})
axarr[0]

#plt.setp(axarr[0].get_xticklabels(), visible=False)
# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
#plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
#plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
plt.savefig('salt_potn.png')
plt.show()


fig = plt.figure()
plt.plot(x, y1, x, y2, x, y3, x, y5, linewidth=2)
plt.show()
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

axarr[1, 0].plot(x, y1 ** 2)
axarr[1, 0].set_title('Axis [1,0]')
axarr[1, 1].scatter(x, y1 ** 2)
axarr[1, 1].set_title('Axis [1,1]')
'''
