"""crea un programa que solicite al operador ingresar el nombre de la persona, su peso, su altura
y calcule el IMC, se debera preguntar si se desea guardar el cambio. por ultimo, se debera mostrar cada
calculo 
"""
nombre=input("ingrese el nombre del paciente, ingrese \"no\" para finalizar la carga: ")

IMC=[]
nombres=[]
pesos=[]
alturas=[]
contador=0
guardar=""

while nombre != "no":

    
    peso=float(input("ingrese el peso: "))
    altura=float(input("ingrese la altura: "))
    imc=peso/(altura**2)   
    
    guardar=input("desea guardar los cambios, ingrese s/n: ")
    while guardar == "s" or guardar == "n":
        
        if guardar == "s":
            nombres.append(nombre)
            alturas.append(altura)
            pesos.append(peso)
            
            print("los datos ingresados fueron guardados")            
            IMC.append(imc)
            break
        elif guardar == "n":
            print("los datos no fueron guardados")
            break
        guardar=input("desea guardar los cambios, ingrese s/n: ")

    nombre=input("ingrese el nombre del paciente, ingrese \"no\" para finalizar la carga: ")

for i in range(len(nombres)):
    print(f"nombre: {nombres[i]}")
    print(f"altura: {alturas[i]}")
    print(f"peso: {pesos[i]}")
    print(f"IMC: {IMC[i]}")
    print("-------")
    

