suma = 0

while True:
    numero = float(input("Ingresa un numero (negativo para terminar): "))

    if numero < 0:
        break

    suma += numero

print("La suma de los numeros positivos es:", suma)