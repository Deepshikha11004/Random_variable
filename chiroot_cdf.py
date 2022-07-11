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

randvar = np.loadtxt('chi_root.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list




def root_V_cdf(x):
	if(x>=0):
		return 1 - np.exp(-x**2/2)
	else:
		return 0.0


	


vec_root_V_cdf = scipy.vectorize(root_V_cdf)

#plotting the CDF
#plt.plot(x.T,err)
plt.plot(x[0:(maxrange)].T,err,'o')

plt.plot(x,vec_root_V_cdf(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_{root(V)}(x)$')
plt.legend(["Numerical","Theory"])



plt.savefig('/home/deepshikha/gvv_randomvariable/figs/rootV_cdf.png')




plt.show()
