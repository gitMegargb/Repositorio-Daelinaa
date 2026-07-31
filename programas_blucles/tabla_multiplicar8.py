numero = int(input("Ingrese un numero: "))

print("Tabla de multiplicar del", numero)

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)