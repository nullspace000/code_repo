#programa de calculadora basica de operaciones aritmeticas: suma, resta, multiplicación, división

num1 = 0
num2 = 0
resultado = 0
restante = 0
seguir = 1
while seguir == 1:
    print("Que operacion desea realizar? (suma, resta, multiplicacion, division):")
    operacion = str(input())
    if operacion == "suma" or operacion == "Suma" or operacion == "Suma " or operacion == "suma ":
        num1 = int(input("Ingrese el primer numero a sumar: "))
        num2 = int(input("Ingrese el segundo numero a sumar: "))
        resultado = num1 + num2
        print("El resultado es:",resultado)

    if operacion == "resta" or operacion == "Resta" or operacion == "Resta " or operacion == "resta ":
        num1 = int(input("Ingrese minuendo de la resta (el numero del cual se va a restar otro numero): "))
        num2 = int(input("Ingrese el sustraendo (el numero que se resta del minueldo: "))
        resultado = num1 - num2
        print("El resultado es:",resultado) 

    if operacion == "multiplicacion" or operacion == "Multiplicacion" or operacion == "multiplicacion " or operacion == "Multiplicacion " or operacion == "multiplicación" or operacion == "Multiplicación" or operacion == "multiplicación " or operacion == "Multiplicación ":
        num1 = int(input("Ingrese el primer numero a multiplicar: "))
        num2 = int(input("Ingrese el segundo numero a multiplicar: "))
        resultado = num1 * num2
        print("El resultado es:",resultado)

    if operacion == "division" or operacion == "Division" or operacion == "division " or operacion == "Division " or operacion == "división" or operacion == "División" or operacion == "división " or operacion == "División ":
        num1 = int(input("Ingrese el dividendo (el numero que se va a dividir): "))
        num2 = int(input("Ingrese el divisor (el numero por el que se divide): "))
        resultado = num1 / num2
        restante = num1 % num2
        print("El resultado es:",resultado)
        print("El restante es:",restante)

    sino = input("Desea realizar otra operacion?: (s/n): ")
    if sino == 'n' or sino == 'N':
        seguir = 0


