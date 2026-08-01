numero = int(input("Ingresa un numero: "))

if numero < 2:
    print("No es un numero primo.")
else:
    primo = True
    
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print("Es un numero primo.")
    else:
        print("No es un numero primo.")