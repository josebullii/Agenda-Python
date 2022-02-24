#Menú de inicio
def mostrarMenu():
    seleccion = 0

    while (seleccion<1) or (seleccion>6):
        print("1 - Añadir contacto")
        print("2 - Editar contacto")
        print("3 - Borrar contacto")
        print("4 - Buscar contacto")
        print("5 - Mostrar todos los contactos")
        print("6 - Salir\n")

        try:
            seleccion = int(input("Selecciona una opción: "))
        except:
            seleccion = 0
            print("No es correcto\n")

        if (seleccion<1) or (seleccion>6):
            print("Las opciones son 1, 2, 3, 4, 5 y 6\n")

    return seleccion

#Añadir contacto
def añadirContacto(vAgenda):

    nombre = input("Dime el nombre del contacto: ")
    numero = input("Escribe su número de teléfono: ")
    print("")
    contacto = nombre + (" - ") + numero

    vAgenda.append(contacto)

#Mostrar todos los contactos
def mostrarContactos():
    for contacto in vAgenda:
        print(contacto)


#Inicio del programa
print("***** AGENDA DE CONTACTOS *****\n")
vAgenda = []

opcion = mostrarMenu()
while (opcion != 6):
    if opcion == 1:
        print("Añadir contacto\n")
        añadirContacto(vAgenda)
    elif opcion == 2:
        print("Editar contacto\n")
    elif opcion == 3:
        print("Borrar contacto\n")
    elif opcion == 4:
        print("Buscar contacto\n")
    else:
        print("Mostrar todos los contactos\n")
        mostrarContactos()
    
    opcion = mostrarMenu()

print("Saliendo de la agenda... Encriptando datos de seguridad")