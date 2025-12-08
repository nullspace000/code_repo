#programa que realice el caćulo del precio de entrada para los visitantes de un museo

#adulto mayor 12%
#profesor 10%
#estudiante 10%

#menores de edad 30$
#mayores de edad 45$
#menores que 3 0$
#solo aplicar un tipo de descuento por boleto


#pedir y definir numero de visitantes
#predir edad de visitante 1
#si es menor que 3, precio = 0
#si es mayor que 60, descuento 12%
#si es mayor que 17,
    #preguntar si es profesor 10%
    #preguntar si es estudiante 10%

#calcular total a pagar
num_visitantes = int(input('Por favor ingrese el numero de visitantes: ')) - 1
edades_visitantes = []
precios_visitantes = []
i = 0
sino = 'n'
while i <= num_visitantes:
    print('Por favor ingrese la edad del visitante ',i+1,':')
    edades_visitantes.append(int(input()))

#caso menor que 3
    if(edades_visitantes[i] < 3):
       precios_visitantes.insert(i,0)

#caso menor de edad
    elif(edades_visitantes[i] < 18 and edades_visitantes[i] > 2):
       print('El visitante ',i+1,' es estudiante? (s/n)')
       sino = input()
       if sino == 's' or sino == 'S':
           precios_visitantes.insert(i,30-30*0.1)
       else:
           precios_visitantes.insert(i,30)

#caso mayor de edad
    elif(edades_visitantes[i] > 17 and edades_visitantes[i] < 60):
       print('El visitante ',i+1,' es estudiante? (s/n)')
       sino = input()
       if sino == 's' or sino == 'S':
           precios_visitantes.insert(i,45-(45*0.1))
       elif sino != 's' or sino == 'S':
           print('El visitante ',i+1,' es profesor? (s/n)')
           sino = input()
           if sino == 's' or sino == 'S':
               precios_visitantes.insert(i,45-(45*0.1))
           else:
               precios_visitantes.insert(i,45)

#caso adulto mayor 
    elif(edades_visitantes[i] > 59):
        precios_visitantes.insert(i,45 - 45 * 0.12)
    else:
        precios_visitantes.insert(i,45)
    i = i + 1

#imprimir resultados
suma_precios = sum(precios_visitantes)

print('visitante : edad : precio')
i = 0
while i <= num_visitantes:
    print(f"{i+1} : {edades_visitantes[i]} : {precios_visitantes[i]}") 
    i = i + 1

print('total: ',suma_precios)
