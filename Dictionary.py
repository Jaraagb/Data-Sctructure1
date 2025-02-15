persona =dict()

def agregar_valor(clave: str, valor: str):
    persona[clave] = valor
    print(f"Se agregó {clave}: {valor} a la persona")

def eliminar_valor(clave: str):
    if clave in persona:
        del persona[clave]
        print(f"Se eliminó {clave} de la persona")
    else:
        print(f"La clave '{clave}' no existe.")

def menu():
    while True:
        persona = dict()

def agregar_valor(clave: str, valor: str):
    persona[clave] = valor
    print(f"Se agregó {clave}: {valor} a la persona")

def eliminar_valor(clave: str):
    if clave in persona:
        del persona[clave]
        print(f"Se eliminó {clave} de la persona")
    else:
        print(f"La clave '{clave}' no existe en el diccionario.")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar persona")
        print("2. Eliminar persona")
        print("3. Ver lista de personas")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            clave = input("Introduce el nombre de la persona: ")
            valor = input(f"Introduce el valor asociado para {clave} (puede ser cualquier dato): ")
            agregar_valor(clave, valor)
        elif opcion == "2":
            clave = input("Introduce el nombre de la persona a eliminar: ")
            eliminar_valor(clave)
        elif opcion == "3":
            print("Lista de personas:", persona)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Llamada al menú
menu()



