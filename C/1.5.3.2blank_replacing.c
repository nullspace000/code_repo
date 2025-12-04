#include <stdio.h>

/* wrirte a program to copy its input to its output, replacing each string of one or more blanks by a single blank */

int main(){

	int input;
	int blanks = 0; /* when this variable is > 2, we dont print the character
			   currently in input */
			       
	int output;

	while ((input = getchar()) != EOF){
		if(input == ' ')
			++blanks;
		if(input != ' ')
			blanks = 0;
		if(blanks < 2){
			printf("%c",input);	
		}
	}
}
