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
#c1 = np.zeros(20)
#c2 = np.linspace(0,1,10)
#c3 = np.ones(20)
#c = np.concatenate([c1,c2,c3])
simlen = int(1e6) #number of samples
err = [] #declaring probability list
h = 2*maxlim/(maxrange-1)
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
#randvar = np.loadtxt('log_V.dat',dtype='double')
randvar = np.loadtxt('vdis.dat',dtype='double')
for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list




def v_cdf(x):
	if(x>=0):
		return 1 - np.exp(-x/2.0)
	else:
		return 0.0



vec_v_cdf = scipy.vectorize(v_cdf)


#plt.plot(x.T,err)
plt.plot(x[0:(maxrange)].T,err,'o')

plt.plot(x,vec_v_cdf(x))  #plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_V(x)$')
plt.legend(["Numerical","Theory"])


plt.savefig('/home/deepshikha/gvv_randomvariable/figs/v_cdf.png')
plt.show()

