#include <stdio.h>

/* count blanks, tabs and newlines in input */

int main(){

	int input;
	int newlines = 0;
	int blanks = 0;
        int tabs = 0;	

	while ((input = getchar()) != EOF){
		if(input == '\n')
			++newlines;
		if(input == ' ')
			++blanks;
		if(input == '\t')
			++tabs;
	}
	printf("newlines: %d\n", newlines);
	printf("blanks: %d\n", blanks);
	printf("tabs: %d\n", tabs);
}
