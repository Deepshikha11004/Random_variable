#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import mpmath as mp

#if using termux
import subprocess
import shlex
#end if


maxrange=50
maxlim = 4
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis

simlen = int(1e6) #number of samples
err = [] #declaring probability list
h = 2*maxlim/(maxrange-1)

randvar = np.loadtxt('tri.dat',dtype='double')
for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def tri_cdf(x):
	if(x<=0):
		return 0.0
	elif(x>0 and x<=1):
		return x**2/2
	elif(x>1 and x<2):
		return 1 - ((2-x)**2/2)
	else:
		return 1.0


vec_tri_cdf = scipy.vectorize(tri_cdf)

plt.plot(x[0:(maxrange)].T,err,'o')

plt.plot(x,vec_tri_cdf(x))  #plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])


plt.savefig('/home/deepshikha/gvv_randomvariable/figs/t_cdf2.png')
plt.show()

