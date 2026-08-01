numeros = []

cantidad = int(input("¿Cuantos elementos tendra la lista? "))

for i in range(cantidad):
    numero = float(input(f"Ingresa el elemento {i + 1}: "))
    numeros.append(numero)

    print("Lista original:", numeros)

    numeros.reverse()

    print("Lista invertida:", numeros)