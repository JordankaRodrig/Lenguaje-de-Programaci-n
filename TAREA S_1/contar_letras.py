# Solicitar al usuario que ingrese una frase
frase = input("Ingresa una frase o palabra: ")

# Inicializar el contador de letras
contador_letras = 0

# Iterar sobre cada caracter en la frase
for caracter in frase:
    # Verificar si el caracter es una letra
    if caracter.isalpha():
        contador_letras += 1

# Mostrar el resultado en la consola
print(f"La cantidad de letras en la frase es: {contador_letras}")
