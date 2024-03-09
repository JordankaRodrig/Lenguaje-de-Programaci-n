class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

# Funcion para agregar un contacto a la lista
def agregar_contacto(lista_contactos, contacto):
    lista_contactos.append(contacto)
    print(f"Contacto '{contacto.nombre}' agregado correctamente.")

# Funcion para mostrar la lista de contactos
def mostrar_contactos(lista_contactos):
    print("Lista de Contactos:")
    for contacto in lista_contactos:
        print(f"Nombre: {contacto.nombre}, Telefono: {contacto.telefono}")

# Crea una lista vacia para almacenar los contactos
lista_de_contactos = []

# Menu de opciones para el usuario
while True:
    print("\nGestión de Contactos")
    print("1. Agregar Contacto")
    print("2. Mostrar Contactos")
    print("3. Salir")

    opcion = input("Ingrese el numero de la opcion deseada (1/2/3): ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el numero de telefono del contacto: ")
        nuevo_contacto = Contacto(nombre, telefono)
        agregar_contacto(lista_de_contactos, nuevo_contacto)

    elif opcion == '2':
        mostrar_contactos(lista_de_contactos)

    elif opcion == '3':
        print("Saliendo del programa.¡Hasta luego!")
        break

    else:
        print("Opcion no valida.favor, ingrese un numero valido (1/2/3).")
