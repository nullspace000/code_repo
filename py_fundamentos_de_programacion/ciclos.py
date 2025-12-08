print("**Opciones***")
print("1. Imprimir los numeros del 1 al 10")
print("2. Sumar los primeros numeros del 1 al n")
print("3. Tabla de multiplicar del numero n, hasta el 10")
print("4. Mostrar numeros pares e impares hasta n")

opt = int(input("Que opcion desea?: "))
if opt == 1:
    for i in range(0,10):
        print(i+1)

elif opt == 2:
    n = int(input("Ingrese el numero hasta el cual quiere sumar: "))
    suma = 0
    for i in range(1,n+1):
        suma = suma + i
        print(suma)

elif opt == 3:
    n = int(input("Ingrese el numero del cual quiere la tabla de multiplicar: "))
    for i in range(1,11):
        print(i * n)

elif opt ==4:
    n = int(input("Ingrese el numero hasta el cual quiere la lista de numeros: "))
    print("Numeros pares:")
    for i in range(1,n+1):
        if i % 2 == 0:
            print(i)
    print("Numeros impares:")
    for i in range(1,n+1):
        if i % 2 != 0:
            print(i)
