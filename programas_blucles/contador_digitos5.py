numero = int(input("Ingrese un numero entero: "))

numero = abs(numero)

contador = 0

if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero = numero // 10
        contador += 1

        print("El numero tiene", contador, "digitos.")