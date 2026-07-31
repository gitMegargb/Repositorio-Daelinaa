pesos = float(input("Ingresa la cantidad en pesos mexicanos: "))

print("1. USD")
print("2. EUR")
print("3. THB")
print("4. JPY")
print("5. KRW")
print("6. AUD")
print("7. PEN")
print("8. CAD")
print("9. VES")
print("10. ARS")

opcion = input("Elige una opcion: ")

match opcion:
    case "1":
        print("USD:", pesos / 18.5)
    case "2":
        print("EUR:", pesos / 20.5)
    case "3":
        print("THB:", pesos * 1.9)
    case "4":
        print("JPY:", pesos * 8.4)
    case "5":
        print("KRW:", pesos * 74)
    case "6":
        print("AUD:", pesos / 12)
    case "7":
        print("PEN:", pesos / 5)
    case "8":
        print("CAD:", pesos / 13.5)
    case "9":
        print("VES:", pesos * 2)
    case "10":
        print("ARS:", pesos * 70)
    case _:
        print("Opcion no valida")