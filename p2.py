nombre=input("ingrese el nombre del paciente, ingrese \"no\" para finalizar la carga: ")
#variables globales#
IMC=[] 
nombres=[]
pesos=[]
alturas=[]

#funcion impresion#
def mostrar_resultados(a, b, c, d):
    for i in range(len(nombres)):
        print("-------")
        print(f"nombre: {a[i]}")
        print(f"altura: {b[i]}")
        print(f"peso: {c[i]}")
        print(f"IMC: {round(d[i],2)}")
        print("-------")

#inicio logica principal#
while nombre != "no":   #bucle general del programa
    try:    #manejo de errores con carga de datos
        peso=float(input("ingrese el peso: "))      #variable local (solo existe dentro del while)
        altura=float(input("ingrese la altura: "))  #variable local (solo existe dentro del while)
        imc=peso/(altura**2)                        #variable local (solo existe dentro del while)
        
    except(ValueError):                             #comprueba que solo se ingresen numeros
        print("debes ingresar un numero")
        continue                            # hace que la ejecucion regrese al try
    except(ZeroDivisionError):                      #comprueba que no sea divida por cero
        print("la altura no puede ser menor a cero")
        continue                            # hace que la ejecucion regrese al try

    
    guardar=input("desea guardar los cambios, ingrese s/n: ")
    
    while guardar != "s" and guardar != "n":    #bucle anidado al while principal, para que solo se pueda responder s o n
        print("Respuesta NO VALIDA, ingrese s o n")    
        guardar=input("desea guardar los cambios, ingrese s/n: ")

    if guardar == "s": #bucle anidado al while principal
        nombres.append(nombre) #se guarda la info en las listas globales
        alturas.append(altura) #se guarda la info en las listas globales
        pesos.append(peso)     #se guarda la info en las listas globales
        IMC.append(imc)   
        print("los datos ingresados fueron guardados")            
        
        
    elif guardar == "n":
        print("los datos no fueron guardados")
    

    nombre=input("ingrese el nombre del paciente, ingrese \"no\" para finalizar la carga: ")    #aca se reinicia el while principal

mostrar_resultados(nombres, alturas, pesos, IMC) #llamado a la funcion impresion 
    

