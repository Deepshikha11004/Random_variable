#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import mpmath as mp


maxrange=50
maxlim=4.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
#err = [] #declaring probability list
#pdf = [] #declaring pdf list



y = np.loadtxt('maxlike.dat',dtype='double')

x = np.random.random(simlen)

plt.scatter(x,y)

plt.savefig('/home/deepshikha/gvv_randomvariable/figs/Y_scatter.png')

#plt.show()