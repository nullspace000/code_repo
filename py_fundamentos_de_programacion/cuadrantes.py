#pedir un punto al usuario
#definir si está sobre el eje y, el eje x o el origen
#definir en que cuardante está

x = int(input("Ingrese la coordenada x del punto: "))
y = int(input("Ingrese la coordenada y del punto: "))
if x == 0 and y == 0:
    print("El punto esta en el origen")
if y == 0:
    print("El punto esta sobre el eje x")
if x == 0:
    print("El punto esta sobre el eje y")
if x >= 0 and y >= 0:
    print("El punto esta en el cuadrante 1")
elif x < 0 and y >= 0:
    print("El punto esta en el cuadrante 2")
elif x < 0 and y < 0:
    print("El punto esta en el cuadrante 3")
elif x >= 0 and y < 0:
    print("El punto esta en el cuadrante 4")
else:
    print("error")

