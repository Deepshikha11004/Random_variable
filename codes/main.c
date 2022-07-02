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

//Mean of uniform
printf("Mean of U:%lf\n",mean("uni.dat"));
printf("Variance of U:%lf\n",variance("uni.dat"));
printf("Mean of X:%lf\n",mean("gau.dat"));
printf("Variance of X:%lf\n",variance("gau.dat"));
return 0;
}
