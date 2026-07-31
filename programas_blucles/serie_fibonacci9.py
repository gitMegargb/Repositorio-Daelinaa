cantidad = int(input("¿Cuantos terminos de la serie Fibonacci deseas mostrar? "))

a = 0
b = 1

print("Serie Fibonacci: ")

for i in range(cantidad):
    print(a)
    siguiente = a + b
    a = b
    b = siguiente