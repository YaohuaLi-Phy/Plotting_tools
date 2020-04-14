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
mpl.rcParams['xtick.labelsize'] = 22
mpl.rcParams['ytick.labelsize'] = 22
#legend
#mpl.rcParams['legend.fancybox'] = True
mpl.rcParams['legend.numpoints'] = 2 #default 2
mpl.rcParams['legend.fontsize'] = 18
#figure width or height
mpl.rcParams['figure.subplot.left'] = 0.175 #default 0.125
mpl.rcParams['figure.subplot.bottom'] = 0.15 #default 0.1
mpl.rcParams['figure.figsize'] = 6,8 #default 8, 6

###########################################################
# constants



#print data
#x_lbl = name[0, int(args.x)]
#y_lbl = name[0, int(args.y)]
x_lbl = 'epsilon'
y_lbl = 'Asphericity'

data1 = np.array([0.1913, 0.05939, 0.045099, 0.05383, 0.247957, 0.0423449, 0.0884576, 0.0413839, 0.0438639,0.0991008,0.0216124, 0.0769663, 0.0951914]) #3.8

data2 = np.array([0.0314023, 0.1061, 0.07569, 0.0851, 0.033682, 0.126387, 0.166426, 0.127056, 0.0951702,0.0677624, 0.121354, 0.0456101, 0.0837621, 0.0456101,0.0253593, 0.0460622])

data3 = np.array([0.228246, 0.0831073, 0.055529, 0.0870971, 0.101363, 0.097251, 0.0582148, 0.0340473, 0.103467, 0.123125, 0.0190638, 0.0661839])  # 4.2

size1 = np.array([13.2034, 11.1104, 10.9563, 12.3185, 13.9363, 11.7906, 14.2646, 13.4437,12.5205, 12.3735, 9.97863, 10.5372,13.1802, 13.6842])

size2 = np.array([11.4943, 21.8738, 16.7575, 8.76794, 9.19018, 15.2869, 14.1492, 13.6842,16.7575,21.8738, 11.4943])

size3 = np.array([18.1457, 16.5158, 10.6864, 13.1463, 8.34392, 24.6485, 10.1691, 12.5381, 9.74349,9.84126, 13.0869, 8.06146])

x = np.array([3.8, 4, 4.2])
y = np.array([np.mean(data1), np.mean(data2), np.mean(data3)])
err = np.array([np.std(data1), np.std(data2), np.std(data3)])


#for i in range(num_files):
#    y.append(data[start:end, 1])


plt.subplot(2, 1, 1)
plt.errorbar(x, y, yerr=err, marker='s', dash_joinstyle='round')
plt.legend()

plt.ylabel(y_lbl)


#plt.title('Na170_Mg4')
#plt.xticks(rotation=45)

plt.subplot(212)
y = np.array([np.mean(size1), np.mean(size2), np.mean(size3)])
err = np.array([np.std(size1), np.std(size2), np.std(size3)])
plt.errorbar(x, y, yerr=err, marker='s', dash_joinstyle='round')
plt.legend()
plt.xlabel(x_lbl)
plt.ylabel('size (# of mers)')
plt.savefig('asphericity.png')
plt.show()
