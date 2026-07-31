celsius = float(input("ingrese los grados Celsius: "))

print("1. Fahrenheit")
print("2. Kelvin")

opcion = input("Elige una opcion: ")

match opcion:
    case "1":
        fahrenheit = (celsius * 9/5) + 32
        print("Grados Fahrenheit: ", fahrenheit)
    case "2":
        kelvin = celsius + 273.15
        print("Grados Kelvin:", kelvin)
    case _:
        print("Opcion no valida")