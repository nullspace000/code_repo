#include <stdio.h>

/*mostrar la tabla de Pitágoras, la cual permite visualizar cuál será el resultado del producto de dos números, así que solicitarás dos factores (cifras) para obtener el resultado de su multiplicación.*/

/*arreglo_1 = ' ',1,2,3,4,5,6,7,8,9,10*/
	/*int i = 0 */
	/*int o = 0 */
	/*while (i<10) {*/
	/*for(i<10) [*/
	/*print (arreglo_1[1i] * arreglo_1[1o] */
	/*print (arreglo_1[2i] * arreglo_1[1] */
	/*print (arreglo_1[3i] * arreglo_1[1] */
	/*print (arreglo_1[4i] * arreglo_1[1] */
	/*print (arreglo_1[5i] * arreglo_1[1] */
	/*print (arreglo_1[6i] * arreglo_1[1] */
	/*print (arreglo_1[7i] * arreglo_1[1] */
	/*print (arreglo_1[8i] * arreglo_1[1] */
	/*print (arreglo_1[9i] * arreglo_1[1] */
	/*print (arreglo_1[10i] * arreglo_1[1] */
	/*]*/


	/*print (arreglo_1[1i] * arreglo_1[2] */
	/*print (arreglo_1[2] * arreglo_1[2] */
	/*print (arreglo_1[3] * arreglo_1[2] */
	/*print (arreglo_1[4] * arreglo_1[2] */
	/*print (arreglo_1[5] * arreglo_1[2] */
	/*print (arreglo_1[6] * arreglo_1[2] */
	/*print (arreglo_1[7] * arreglo_1[2] */
	/*print (arreglo_1[8] * arreglo_1[2] */
	/*print (arreglo_1[9] * arreglo_1[2] */
	/*print (arreglo_1[10] * arreglo_1[2] */
	/*}*/
int main(){
	int i;
	int o;
	int a;	
	int arreglo_1[10];
	int factor_1;
	int factor_2;
	int resultado;
	for(i=0;i<10;i++){
		arreglo_1[i] = i+1;
	}
	
	/*imprimir valores de arreglo 1*/
	printf("valores arreglo_1: ");
	for(i=0;i<10;i++){
		printf("%d",arreglo_1[i]);
	}
	printf("\n");
	/*imprimir valores de arreglo 1*/

	for(o=0;o<10;o++){
		for(i=0;i<10;i++){
			a = (arreglo_1[i] * arreglo_1[o]);
			printf("| %3d ",a);
		}
		printf("|\n");
	}
	/* Pedir factores, realizar multiplicación, mostrar resultado y preguntar si bucle*/
	int f = 1;
	char sino;
	while(f == 1){
		printf("Por favor ingrese el primer factor que desea multiplicar: ");
		scanf("%d", &factor_1);
		printf("Por favor ingrese el segundo factor que desea multiplicar: ");
		scanf("%d", &factor_2);
		resultado = (factor_1 * factor_2);
		printf("El resultado de %d por %d es: %d\n", factor_1, factor_2, resultado);

		printf("Desea realizar otra multiplicación? (s/n): ");
		scanf("%c", &sino);
		if(sino == 'n' || sino == 'N'){
			f = 0;	
		}	
	}
	printf("\n");
}
