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
mpl.rcParams['axes.labelsize'] = 25
mpl.rcParams['axes.titlesize'] = 25
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

path = '/home/yaohua/Downloads/newQuest_b1021/cg_protein/DNA_rod/HistoResults/'
parser=argparse.ArgumentParser()
#fn = 'output.txt'
#parser.add_argument("fn", type=str)
parser.add_argument("skiplines")
#filename = str(args.fn)
filename= 'totalhist_single_neg_mole2.0_IBI_1_dist_D.dat'
#parser.add_argument("x")
#parser.add_argument("y")
#parser.add_argument("start")
#parser.add_argument("name")
args = parser.parse_args()

#name = np.genfromtxt(path+fn, delimiter=' ', dtype=str)
data = np.genfromtxt(path+filename, delimiter=' ', skip_header=int(args.skiplines))

#print data
#x_lbl = name[0, int(args.x)]
#y_lbl = name[0, int(args.y)]
x_lbl = 'X (nm)'
y_lbl = ''

start=5
end=len(data)

end=len(data)-50
x = data[start:end, 0]
y = data[start:end, 1]

def tailMean(arr):
    tailL = 20
    meanVal = np.mean(arr[-tailL:-1])
    stdVal = np.std(arr[-tailL:-1])
    return meanVal, stdVal

meanH, stdH = tailMean(y)

#for i in range(num_files):
#    y.append(data[start:end, 1])


fig = plt.figure()
plt.plot(x,y)
#plt.ylim(-5, 10)
#plt.legend()
plt.xlabel(x_lbl)
plt.ylabel(y_lbl)
#plt.xticks(rotation=45)
plt.savefig(filename+'.png')
plt.show()
