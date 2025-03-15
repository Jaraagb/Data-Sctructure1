from datetime import datetime

class Nodo:
    def __init__(self, tarea):
        self.dato = tarea
        self.siguiente = None

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_limite):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_limite = datetime.strptime(fecha_limite, "%Y-%m-%d")
    
    def __repr__(self):
        return f"Descripción: {self.descripcion}, Prioridad: {self.prioridad}, Fecha límite: {self.fecha_limite.strftime('%Y-%m-%d')}"

class ListaTareas:
    def __init__(self):
        self.primero = None
    
    def agregar(self, descripcion, prioridad, fecha_limite):
        nueva_tarea = Nodo(Tarea(descripcion, prioridad, fecha_limite))
        if not self.primero or (self.primero.dato.prioridad > prioridad or (self.primero.dato.prioridad == prioridad and self.primero.dato.fecha_limite > nueva_tarea.dato.fecha_limite)):
            nueva_tarea.siguiente = self.primero
            self.primero = nueva_tarea
        else:
            actual = self.primero
            while actual.siguiente and (actual.siguiente.dato.prioridad < prioridad or (actual.siguiente.dato.prioridad == prioridad and actual.siguiente.dato.fecha_limite <= nueva_tarea.dato.fecha_limite)):
                actual = actual.siguiente
            nueva_tarea.siguiente = actual.siguiente
            actual.siguiente = nueva_tarea
    
    def eliminar(self, descripcion=None, posicion=None):
        if not self.primero:
            return False
        
        if descripcion:
            if self.primero.dato.descripcion == descripcion:
                self.primero = self.primero.siguiente
                return True
            actual = self.primero
            while actual.siguiente and actual.siguiente.dato.descripcion != descripcion:
                actual = actual.siguiente
            if actual.siguiente:
                actual.siguiente = actual.siguiente.siguiente
                return True
        
        elif posicion is not None:
            if posicion == 0:
                self.primero = self.primero.siguiente
                return True
            actual = self.primero
            contador = 0
            while actual.siguiente and contador < posicion - 1:
                actual = actual.siguiente
                contador += 1
            if actual.siguiente:
                actual.siguiente = actual.siguiente.siguiente
                return True
        return False
    
    def mostrar(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente
    
    def buscar(self, descripcion):
        actual = self.primero
        while actual:
            if actual.dato.descripcion == descripcion:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def completar(self, descripcion):
        return self.eliminar(descripcion=descripcion)

# Ejemplo de uso
if __name__ == "__main__":
    tareas = ListaTareas()
    tareas.agregar("Comprar pan", 1, "2025-03-10")
    tareas.agregar("Revisión médica", 2, "2025-03-12")
    tareas.agregar("Pagar impuestos", 1, "2025-03-15")
    tareas.agregar("Ir al gimnasio", 3, "2025-03-11")
    
    print("Lista de tareas:")
    tareas.mostrar()
    
    print("\nEliminando 'Revisión médica'...")
    tareas.eliminar(descripcion="Revisión médica")
    tareas.mostrar()
    
    print("\nBuscando 'Pagar impuestos'...")
    tarea_encontrada = tareas.buscar("Pagar impuestos")
    print(tarea_encontrada if tarea_encontrada else "No encontrada")
    
    print("\nCompletando 'Comprar pan'...")
    tareas.completar("Comprar pan")
    tareas.mostrar()
