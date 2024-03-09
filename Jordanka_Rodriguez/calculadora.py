def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No es posible dividir por cero."

# Funcion principal
def calculadora():
    print("Calculadora basica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    # Solicitar al usuario que elija una operacion
    opcion = input("Ingrese el numero de la operacion deseada (1/2/3/4): ")

    # Solicitar al usuario que ingrese dos numeros
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Realizar la operacion segun la opcion seleccionada
    if opcion == '1':
        resultado = suma(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == '2':
        resultado = resta(num1, num2)
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == '3':
        resultado = multiplicacion(num1, num2)
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif opcion == '4':
        resultado = division(num1, num2)
        print(f"El resultado de la division es: {resultado}")
    else:
        print("Opcion no valida. Por favor, ingrese un numero valido (1/2/3/4).")

# Llamar a la funcion principal
calculadora()
