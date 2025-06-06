"""¡El Gran Vendedor!

Tu programa debe hacer lo siguiente:Registrar el Valor de Cada Venta:
 Pide al usuario que ingrese el valor monetario de cada venta realizada. 
 Las ventas pueden ser cualquier número positivo. 
 El registro de ventas termina cuando el usuario escribe la palabra "fin" (sin importar mayúsculas o minúsculas).

Control de Errores (Opcional):
Si el usuario ingresa algo que no es un número válido (ej. "no vendí", "cancelada"),
 o un número negativo, tu programa debe mostrar un mensaje de error y no contar esa entrada como una venta válida.

Si no se registra ninguna venta antes de escribir "fin",
 tu programa debe manejar esta situación para evitar errores al mostrar los resultados.

Reporte del Gran Vendedor: Una vez que el usuario termine de ingresar ventas, 
tu programa debe mostrar un resumen claro que incluya:

Requerimientos:
El número total de ventas realizadas.
El valor total de los ingresos acumulados.
La venta individual de mayor valor.
La venta individual de menor valor.

"""

# defino variables
ventas = [] #aca voy a ir guardando los valores ingresados

while True: #es un bucle infinito de por si, no comprueba nada
    monto = input('Ingrese el monto a registrar, si desea finalizar ingrese "fin": ').lower() #se pide el monto y se lo convierte en minuscula
    if monto == "fin": #aca se comprueba si el usuario quiere salir
        break # este break interrumpe el proceso de este while(porque el usuario quiere salir), dijimos mas arriba que while true es infinito
    try: # intenta hacer lo siguiente
        valor = float(monto) # intenta convertir el monto que fue cargado como string a numero (el usuario puede meter cualquier cosa)
        if valor > 0: # si aparte de ser un numero es mayor a cero...
            ventas.append(valor) # agregalo a la lista "ventas=[]" el numero ingresado
        
    except ValueError: # si el string no se pudo convertir a numero, ej: se ingresa "hola", se activa el error ya que no puede convertir hola a numero
        print("No ingreso un valor valido, solo puede ingresar numeros o \"fin\" para finalizar")
    
    #python regresa al while, hasta que no se cargue "fin", ingrese al if y se active el brake, no se va a salir del while


if len(ventas) == 0: # utilizo un if para ver si no se registro una venta (carga de un numero), ya que el len lee la cantidad de elementos de la lista, si devuelve cero quiere decir esta vacia
    print("No se registraron ventas.")
else: # si hay aunque sea un numero dentro (el len va a devolver la cantidad) se hace lo siguiente
    totalVentas = sum(ventas) # se guarda en una variable la suma de los elementos de la lista. Python tiene la palabra reservada sum que es para sumar elementos dentro de listas
    maximaVenta = max(ventas) # idem anterior, max devuelve el valor maximo
    minimaVenta = min(ventas) # idem anterior, devuelve minimo
    cantidadVenta = len(ventas) # recordar que len devuelve la cantidad de elementos almacenados en una lista
    print(f"Cantidad de ventas: {cantidadVenta}")
    print(f"Total de ingresos: {totalVentas}")
    print(f"Venta máxima: {maximaVenta}")
    print(f"Venta mínima: {minimaVenta}")