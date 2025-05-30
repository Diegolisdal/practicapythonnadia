# definicion para validar float del error del tipo ValueError
def validar_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
    
        except(ValueError):                            
            print("No se acepta texto, debes ingresar un numero")
            continue                           
                           
        return valor
    
# definicion para validar int del error del tipo ValueError    
def validar_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
    
        except(ValueError):                            
            print("No se acepta texto, debes ingresar un numero")
            continue                           
                           
        return valor  
numero = validar_float("ingrese un dividendo: ")
numero1 = validar_int("ingrese un numero: ")
""" aca incluyo valizar division cero
divisor= validar("ingrese un divisor")
while divisor == 0:
    divisor= validar("ingrese un divisor")

resultado= dividendo/divisor 
"""