import math

numero = float(input("Ingrese un numero: "))

if numero >0:
    raiz = math.sqrt(numero)
    print("La raiz cuadrada es:", raiz)
else:
    print("No se puede calcular la raiz cuadrada de un numero negativo.")