numeros = []

cantidad = int(input("¿Cuántos números vas a ingresar?: "))

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

mayor = max(numeros)
menor = min(numeros)

print("Lista:", numeros)
print("Número mayor:", mayor)
print("Número menor:", menor)