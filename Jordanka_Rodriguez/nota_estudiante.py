# Funcion para determinar si un estudiante recibe una beca
def otorgar_beca(nota):
    if nota > 95:
        return "Felicidades, has obtenido la beca."
    else:
        return "Lo siento, no cumples con los requisitos para la beca."

# Funcion principal
def main():
    # Solicitar al usuario que ingrese la nota del estudiante
    try:
        nota = float(input("Ingrese la nota del estudiante (porcentaje): "))
        
        # Llamar a la funcion otorgar_beca y mostrar el resultado
        resultado = otorgar_beca(nota)
        print(resultado)

    except ValueError:
        print("Error: Por favor, ingrese un valor numerico para la nota.")

# Llamar a la función principal
main()
