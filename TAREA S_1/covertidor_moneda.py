# Definir tasas de cambio ficticias
tasas_de_cambio = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0}

# Solicitar al usuario la cantidad de dinero y la moneda de origen
cantidad = float(input("Ingresa la cantidad de dinero: "))
moneda_origen = input("Ingresa la moneda de origen: (USD, EUR, GBP, JPY): ").upper()

# Verificar si la moneda de origen es válida
if moneda_origen not in tasas_de_cambio:
    print("Moneda de origen no válida.")
else:
    # Permitir al usuario seleccionar la moneda de destino
    moneda_destino = input("Ingresa la moneda de destino: (USD, EUR, GBP, JPY): ").upper()

    # Verificar si la moneda de destino es válida
    if moneda_destino not in tasas_de_cambio:
        print("Moneda de destino no válida.")
    else:
        # Calcular el monto convertido
        monto_convertido = cantidad * (tasas_de_cambio[moneda_destino] / tasas_de_cambio[moneda_origen])

        # Mostrar el resultado en la consola
        print(f"{cantidad} {moneda_origen} equivale a: {monto_convertido:.2f} {moneda_destino}")
