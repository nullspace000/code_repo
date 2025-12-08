#verificar si un numero es positivo negativo o cero
seguir = 1
while seguir == 1:

    num1 = float(input("Por favor ingrese un número: "))
    if num1 > 0:
        print("El numero es positivo.")
    elif num1 < 0:
        print("El numero es negativo.")
    elif num1 == 0:
        print("El numero es cero.")
    else:
        print("que es mamada?")

    sino = input("desea ingresar otro número?: (s/n): ")
    if sino == 'n' or sino == 'N':
        seguir = 0
