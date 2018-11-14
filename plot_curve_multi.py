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
mpl.rcParams['axes.labelsize'] = 24
mpl.rcParams['axes.titlesize'] = 24
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

###########################################################
# constants

path = '/home/yaohua/Downloads/questb1021/protein/umbrella3/testMg/WHAM/'
parser=argparse.ArgumentParser()
#fn = 'output.txt'
parser.add_argument("fn", type=str)
parser.add_argument("skiplines")
parser.add_argument("col_start")
parser.add_argument("num_colunm")
parser.add_argument("start")
#parser.add_argument("name")
args = parser.parse_args()

#name = np.genfromtxt(path+fn, delimiter=' ', dtype=str)
data = np.genfromtxt(path+str(args.fn), delimiter='\t', skip_header=int(args.skiplines))

#print data
#x_lbl = name[0, int(args.x)]
#y_lbl = name[0, int(args.y)]
x_lbl = 'X'
y_lbl = 'PMF (kCal/mol)'

start=int(args.start)
end=len(data)
print args.start
end=len(data)
x = data[start:end, 0]
y = []
numC = int(args.num_colunm)
for i in range(numC):
    y.append(data[start:end, i])

#for i in range(num_files):
#    y.append(data[start:end, 1])


fig = plt.figure()
for i in range(int(args.col_start), numC):
    plt.plot(x,y[i], linewidth=2, label='window{}'.format(i))
plt.legend()
plt.xlabel(x_lbl)
plt.ylabel(y_lbl)
#plt.xticks(rotation=45)
#plt.savefig('plot.pdf')
plt.show()


