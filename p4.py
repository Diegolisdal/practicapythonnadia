n1=int(input("ingrese el primer numero: "))
n2=int(input("ingrese el segundo numero: "))
numero=n1
while numero > n1 and numero < n2:
    if numero%2 == 0:
        print(numero)
        numero=numero +1
    else:
        numero=numero +1