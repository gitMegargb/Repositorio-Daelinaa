saldo = 1000

while True:
    print("\n=== CAJERO AUTOMÁTICO ===")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Tu saldo es:", saldo)

    elif opcion == "2":
        deposito = float(input("Ingresa la cantidad a depositar: "))
        saldo += deposito
        print("Depósito realizado.")
        print("Nuevo saldo:", saldo)

    elif opcion == "3":
        retiro = float(input("Ingresa la cantidad a retirar: "))

        if retiro <= saldo:
            saldo -= retiro
            print("Retiro realizado.")
            print("Nuevo saldo:", saldo)
        else:
            print("Fondos insuficientes.")

    elif opcion == "4":
        print("Gracias por usar el cajero.")
        break

    else:
        print("Opción no válida.")