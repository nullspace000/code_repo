import pyttsx3
import time
#programa para pasar lista con text to speach que diga el nombre de los alumnos
#Este programa le ayudará a pasarlista

#Solicita al usuario su nombre o nickname.
nickname = input('Ingrese su nickname: ')
#Genera un mensaje de bienvenida, donde agregues la información obtenida en el paso uno mediante operadores string.
print(f'Bienvenido {nickname}!')

#Por medio una función, genera un mensaje de espera de máximo cinco segundos, mientras que en la pantalla se debe leer un aviso de carga de programa.
def carga():
    time.sleep(1)
    print('Cargando:|===>                                   |')
    time.sleep(1)
    print('Cargando:|=============>                         |')
    time.sleep(1)
    print('Cargando:|=========================>             |')
    time.sleep(1)
    print('Cargando:|======================================>|')
carga()

#lista de alumnos
alumnos = [
 ['Juan Gomez Arriaga', 'no definido'],
 ['Valesa Peraltes Ruega', 'no definido'],
 ['Joaquín Hernandez Gozo', 'no definido'],
 ['Carlos Ramírez González', 'no definido'],
 ['María López Sánchez', 'no definido'],
 ['Juan Pérez Rodríguez', 'no definido'],
 ['Ana Torres Martínez', 'no definido'],
 ['Luis Fernández Castillo', 'no definido'],
 ['Laura Morales Díaz', 'no definido'],
 ['Jorge Herrera Díaz', 'no definido'],
 ['Carmen García Romero', 'no definido'],
 ['Pedro Mendoza Ortega', 'no definido'],
 ['Isabel Ruiz Herrera', 'no definido'],
]
#definiendo numero de alumnos para el límite del bucle
num_alumnos = int(len(alumnos))
print(f'Alumnos: {num_alumnos}')
#pyttsx3.init() creates and returns a TTS engine object (an instance of the speech engine).
tts = pyttsx3.init()
tts.setProperty('rate', 130)
#definiendo bucle para contar asistencias
for x in range (0, num_alumnos):
 #imprimiendo nombre del alumno actual y preguntando si está presente
    print(f'Alumno {alumnos[x][0]} presente?')
    u = 1
    while u == 1:
        #imprimiendo opciones que tiene el usuario
        print('(1) si \n(2) no')

        #tts nombra al alumno actual
        tts.say(alumnos[x][0])
        #It processes and plays the speech commands that you’ve queued up using .say() or .speak().
        tts.runAndWait()
        input_usuario = input()
        #caso si
        if input_usuario == '1' or input_usuario == 'si' or input_usuario == 's':
        #asignando asistencia
            alumnos[x][1] = 's'
            #se rompe el bucle
            u = 0
        #caso no
        elif input_usuario == '2' or input_usuario == 'no' or input_usuario == 'n':
            #asignando asistencia
            alumnos[x][1] = 'n'
            u = 0
        #caso esperar
        #elif input_usuario == '3' or input_usuario == 'esperar' or input_usuario == 'e':
        #asignando asistencia
        #alumnos[x][1] = 'e'
        #u = 0
        #caso exepción
        else:
            print('Por favor intentelo de nuevo.')
            print(alumnos)
            #ipmrimiendo tabla de alumnos con el estado de su asistencia
            print('\nalumno : asistencia')
            for y in range(0, num_alumnos):
                print(f'{alumnos[y][0]} : {alumnos[y][1]}')
#Emplea el ciclo while para generar un menú donde se muestren, por lo menos, tres opciones para manipular documentos (leer, escribir y crear archivos), así como una para cambiar de usuario. Estas alternativas deben presentarse en forma de matriz.
#Utiliza un ciclo for para medir el tiempo que tarda el usuario en seleccionar una opción; si después de 10 minutos no ha elegido ninguna, se le mostrará un mensaje para preguntarle si desea continuar. El usuario debe escribir “si” para seguir en el menú o “no” para cambiar a la pantalla inicial.
#Se debe preguntar al usuario la fecha en el formato numérico de día, mes y año; por ejemplo, 12/06/2023. Este valor se almacenará en una tupla basada en esta sintaxis:
#Fecha = día, mes, año

#La fecha introducida por el usuario debe utilizarse cuando se crea o se modifica un archivo.

#Para la lectura, deberás tener creados cuatro o más archivos de manera previa, los cuales se mostrarán en forma de lista o diccionario para seleccionar uno; posteriormente, se solicitará al usuario el nombre de aquel que desea abrir.
#Implementa los manejadores de excepciones necesarios en el código, por ejemplo, si se intenta leer un archivo inexistente o se ingresa un nombre mal escrito.
#Agrega comentarios relevantes para el mantenimiento del programa.
#Haz el debugging del código elaborado.
#Finalmente, elabora un reporte donde muestres tus resultados.
