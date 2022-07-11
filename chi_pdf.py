#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

# #if using termux
# import subprocess
# import shlex
# #end if


maxrange=50
maxlim=4.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)

randvar = np.loadtxt('chi.dat',dtype='double')


for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def chi_pdf(x):
    if (0 <= x): 
        return 0.5*np.exp(-x/2)
    else: 
        return 0


	
vec_chi_pdf = scipy.vectorize(chi_pdf)


plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.plot(x,vec_chi_pdf(x))
#plt.plot(x,vec_gauss_pdf(x))#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_V(x_i)$')
plt.legend(["Numerical","Theory"])
#plt.savefig('../figs/X_PDF.png')
plt.savefig('/home/deepshikha/gvv_randomvariable/figs/chi_pdf.png')
