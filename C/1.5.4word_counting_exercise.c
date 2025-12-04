#include <stdio.h>

int main(){
        int c;
	char b;
        
        while ((c = getchar()) != EOF) {
               if (c == ' ' || c == '\n' || c == '\t')
			printf("\n");
               else {
			b = c;
                        printf("%c", b); 
		}
        }
}
