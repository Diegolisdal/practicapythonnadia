# manejo error  division por cero
"""
try: 
    a=int(input("ingrese numero a: "))
    b=int(input("ingrese numero b: "))
    promedio=a/b
        
except(ZeroDivisionError):    
    while b == 0:
        b=int(input("b no puede valer 0, ingrese nuevamente un valor para b: "))
    promedio=a/b
print(f"el promedio es: {promedio}")
"""
# manejo error variable no debe ser str
while True:
    try:
        a=int(input("ingrese el valor de a: "))
        b=int(input("ingrese el valor de b: "))
        promedio=a/b
        break
    except(ValueError):
        print("se debe ingresar valores numericos")
    except(ZeroDivisionError):
         print("No se puede dividir por 0, ingrese nuevamente los valores ")
print(promedio)    