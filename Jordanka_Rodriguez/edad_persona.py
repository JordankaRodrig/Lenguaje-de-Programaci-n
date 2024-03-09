# Funcion para determinar si una persona es mayor o menor de edad
def verificar_edad(edad):
    if edad >= 18:
        return "Es mayor de edad."
    else:
        return "Es menor de edad."

# Funcion principal
def main():
    # Solicitar al usuario que ingrese su edad
    try:
        edad = int(input("Ingrese su edad: "))
        
        # Llamar a la funcion verificar_edad y mostrar el resultado
        resultado = verificar_edad(edad)
        print(resultado)

    except ValueError:
        print("Error: Por favor, ingrese un valor numerico para la edad.")

# Llamar a la funcion principal
main()
