#verificar si un numero es multiplo de 3 y de 5

num = int(input("Por favor ingrese el numero a verificar: "))
multiplo1 = int(input("Por favor ingrese el primer multiplo: "))
multiplo2 = int(input("Por favor ingrese el segundo multiplo: "))
if num % multiplo1 == 0 and num % multiplo2 == 0:
    print(f"El numero es multiplo de {multiplo1} y {multiplo2}.")
else:
    print("No es multiplo")
