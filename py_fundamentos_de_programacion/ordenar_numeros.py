#que le pida al usuario 3 numeros enteros y el programa losmuestre en orden ascendente y descendente utilizando solo estrucuras de desición

num1 = int(input("ingrese el numero 1: "))
num2 = int(input("ingrese el numero 2: "))
num3 = int(input("ingrese el numero 3: "))
#orden descendente 
#1,2,3
if num1 > num2 and num2 > num3:
    print(f"{num1},{num2},{num3}")
#1,3,2
elif num1 > num3 and num3 > num2:
    print(f"{num1},{num3},{num2}")
#3,2,1
elif num3 > num2 and num2 > num1:
    print(f"{num3},{num2},{num1}")
#2,1,3
elif num2 > num1 and num1 > num3:
    print(f"{num2},{num1},{num3}")
#2,3,1
elif num2 > num3 and num3 > num1:
    print(f"{num2},{num3},{num1}")
#3,1,2
elif num3 > num1 and num1 > num2:
    print(f"{num3},{num1},{num2}")

#orden acendente 
#1,2,3
if num1 < num2 and num2 < num3:
    print(f"{num1},{num2},{num3}")
#1,3,2
elif num1 < num3 and num3 < num2:
    print(f"{num1},{num3},{num2}")
#3,2,1
elif num3 < num2 and num2 < num1:
    print(f"{num3},{num2},{num1}")
#2,1,3
elif num2 < num1 and num1 < num3:
    print(f"{num2},{num1},{num3}")
#2,3,1
elif num2 < num3 and num3 < num1:
    print(f"{num2},{num3},{num1}")
#3,1,2
elif num3 < num1 and num1 < num2:
    print(f"{num3},{num1},{num2}")

