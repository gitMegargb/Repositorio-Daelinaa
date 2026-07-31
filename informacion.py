print("Selecciona una opcion:")
print("1. Artista")
print("2. Pelicula")
print("3. Serie")
print("4. Videojuego")
print("5. Animal")

opcion = input("Elige una opcion: ")

match opcion:
    case "1":
        print("Artista: Taylor Swift es una cantante y compositora estadounidense.")
    case "2":
        print("Pelicula: Intensamente es una pelicula animada de Pixar.")
    case "3":
        print("Serie: Stranger Things es una serie de ciencia ficcion.")
    case "4":
        print("Videojuego: Minecraft es un juego de construccion y aventura.")
    case "5":
        print("Animal: El delfin es un mamifero marino muy inteligente.")
    case _:
        print("Opcion no valida.")