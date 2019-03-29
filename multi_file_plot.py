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



mpl.rcParams['lines.linewidth'] = 3
mpl.rcParams['lines.markersize'] = 10
# comment the below line because it also change the circle edge width
#mpl.rcParams['lines.markeredgewidth'] = 3 # plus cross marker
mpl.rcParams['axes.labelsize'] = 28
mpl.rcParams['axes.titlesize'] = 28
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24
#legend
#mpl.rcParams['legend.fancybox'] = True
mpl.rcParams['legend.numpoints'] = 2 #default 2
mpl.rcParams['legend.fontsize'] = 20
#figure width or height
mpl.rcParams['figure.subplot.left'] = 0.175 #default 0.125
mpl.rcParams['figure.subplot.bottom'] = 0.15 #default 0.1
mpl.rcParams['figure.figsize'] = 10, 7.5 #default 8, 6

###########################################################
# constants

path = '/home/yaohua/Downloads/repos/Protein_Charge/'

fn1 = '1egm_qpH'
fn2 = '3ngk_qpH'
parser=argparse.ArgumentParser()
#fn = 'output.txt'
parser.add_argument("skiplines")
parser.add_argument("x")
parser.add_argument("y")
#parser.add_argument("name")
args = parser.parse_args()

#name = np.genfromtxt(path+fn, delimiter=' ', dtype=str)
data = np.genfromtxt(path+fn1, delimiter='\t', skip_header=int(args.skiplines))
data2 = np.genfromtxt(path+fn2, delimiter='\t', skip_header=int(args.skiplines))
#print data
#x_lbl = name[0, int(args.x)]
#y_lbl = name[0, int(args.y)]
x_lbl = 'pH'
y_lbl = 'charge'

start=0
end=len(data)
end=len(data)
x = data[start:end, int(args.x)]
y = data[start:end, int(args.y)]
y2 = data2[start:end, int(args.y)]

#for i in range(num_files):
#    y.append(data[start:end, 1])


fig = plt.figure()
plt.plot(x,y, label='1egm')
plt.plot(x,y2, label='3ngk')
plt.legend()
plt.xlabel(x_lbl)
plt.ylabel(y_lbl)
plt.grid(True)
#plt.xticks(rotation=45)
plt.savefig(path+'charges_ngk_egm.pdf')
plt.show()


