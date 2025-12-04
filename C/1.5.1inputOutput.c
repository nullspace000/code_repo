#include <stdio.h>

/* copy input to output; 1sst version */

int main(){
	int c;

	c = getchar();
	while (c != EOF){
		putchar(c);
		c = getchar();	
	}
}

/* We can ue char type for c variable since c must be big enough to hold EOF in addition to any possible char. Therefore we use int */
