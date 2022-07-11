#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
uniform("uni.dat", 1000000);

//Gaussian random numbers
gaussian("gau.dat", 1000000);
v("uni.dat",1000000);
triangular("tri.dat",1000000);
bernoulli("ber.dat",1000000);
maxlike("maxlike.dat", 0.5);

chi("chi.dat",1000000);
chi_root("chi_root.dat",1000000);

//Mean of uniform
printf("Mean of U:%lf\n",mean("uni.dat"));
printf("Variance of U:%lf\n",variance("uni.dat"));
printf("Mean of X:%lf\n",mean("gau.dat"));
printf("Variance of X:%lf\n",variance("gau.dat"));
printf("P_(e|0) = %lf\n",x_cap(1));
printf("P_(e|1) = %lf\n",x_cap(-1));
return 0;
}