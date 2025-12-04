#include <stdio.h>

/* count digits, white space, others */ 

int main()
{
	int c, i, nwhite, nother;
	int ndigit[10];

	nwhite = nother = 0;
	for (i = 0; i < 10; ++i)
		ndigit[i] = 0;   /* you're converting the character digit to its 
					numeric value. For example: If c = '5', then
					'5' - '0' = 53 - 48 = 5. So ndigit[5]++ is 
					executed, which means: increment the counter					    for digit 5. */

	while ((c = getchar()) != EOF)
		if (c >= '0' && c <= '9')
			++ndigit[c-'0'];
		else if (c == ' ' || c == '\n' || c == '\t')
			++nwhite;
		else
			++nother;

	printf("digits ...\n");
	for (i = 0; i < 10; ++i)
		printf("%d: %d\n",i, ndigit[i]);
	printf("white space = %d\nother = %d\n", nwhite, nother);
}
