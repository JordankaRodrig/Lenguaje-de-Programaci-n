# Funcion para calcular el descuento
def calcular_descuento(precio):
    if precio > 500:
        descuento = 0.10 * precio
        precio_con_descuento = precio - descuento
        return precio_con_descuento
    else:
        return precio

# Funcion principal
def aplicacion_descuento():
    print("Aplicacion de Descuento")

    # Solicitar al usuario ingresar el precio del producto
    precio_producto = float(input("Ingrese el precio del producto en cordobas: "))

    # Calcular el precio con descuento utilizando la funcion
    precio_final = calcular_descuento(precio_producto)

    # Mostrar el resultado al usuario
    print(f"El precio final con descuento es: {precio_final} cordobas")

# Llamar a la funcion principal
aplicacion_descuento()
