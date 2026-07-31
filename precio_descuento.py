precio = float(input("ingresa el precio del producto: "))

if precio <= 100:
    descuento = 0
elif precio <= 200:
    descuento = 0.10
elif precio <= 500:
    descuento = 0.20
else:
    descuento = 0.30

total = precio - (precio * descuento)

print("Descuento aplicado: ", descuento * 100, "%")
print("Total a pagar: ", total)