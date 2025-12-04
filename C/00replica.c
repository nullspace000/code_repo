# include <stdio.h>

/* program that prints a table of the conversion of fahrenheit to celcius with the range 0 - 300 */

int main(){
	int start = 0;
	int end = 300;
        int increment = 20;
	float cel;
      	float fahr;

	fahr = start;
	while(fahr < end){
		cel = (fahr - 32.0) * (5.0/9.0);
		printf("%d %d",fahr, cel);
		fahr = fahr + increment;	
	}

}
