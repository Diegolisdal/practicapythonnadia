nombre=input("ingrese el nombre del paciente, ingrese \"no\" para finalizar la carga: ")

IMC=[]
nombres=[]
pesos=[]
alturas=[]

def mostrar_resultados(a, b, c, d):
    for i in range(len(nombres)):
        print("-------")
        print(f"nombre: {a[i]}")
        print(f"altura: {b[i]}")
        print(f"peso: {c[i]}")
        print(f"IMC: {round(d[i],2)}")
        print("-------")


while nombre != "no":
    try:
        peso=float(input("ingrese el peso: "))
        altura=float(input("ingrese la altura: "))
        imc=peso/(altura**2) 
    except(ValueError):
        print("debes ingresar un numero")
        continue
    except(ZeroDivisionError):
        print("la altura no puede ser menor a cero")
        continue

    guardar=""
    guardar=input("desea guardar los cambios, ingrese s/n: ")
    
    while guardar != "s" and guardar != "n":
        print("Respuesta NO VALIDA, ingrese s o n")    
        guardar=input("desea guardar los cambios, ingrese s/n: ")

    if guardar == "s":
        nombres.append(nombre)
        alturas.append(altura)
        pesos.append(peso)
            
        print("los datos ingresados fueron guardados")            
        IMC.append(imc)
        
    elif guardar == "n":
        print("los datos no fueron guardados")
    

    nombre=input("ingrese el nombre del paciente, ingrese \"no\" para finalizar la carga: ")

mostrar_resultados(nombres, alturas, pesos, IMC)
    

