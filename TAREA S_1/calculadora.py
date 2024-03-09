# Calcudora simplet
def calculadora ():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    opciones = input("Ingrese la operacion que desea realizar: 1.Suma, 2.Resta, 3.Multiplicación, 4.División ")
    resultado = 0

    if opciones == "1":
        resultado = numero1 + numero2
        print("El resultado de la suma es: " + str(resultado))
    if opciones == "2":
        resultado = numero1 - numero2
        print("El resultado de la resta es: " + str(resultado))
    if opciones == "3":
        resultado = numero1 * numero2
        print("El resultado de la multiplicacion es: " + str(resultado))
    if opciones == "4":
        resultado = numero1 / numero2
        print("El resultado de la división es: " + str(resultado))


calculadora()
