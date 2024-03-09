import random

# Generar un número aleatorio entre 1 y 30
numero = random.randint(1, 30)

print("Bienvenido al juego de Adivina el Número.")
print("Intenta adivinar un número entre 1 y 30.")

intentos = 0

while True:
    # Solicitar al usuario que ingrese su suposición
    suposicion = int(input("Ingresa tu suposición: "))
    
    # Incrementar el contador de intentos
    intentos += 1
    
    # Verificar si el numero es correcto
    if suposicion == numero:
        print(f"¡Felicidades! has adivinado el número en: {intentos} intentos.")
        break
    elif suposicion < numero:
        print("El número es más alto. Intenta de nuevo.")
    else:
        print("El número es más bajo. Intenta de nuevo.")

