numeros = []

cantidad = int(input("¿Cuántos números vas a ingresar?: "))

for i in range(cantidad):
    numero = int(input("Ingresa un número: "))
    numeros.append(numero)

suma = 0

for numero in numeros:
    suma += numero

print("La suma de los elementos es:", suma)