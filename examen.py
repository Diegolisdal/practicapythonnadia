"""     ENUNCIADO
un profesor necesita un programa para calcular la calificacion de sus estudiantes

IGRESO DE DATOS: 
a) nombre
b) nota1
c) nota2
d) nota3
e) porcentaje asistencia

CONDICION DE APROBACION
a) Calificacion final mayor a 7 y asistencia mayor a 75%

MENU
a) continuar ingresando datos
b) descartar datos ingresados
c) finalizar carga y mostrar resultados

AL FINALIZAR LA CARGA (no contar los libres (asistencia menor a 75%))
a) El promedio general de todas las calificaciones calculadas
b) la cantidad total de estudiantes aprobados
c) la calificacion mas alta registrada y el nombre de los alumnos

REPORTE
a) Conteo:
    1) "Aprobados con Honores", calificacion final 9 y 90% asistencia
    2) "Aprobados Regular", calificacion final mayor igual 7 y asistencia mayor igual 75
    3) "Reprobados por calificacion", calificacion final menor a 7
    4) "Reprobados por ausencia", calificacion final mayor igual a 7 pero asistencia menor a 75%
"""
promedio_generales = [] #aca almaceno el promedio de cada alumno si cumple con la asistencia, para luego calcular el promedio general
calificacion_mas_alta = 0 #aca voy a ir reemplazando la calificacion mas alta obtenida
nombres_calificacion_mas_alta = [] #aca voy a ir almacenando el o los nombres del alumno que obtuvo la calificacion mas alta
aprobado_Honores = [] #aca almaceno los nombres de los alumnos con la condicion solicitada, para luego obtener la cantidad y poder mostrar los nombres. Podria haber usado simplemente una variable de tipo contador
aprobado_Regular = [] #idem
reporbado_Calificacion = [] #idem
reprobado_Ausencia = [] #idem

nombre = input("Ingrese el nombre del alumno, si desea finalizar la carga ingrese \"salir\": ").lower() #logica para solicitar nombre o finalizar al escribir  la palabra especificada

while nombre!= "salir": #miestras que lo ingresado sea distinto a salir, hace lo siguiente:
    notas = [] #creo la variable notas como lista, para guardar las 3 notas aca y usar max(notas) para obtener la mayor, me ahorro logica y lineas de codigo que si usara 3 variables
    for i in range (3): #uso un for porque se que son 3 notas
        notas.append(float(input(f"ingrese la nota {i+1}: "))) # logica para agregar en la lista anterior las notas
    promedio = sum(notas)/3
    asistencia = int(input("Ingrese el porcentaje de asistencia: "))

    guardar = input("Desea guardar los cambios, escriba \"si\" o \"no\": ").lower() #solicito si se desea descartar lo cargado
    
    if guardar == "si": #logica para descartar los datos cargados
        # logica para guardar la nota mas alta########
        if max(notas) > calificacion_mas_alta: #si la nota mas alta del ultimo alumno que cargue, es mayor que la guardada
            nombres_calificacion_mas_alta.clear() #limpio la lista donde se guardaban los nombres de los alumnos con notas mas altas
            nombres_calificacion_mas_alta.append(nombre) #agrego el nuevo nombre
            calificacion_mas_alta = max(notas) #cambio el valor de la nota mas alta por el nuevo valor
        elif max(notas) == calificacion_mas_alta: # si la nota es igual a la que ya estaba registrada como mas alta
            nombres_calificacion_mas_alta.append(nombre) #solo agrego el nombre a la lista de alumno con mayor nota, ya que el valor de la nota esta en la variable 

        # logica para registrar los diferentes resultados posibles###
        if  promedio > 9 and asistencia > 90:
            promedio_generales.append(promedio) # agrego el promedio a la lista general de promedios
            aprobado_Honores.append(nombre) # agrego el nombre a la lista correspondiente

        elif promedio >= 7 and asistencia >= 75:
           promedio_generales.append(promedio)
           aprobado_Regular.append(nombre) 

        elif promedio < 7 and asistencia >= 75:
           promedio_generales.append(promedio)
           reporbado_Calificacion.append(nombre)

        else:
            reprobado_Ausencia.append(nombre)

    nombre = input("Ingrese el nombre del alumno, si desea finalizar la carga ingrese \"salir\": ").lower() #vuelvo a solicitar el nombre del alumno para continuar el ciclo while o salir

# Impresion de resultados, estos se calculan dentro del print, ya que para saber la cantidad de alumnos 
# uso len() para obtener la cantidad de nombres almacenados en la variable
print("\n******RESULTADOS******\n")
print(f"El promedio general de todas las calificaciones, sin incluir los alumnos libres fue de: {sum(promedio_generales)/len(promedio_generales)}")
print(f"La cantidad total de alumnos aprobados fue de: {len(aprobado_Honores)+len(aprobado_Regular)}") 
print(f"La calificacion de parcial mas alta registra fue de: {calificacion_mas_alta} y pertenece a: {nombres_calificacion_mas_alta}") 
print(f"La cantidad de alumnos aprobados con Honores fue de: {len(aprobado_Honores)} y sus nombres son: {aprobado_Honores}")  
print(f"La cantidad de alumnos aprobados Regular fue de: {len(aprobado_Regular)} y sus nombres son: {aprobado_Regular}")
print(f"Los alumnos que reprobaron por Calificacion fue de: {len(reporbado_Calificacion)} y sus nombres son: {reporbado_Calificacion}")
print(f"Los alumnos que reprobaron por no cumplir la asisencia fue de: {len(reprobado_Ausencia)} y sus nombres son: {reprobado_Ausencia}")
