import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    numero = int(input("Adivina el numero (1-100): "))
    intentos += 1

    if numero < numero_secreto:
        print("El numero es mayor. ")
    elif numero > numero_secreto:
        print("El numero es menor. ")
    else:
        print("¡Felicidades! Adivinaste el numero.")
        print("Intentos realizados:", intentos)
        break