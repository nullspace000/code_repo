#include <stdio.h>

/* count charactes in input */
int main(){
	double nc;

	for (nc = 0; getchar() != EOF; ++nc)
		; /* null statement */
	printf("%.0f\n", nc);
		/* printf uses %f for both float and double; %.0f suppresses printing of decimal point and tha fraction part, which is zero in this case. */		
}
