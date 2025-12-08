#include <stdio.h>

int main()
{
	int c;
	int i;
	char nombre_usuario[20];
	/*get user name input*/
	printf("Ingrese su nombre: ");
	/*i = 0;
	while((c = getchar()) != EOF){
		nombre_usuario[i] = c;
		i++;
	}*/
	scanf("%s", nombre_usuario);

	/*count first name characters
	char a;
	int l = 0;
	while(a != ' ' || a != EOF){
		a = nombre_usuario[l];
		++l;
	}
	print first name*/
	printf("Bienvenido ");
	for (i = 0; i < 20; ++i){
		printf("%c",nombre_usuario[i]);	
	}
	printf("\n");


	/*pedir al menos 5 plataformas con su respectivo valor de tiempo*/
	printf("Debera ingresar al menos 5 plataformas con su respectivo tiempo de uso.\n");
	/*2d array to store the names becuause strings are arrays in c*/
	int platform_names_array[50][20]; /*50 names up to 20 chars long*/
	int platform_time_array[50];
	/*set all indexes of array to 0*/
	for(i=0;i<50;i++){
		platform_time_array[i] = 0;
	}	
	int index = 1;
	int loopcheck =1;
	int sino;	
	while(loopcheck == 1){
		printf("Por favor ingrese el nombre de la plataforma %d: ", index);
		/*i = 0;
		while((b = getchar()) != EOF){
			platform_names_array[index][i] = b;
			i++;
		}*/
		scanf("%s", platform_names_array[index]);

		/*input time*/
		printf("Por favor ingrese el numero de horas que dedico a la plataforma %d: ", index);
		scanf("%d", &platform_time_array[index]);
		++index;
		/*ask user if want to submit more platforms*/
		if(index > 5){
			printf("Desea agregar otra plataforma? (s/n): ");
			scanf(" %c", &sino);
			if(sino != 's' || sino != 'S'){
				/*end loop*/
				loopcheck = 0;
			}if(sino == 's' || sino == 'S'){
				printf("%c\n",sino);
				loopcheck = 1;
			}	
		}
	}
	/*sumar horas*/
	float sum = 0;
	for(i=0;i<50;i++){
		sum = sum + platform_time_array[i];
	}
	/*calcular % del día */
	float porsentaje_dia = (sum / 24.0);
	float porsentaje_dia_2 = porsentaje_dia * 100.0;
	/*imprimir resultados*/
	printf("En total pasaste %.2f",sum);
	printf(" horas en plataformas digitales.\n");
	printf("Esto equivale al %.2f%% de tu día.\n", porsentaje_dia_2);
	/*imprimir arreglos
	printf("|    nombre     | horas |\n");
	printf("|---------------|-------|\n");
	for(i=1;i<index;i++){	
		printf("%15s | %.2f\n", platform_names_array[i], platform_time_array[i]);
	}
	printf("%.2f",platform_time_array[1]);*/
}


