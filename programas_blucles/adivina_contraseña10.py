contraseña = "python123"
intento = ""

while intento != contraseña:
    intento = input("Ingresa la contraseña: ")

    if intento == contraseña:
        print("Contraseña incorrecta. Intenta de nuevo.")

        print("¡Contraseña correcta! Acceso concedido.")