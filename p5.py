# definicion para validar TODOS los float del error del tipo ValueError
def validar_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
    
        except(ValueError):                            
            print("No se acepta texto, debes ingresar un numero")
            continue                           
                           
        return valor
    
# definicion para validar TODOS los int del error del tipo ValueError    
def validar_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
    
        except(ValueError):                            
            print("No se acepta texto, debes ingresar un numero")
            continue                           
                           
        return valor  
    
#como usar la validacion, en vez de usar peso=float(input("ingrese su peso: ")), uso    
peso = validar_float("ingrese su peso: ")
altura = validar_float("ingrese su altura en metros: ")
#como usar la validacion, en vez de usar edad=int(input("ingrese su edad: ")), uso
edad = validar_int("ingrese su edad: ")
print(peso, altura, edad)
