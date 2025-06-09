"""
Una pequena empresa necesita un programa para relaizar un seguimiento basico del progreso de su proyecto interno
DEFINICION DEL PROYECTO
1) se registra su nombre
2) el lider del proyecto asignado
3) las horas estimadas para su finalizacion
4) las horas trabajadas hasta el momento (inicialmente cero). 
5) El porcentaje de avance de un proyecto se calcula como (horas trabajadas/ horas estimadas)*100 (asumir horas estimadas > 0 para este calculo). 
6) un proyecto se considera excedido en estimacion si las horas trabajadas son mayores que las horas estimadas
MENU DE OPERACIONES (solo letras mayusculas, caso contrario opcion no valida)
1) registrar nuevo proyecto (pidiendo nombre, lider, horas estimadas)
2) registrar horas trabajadas para un proyecto ya registrado (por nombre o identificador), se le sumaran a las ya existentes.
3) cargar nuevo proyecto (en caso de un error de carga)
4) mostrar reporte (antes de esta accion se debe pedir confirmacion)
AL FINALIZAR LA CARGA
1) se debe listar nombre, lider, horas estimadas, horas trabajadas, porcentaje avance. en orden de registro
2) el total de las horas estmiadas
3) el total de las horas trabajadas
4) mostrar advertencia cuando se exceda la estimacion
5) porcentaje de avance
REPORTES
1) Cantidad no iniciado
2) cantidad en curso HT > o y HT < HE
3) cantidad finalizado justo a tiempo HT > 0 y HT = HE
4) cantidad finalizado Excedido en horas HT > HE
"""
proyectos = [] #como debo poder buscar un proyecto y cambiar las horas trabajadas, utilizo una lista que cada elemento sera otra lista. la otra opcion seria usar diccionario
opcion = input("Que desea realizar:\n Si desea registrar un nuevo proyecto ingrese\"NUEVO\"\nSi desea registrar nuevas horas de un proyecto ingrese\"HORAS\"\nSi desea mostrar reporte ingrese \"MOSTRAR\"\nSi desea finalizar ingrese \"FINALIZAR\"\nOPCION: ")
while True:
    
    if opcion == "NUEVO":
        nombre = input("Ingrese el nombre del proyecto: ")
        lider = input("Ingrese el nombre del lider del proyecto: ")
        he = int(input("Ingrese las horas estimadas: "))
        ht = int(input("Ingrese las horas trabajadas: "))
        lista = [nombre, lider, he, ht, ht*100/he] #guardo toda la info en una lista
        proyectos.append(lista) #agrego la lista anterior como elemento de una lista
        print("Carga finalizada\n")                                                         #lista 1                        lista 2
        # si agrego 2 nuevos proyectos, la lista proyectos quedaria asi: proyectos=[["Extraccion","Pepe",90,30,33],["Remodelacion","Juan",100,50,50]]
    elif opcion == "HORAS":
        modificar = input("Ingrese el nombre del proyecto al cual desea sumar horas trabajadas: ")
        hs = int(input("Ingrese las horas que desee sumar al proyecto: "))
        for proyecto in proyectos: #recorro la lista general, proyecto va a 
            if proyecto[0] == modificar: #comparo el nombre ingresado con el nombre de la lista, que esta almacenada siempre en el primer lugar
                proyecto[3] = proyecto[3]+hs #reemplazo las horas trabajadas almacenadas en la psoicion 3
                proyecto[4] = proyecto[2]*100/proyecto[3] #reemplazo el porcentaje de avance
                print("Modificacion de horas trabajadas realizada \n")   

    elif opcion == "MOSTRAR":
        cantidad_no_iniciado = 0
        cantidad_en_curso= 0
        cantidad_finalizado_a_tiempo = 0
        cantidad_exedido = 0
        for proyecto in proyectos: # Muestro de a una lista dentro de la lista general de proyectos, cada elemento
            print("-----------------------------")
            print(f"Proyecto: {proyecto[0]}")
            print(f"Lider: {proyecto[1]}")
            print(f"Horas estimadas: {proyecto[2]}")
            print(f"Horas trabajadas: {proyecto[3]}")

            if proyecto[3] == 0: #logica para clasificar los proyectos, segun lo solicitado en reporte
               cantidad_no_iniciado = cantidad_no_iniciado + 1 

            elif proyecto[3] > 0 and proyecto[3] < proyecto[2]:
                cantidad_en_curso = cantidad_en_curso + 1

            elif proyecto[3] > 0 and proyecto[3] == proyecto[2]:
                cantidad_finalizado_a_tiempo = cantidad_finalizado_a_tiempo + 1

            elif proyecto[3] > proyecto[2]: #aparte de la logica de clasificar, coloco un print para advertir si esta excedido en tiempo
                cantidad_exedido = cantidad_exedido + 1
                print(f"EL PROYECTO SE ENCUENTRA EXEDIDO EN TIEMPO POR {proyecto[3]-proyecto[2]} HORAS")

            print(f"Porcentaje de avance: {proyecto[4]}")
            print("-----------------------------")

        print("\n") #finaliza la impresion de datos de cada proyecto, comienzo a mostrar lo solicitado en reportes
        print(f"La cantidad de proyectos no iniciados es de: {cantidad_no_iniciado}")
        print(f"La cantidad de proyectos en curso es de: {cantidad_en_curso}")
        print(f"La cantidad de proyectos finalizados justo a tiempo es de: {cantidad_finalizado_a_tiempo}")
        print(f"La cantidad de proyectos excedidos es de: {cantidad_exedido}\n")

    elif opcion == "FINALIZAR": #para finalizar el bucle infinito while True y terminar el programa
        print("Programa finalizado")    
        break #interrumpe la ejecucion del while, por ende no se ejecuta la linea que esta mas abajo ya que esta dentro de este
    
    opcion = input("Que desea realizar:\n Si desea registrar un nuevo proyecto ingrese\"NUEVO\"\nSi desea registrar nuevas horas de un proyecto ingrese\"HORAS\"\nSi desea mostrar reporte ingrese \"MOSTRAR\"\nSi desea finalizar ingrese \"FINALIZAR\"\nOPCION: ")
