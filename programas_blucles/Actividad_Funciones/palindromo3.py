palabra = input("Ingrese una palabra: ").lower()

if palabra == palabra[::-1]:
    print("Es un palindromo.")
else:
    print("No es un palindromo.")