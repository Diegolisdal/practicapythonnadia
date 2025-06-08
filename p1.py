"""crea un programa que solicite al operador ingresar el nombre de la persona, su peso, su altura
y calcule el IMC, se debera preguntar si se desea guardar el cambio. por ultimo, se debera mostrar cada
calculo 
"""
nombre=input("ingrese el nombre del paciente, ingrese \"no\" para finalizar la carga: ") # esta linea se debe repetir al final del bucle principal 

IMC=[] #listas vacias donde se van a ir guadando los resultados
nombres=[]
pesos=[]
alturas=[]

while nombre != "no": #bucle principal que permite cargar las personas hasta que se ingrese no
   
    peso=float(input("ingrese el peso: "))
    altura=float(input("ingrese la altura: "))
    imc=peso/(altura**2)   
    
    guardar=input("desea guardar los cambios, ingrese s/n: ") 
    while guardar == "s" or guardar == "n": # aca solo se acepta s o n como respuesta
        
        if guardar == "s": # si es s, se agregan con .append los datos
            nombres.append(nombre)
            alturas.append(altura)
            pesos.append(peso)
            
            print("los datos ingresados fueron guardados")            
            IMC.append(imc)
            break # interrumpe el while de guardar, si no me va a preguntar indefinidamente
        elif guardar == "n":
            print("los datos no fueron guardados")
            break # interrumpe el while de guardar, si no me va a preguntar indefinidamente
        

    nombre=input("ingrese el nombre del paciente, ingrese \"no\" para finalizar la carga: ") # aca es donde vuelvo a repetir la primera linea del while principal

borrar=input("Desea borrar el ultimo registro?  ingrese s/n: ")
if borrar == "s": #si la respuesta es s
    nombres.pop() #.pop() borra el utlimo elemento de una lista
    alturas.pop()
    pesos.pop()
    IMC.pop()

# no se pone else porque no hay que hacer nada si no quiero borrar

for i in range(len(nombres)): #muestro resultados, para eso averiguo con len la cantidad de elementos almacenados, para luego recorrerlos con i
    print(f"nombre: {nombres[i]}") # voy imprimiendo la posicion i de cada lista
    print(f"altura: {alturas[i]}")
    print(f"peso: {pesos[i]}")
    print(f"IMC: {IMC[i]}")
    print("-------")
    

