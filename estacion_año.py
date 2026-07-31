mes = input("ingrese un mes: ").lower()

match mes:
    case "diciembre" | "enero" | "febrero":
        print("La estación es invierno")
    case "marzo" | "abril" | "mayo":
        print("La estación es primavera")
    case "junio" | "julio" | "agosto":
        print("La estación es verano")
    case "septiembre" | "octubre" | "noviembre":
        print("La estación es otoño")
    case _:
        print("Mes no válido")
        