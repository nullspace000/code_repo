nombre = input('hola, como te llamas? ') 
print('hola ',nombre)
youtube = float(input('Cuantas horas pasaste hoy en youtube? '))
tiktok = float(input('Cuantas horas pasaste hoy en tiktok?'))
instagram = float(input('Cuantas horas pasaste hoy en instagram? '))
netflix = float(input('Cuantas horas pasaste hoy en netflix? '))
spotify = float(input('Cuantas horas pasaste hoy en spotify? '))

suma = youtube + tiktok + instagram + netflix + spotify
print('Hoy pasaste', suma,' horas en estas plataformas.')
porsentaje = (suma / 24) * 100
print('Eso equivale a ',porsentaje,'% de tu día.')


