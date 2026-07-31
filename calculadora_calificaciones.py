parciales = float(input("ingrese la calificacion de parciales: "))
proyecto = float(input("ingrese la calificacion del proyecto: "))
examen = float(input("ingrese la calificacion del examen: "))

calificacion_final = (parciales * 0.40) + (proyecto * 0.30) + (examen * 0.30)

print("La calificacion final es:" , calificacion_final)

if calificacion_final >= 70:
    print("Resultado: Aprobado")
else:
    print("Resultado: Reprobado")