salario_bruto = float(input("ingrese el salario bruto: "))
porcentaje = float(input("ingrese el porcentaje de impuesto y deducciones: "))

descuento = salario_bruto * (porcentaje / 100)
salario_neto = salario_bruto - descuento

print("El salario neto es: ", salario_neto)