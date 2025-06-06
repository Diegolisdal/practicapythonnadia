""" realice un programa que solicite nombre, peso y altura de personas para luego calcular el imc
se debera poder ingresar personas hasta que el usuario desee terminar la carga, ingresando la palabra no
tambien debera preguntar si se desea guardar o no a la persona luego de cargar sus datos
por ultimo, se debe mostrar todos los datos de todas las personas cargadas 
"""
nombre=input("ingrese el nombre del paciente, ingrese \"no\" para finalizar la carga: ")
#variables globales#
IMC=[] 
nombres=[]  # ejemplo de como se guarda nombres=["diego","nadia","pepe"]
pesos=[]    # ejemplo de como se guarda pesos=[72,52,108]
alturas=[]  # ejemplo de como se guarda alturas=[1.82,1.62,2.0]
   

#inicio logica principal#
while nombre != "no":   #bucle general del programa, se repite hasta que el usuario ingresa no
    
        peso=float(input("ingrese el peso: "))      #variable local (solo existe dentro del while)
        altura=float(input("ingrese la altura: "))  #variable local (solo existe dentro del while)
        imc=peso/(altura**2)                        #variable local (solo existe dentro del while)
        
                             # hace que la ejecucion regrese al try

    
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

for i in range(len(nombres)): #len lee el la cantidad de nombres que tiene la lista, en vez de usar for i in range(), como no se sabe cuantos nombres hay almacenados se obtiene la cantidad con len
    print("-------")            # se usa un for i in range para que la "i" al tomar el primer valor, imprima el primer dato de cada variable, que es como se guardo la informacion de las personas
    print(f"nombre: {nombres[i]}")
    print(f"altura: {alturas[i]}")
    print(f"peso: {pesos[i]}")
    print(f"IMC: {round(IMC[i],2)}")
    print("-------")
    

"""
comentario del print con el ejemplo de estos datos simulados
nombres=["diego","nadia","pepe"]
pesos=[72,52,108]
alturas=[1.82,1.62,2.0]
IMC=[2,3,5.6]

el range es 3, ya que el len(nombres) es la cantidad de nombres guardados en esa variable "nombres"
entonces, "i" va a tomar 3 valores (0,1, y 2)
luego se imprime el primer elemento de cada lista, usando  print(f"nombre: {nombres[i]}"), print(f"altura: {alturas[i]}"), etc
al terminar el ultimo valor, vuelve al for, donde "i" toma el valor 1, donde ahora se va a imprimir el contenido en la posicion 1 de cada lista   
"""