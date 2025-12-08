import time
#Desarrollar un programa en Python que permita gestionar las calificaciones de un gurpo de estudiantes utilizando archivos de texto para elmacenar la información
print('\033[32m############################')
print('# Gestor de Calificaciones #')
print('############################\033[0m')
#requerimientos del programa
#1. archivo inicial
#   Debe existir un arvhivo llamado estudiantes.txt que contenga los nombres de los alumons(uno por línea)
#   Ejemplo:
#   Ana
#   Juan
#   Pedro
#   María

#\033[31m → red
#\033[32m → green
#\033[33m → yellow
#\033[34m → blue
#\033[35m → magenta
#\033[36m → cyan
#\033[0m → reset (always use at the end)

#3. funciones de cada opción
#   1. pedir nombre del estudiante y calificación (0-100). validar que el estudiante existe en estudiantes.txt guardar en un archivo calificaciones.txt en formato:
#        Ana,85
#        Juan,70
#        Pedro,95
def registro_cal():
    nombre_est = input('\nIngrese el nombre del estudiante: ')
    calificacion = int(input('\nIngrese la calificación del estudiante de 0 - 100: '))
    archivo = open("estudiantes.txt")
    contenido = archivo.read()
    existe_estudiante = 0
    x = contenido.find(nombre_est)
    if x != -1:
        existe_estudiante = 1
        f = open("calificaciones.txt", "a")
        f.write(f"\n{nombre_est} : {calificacion}")
        f.close()
        print(f"\n\033[32mSe guardó la calificación del estudiante: {nombre_est} en calificaciones.txt\033[0m")
    if x == -1:
        print(f"\n\033[31mEl estudiante: {nombre_est} no existe en la lista de estudiantes. \nNo se guardará su calificación en calificaciones.txt.\033[0m")

#   2. leer calificaciones.txt y mostrar en pantalla todos los registros.
def leer_cal():
    archivo = open("calificaciones.txt")
    print(f'\033[32m{archivo.read()}\033[0m')

#   3. Pedir el nombre de un estudiante y mostrar solo sus calificaciones(puede tener varias)
def cal_est():
    nombre_est = input('\nIngrese el nombre del estudiante: ')
    archivo = open("calificaciones.txt")
    contenido = archivo.read()
    for line in contenido.splitlines():
        if nombre_est in line:
            print(f"\033[32m {line} \033[0m")
    
#   4. Calcular y mostrar:
#       Promedio del grupo
#       Calificación más altay más baja
#       Número de aprobados y reprobados (>= 70 es aprobado)
def calc_most():
    archivo = open("calificaciones.txt")
    contenido = archivo.read()
    lines = 0
    for line in contenido.splitlines():
        lines = lines + 1
    suma = 0
    cals = []
    for line in contenido.splitlines():
        n, cal = line.split(" : ")  # split into two parts
        cal = int(cal)
        cals.append(cal)
    suma = sum(cals) 
    #print(f'suma: {sum}')
    #print(f'lines: {lines}')
    apro = []
    repro = []
    for cal in cals:
        if cal >= 70:
            apro.append(cal)
        if cal < 70:
            repro.append(cal)
    num_apro = 0
    for x in apro:
        num_apro = num_apro + 1
    num_repro = 0
    for x in repro:
        num_repro = num_repro + 1
    reporte = (f'Promedio del grupo: {suma/lines}\nCalificación más alta: {max(cals)}\nNúmero de aprobados: {num_apro}\nNúmero de reprobados: {num_repro}')
    return reporte 
   
#5. Exportar reporte?
def exp_rep():
    with open("reporte.txt", "w") as file:
        file.write(calc_most())
        file.close()


#2. menú principal
#   El programa dee mostrar un menú usando match=case con las siguiantes opciones:
#   1. registrar calificacion de un estudiante
#   2. mostrar todas las calificaciones
#   3. buscar calificaciones por estudiante
#   4. mostrar estadísticas del grupo
#   5. exportar reporte a archivo
#   6. salir
a = 1
while a == 1:
    print('\n1. Registrar calificacion de un estudiante')
    print('2. Mostrar todas las calificaciones')
    print('3. Buscar calificaiones por estudiante')
    print('4. Mostrar estadísitcas del grupo')
    print('5. Exportar reporte a archivo')
    print('6. Salir')
    #try:
    eleccion = int(input('\n¿Qué opcion elige?: '))
    #if eleccion > 6 or eleccion < 1:
    #    raise Exception('\n Error. Número fuera de rango')
    #except:
    #    print('\n Error. Intentelo de nuevo.')
    #else:
    if eleccion == 1:
        print('\n1. Registro de calificación...')
        registro_cal()
        time.sleep(1)

    if eleccion == 2:
        print('\n2. Mostrando calificaciones...')
        leer_cal()
        time.sleep(1)

    if eleccion == 3:
        print('\n3. Buscar calificaiones por estudiante...')
        cal_est()
        time.sleep(1)

    if eleccion == 4:
        print('\n4. Mostrando estadísticas del gurpo...')
        print(f'\033[32m{calc_most()}\033[0m')
        time.sleep(1)

    if eleccion == 5:
        print('\033[32m\n5. Exportando reporte...\033[0m')
        exp_rep()
        time.sleep(1)

    if eleccion == 6:
        print('\033[32m\nSaliendo...\033[0m')
        a = 0



