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
mpl.rcParams['axes.labelsize'] = 26
mpl.rcParams['axes.titlesize'] = 26
mpl.rcParams['xtick.labelsize'] = 26
mpl.rcParams['ytick.labelsize'] = 26
#legend
#mpl.rcParams['legend.fancybox'] = True
mpl.rcParams['legend.numpoints'] = 2 #default 2
mpl.rcParams['legend.fontsize'] = 18
#figure width or height
mpl.rcParams['figure.subplot.left'] = 0.175 #default 0.125
mpl.rcParams['figure.subplot.bottom'] = 0.15 #default 0.1
mpl.rcParams['figure.figsize'] = 10, 7.5 #default 8, 6

###########################################################
# constants

path = './data/'
parser=argparse.ArgumentParser()
#fn = 'output.txt'
parser.add_argument("fn", type=str)
parser.add_argument("skiplines")
#parser.add_argument("name")
args = parser.parse_args()

#name = np.genfromtxt(path+fn, delimiter=' ', dtype=str)
data = np.genfromtxt(path+str(args.fn), delimiter='\t', skip_header=int(args.skiplines))

#print data
#x_lbl = name[0, int(args.x)]
#y_lbl = name[0, int(args.y)]
x_lbl = 'Concentration (M)'
y_lbl = 'y'

start=0
end=len(data)-1
x = data[start:end, 0]
y = data[start:end, 1]
y2= data[start:end, 2]
err = data[start:end, 3]
def tailMean(arr):
    tailL = 20
    meanVal = np.mean(arr[-tailL:-1])
    stdVal = np.std(arr[-tailL:-1])
    return meanVal, stdVal

#meanH, stdH = tailMean(y)

#for i in range(num_files):
#    y.append(data[start:end, 1])


fig = plt.figure()
plt.scatter(x,y,marker='s', label='Simulation')
plt.errorbar(x, y, yerr=err)
plt.plot(x,y2, label='PB')
plt.legend()
plt.xlabel(x_lbl)
plt.ylabel(y_lbl)
#plt.title('Na170_Mg4')
#plt.xticks(rotation=45)
plt.savefig(path+str(args.fn)+'.png')
plt.show()
