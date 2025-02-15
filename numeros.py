
numero = list()

def agregarNumero(numero_agregar):
    numero.append(numero_agregar)
    print(f"Se agregó {numero_agregar} a la lista.")


def eliminarNumero(numero_eliminar):
    if numero_eliminar in numero:
        numero.pop(numero.index(numero_eliminar))
        print(f"Se eliminó {numero_eliminar} de la lista.")
    else:
        print(f"El número {numero_eliminar} no se encuentra en la lista.")
    

def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar número a la lista")
        print("2. Eliminar número de la lista")
        print("3. Ver lista")
        print("4. Agregar Varios Numeros")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            numero_agregar = int(input("Introduce el número que deseas agregar: "))
            agregarNumero(numero_agregar)
        elif opcion == "2":
            numero_eliminar = int(input("Introduce el número que deseas eliminar: "))
            eliminarNumero(numero_eliminar)
        elif opcion == "3":
            print("Lista actual:", numero)
            if not numero:
                print("La lista actual esta vacia")
        elif opcion == "4":
             print("Saliendo")
             break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
