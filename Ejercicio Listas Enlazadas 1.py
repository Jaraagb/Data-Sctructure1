from typing import Optional

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Animal:
    def __init__(self, nombre: str, edad: int, especie: str):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
    
    def __repr__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}"

class ListaAnimales:
    def __init__(self):
        self.primero = None
    
    def agregar(self, nombre: str, edad: int, especie: str):
        if self.existe(nombre, especie):
            print(f"El animal {nombre} de especie {especie} ya está registrado.")
            return
        nuevo_nodo = Nodo(Animal(nombre, edad, especie))
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo
    
    def existe(self, nombre: str, especie: str) -> Optional[Animal]:
        actual = self.primero
        while actual:
            if actual.dato.nombre == nombre and actual.dato.especie == especie:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def mostrar_iterativo(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente
    
    def mostrar_recursivo(self, nodo: Optional[Nodo]):
        if nodo:
            print(nodo.dato)
            self.mostrar_recursivo(nodo.siguiente)

# Ejemplo de uso
if __name__ == "__main__":
    registro = ListaAnimales()
    registro.agregar("Jaguar", 7, "Felino")
    registro.agregar("Cebra", 5, "Equino")
    registro.agregar("Lobo", 4, "Canino")
    registro.agregar("Cebra", 5, "Equino")  # No se agregará por ser repetido
    
    print("\nAnimales registrados (iterativo):")
    registro.mostrar_iterativo()
    
    print("\nAnimales registrados (recursivo):")
    registro.mostrar_recursivo(registro.primero)

