try: 
    with open("archivo.txt","r")
    encoding=("UTF-8") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe.")

try:
    with open("archivo.txt","w")
    encoding=("UTF-8") as archivo:
except PermissionError as PermissionError as e:
    print("Error: El archivo no se puede escribir.")
