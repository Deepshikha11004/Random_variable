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

randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list


def uni_cdf(x):
	if(x>=0 and x<=1):
		return x
	elif x<0:
		return 0.0
	else:
		return 1.0

def Q(x):
	return (1 - mp.erf(x/np.sqrt(2)))/2

def gauss_cdf(x):
	return 1 - Q(x)





vec_gauss_cdf = scipy.vectorize(gauss_cdf)


plt.plot(x[0:(maxrange)].T,err,'o')

plt.plot(x,vec_gauss_cdf(x))  #plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])



plt.savefig('/home/deepshikha/gvv_randomvariable/figs/x_cdf.png')
plt.show()

#if using termux
#plt.savefig('../figs/uni_cdf.pdf')
#plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
#plt.show() #opening the plot windowpi