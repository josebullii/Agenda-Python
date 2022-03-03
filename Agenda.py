#Menú de inicio
from operator import index


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

#Buscar contacto (devuelve su posición en la lista)
def buscarContacto(vAgenda):
    v = []
    dato = input("Dime el nombre o el teléfono que deseas buscar: ")
    cont = 0
    for i in vAgenda:
        if i.find(dato) >= 0:
            return cont
        cont = cont + 1
    print("Contacto no existente")

#Mostrar la información del contacto
def muestraContacto(vAgenda, index):
    if(index != None):
        datos = vAgenda[index].split("-")
        print("Nombre: ", datos[0])
        print("Número: ", datos[1], "\n")

#Borrar contacto
def borrarContacto(vAgenda, index):
    vAgenda.pop(index)

#Editar contacto
def editarContacto(vAgenda, index):
    index = buscarContacto(vAgenda)
    if index != None:
        vAgenda.pop(index)
        nombre = input("Dime el nuevo nombre del contacto: ")
        numero = input("Escribe su nuevo número de teléfono: ")
        index = nombre + (" - ") + numero

        vAgenda.append(index)
        print("Contacto editado\n")

#Mostrar todos los contactos
def mostrarContactos():
    for contacto in vAgenda:
        print(contacto, "\n")

#Inicio del programa
print("***** AGENDA DE CONTACTOS *****\n")
vAgenda = []

opcion = mostrarMenu()
while (opcion != 6):
    if opcion == 1:
        añadirContacto(vAgenda)

    elif opcion == 2:
        editarContacto(vAgenda, index)

    elif opcion == 3:
        #Borrar contacto de la agenda
        index = buscarContacto(vAgenda)
        if index != None:
            vAgenda.pop(index)
            print("Contacto eliminado\n")

    elif opcion == 4:
        muestraContacto(vAgenda, buscarContacto(vAgenda))

    else:
        mostrarContactos()
    
    opcion = mostrarMenu()

print("Saliendo de la agenda... Encriptando datos de seguridad")