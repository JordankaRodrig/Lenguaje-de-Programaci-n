# Solicitar al usuario que ingrese un número entero
numero = input("Ingresa un número entero: ")

# Inicializar la suma de dígitos
suma_digitos = 0

# Verificar si la entrada es un número entero
if numero.isdigit():
    # Iterar sobre cada dígito en el número
    for digito in numero:
        suma_digitos += int(digito)

    # Mostrar el resultado en la consola
    print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
else:
    print("Por favor, ingresa un número entero válido.")
