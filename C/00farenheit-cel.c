#include <stdio.h>

/* print Fahrenheit-Celsius table from fahr = 0,20, ..., 300; floating-point version*/

int main(){
	float fahr, celsius;
	int lower,upper,step;

	lower = 0; /* lower limit of temperature table */
	upper = 300; /* upper limit */
	step = 20; /* step size */

	fahr = lower;
	printf("\nfahrenheit | celsius \n");
	while (fahr <= upper){
		celsius = (5.0/9.0) * (fahr - 32.0); /* we divide 5.0 by 9.0 because 
							integer division would truncate to 0. */
		printf("%10.0f | %.1f \n", fahr, celsius); /* %3.0f says that a floating-point number (fahr) is to be printed at least three characters wide with no decimal point. %6.1f describes celsius that is to be printed at least six characters wide with one digit after the decimal point. */
		fahr = fahr + step;
	}
}

/* %d print as decimal integer
 * %6d print as decimal integer, at least 6 characters wide
 * %f print as floating point 
 * %6f print as floating point at least 6 characters wide
 * %.2f print as floating point, 2 characters after decimal point 
 * %6.2f print as floating point at least 6 wide and 2 after decimal point */
