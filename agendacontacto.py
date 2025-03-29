class Node:
    def __init__(self, key, phone, email):
        self.key = key      # key es el nombre del contacto
        self.value = {"phone": phone, "email": email}  # Diccionario con teléfono y email
        self.next = None    # next es para manejar las colisiones (encadenamiento)

class Phonebook:
    def __init__(self, size=10):
        self.size = size          # Tamaño de la tabla hash
        self.table = [None] * size  # Inicializa la tabla hash con valores vacíos
    
    def Fhash(self, key):
        hash_value = 0
        for i, c in enumerate(key):
            hash_value += (ord(c) * (i + 1))  # Multiplicamos el valor ASCII por su posición
            return hash_value % self.size  # Aplicamos el módulo para que el valor esté dentro del rango adecuado

    
    def insert(self, key, phone, email):
        index = self.Fhash(key)  # Calculamos el índice de la tabla
        new_node = Node(key, phone, email)
        
        if self.table[index] is None:
            # Si no hay colisión, colocamos el nodo en esa posición
            self.table[index] = new_node
        else:
            # Si hay colisión, buscamos el último nodo en esa posición y lo agregamos
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node
    
    def search(self, key):
        index = self.Fhash(key)  # Calculamos el índice donde debería estar el contacto
        current = self.table[index]
        
        while current:
            if current.key == key:  # Si encontramos el contacto
                return current.value  # Devuelve el diccionario con teléfono y email
            current = current.next
        return None  # Si no lo encontramos, devolvemos None
    
    def delete(self, key):
        index = self.Fhash(key)  # Calculamos el índice donde debería estar el contacto
        current = self.table[index]
        previous = None
        
        while current:
            if current.key == key:  # Si encontramos el contacto
                if previous:
                    previous.next = current.next  # Saltamos el nodo
                else:
                    self.table[index] = current.next  # Si es el primero en la lista, lo eliminamos
                return True
            previous = current
            current = current.next
        return False  # Si no encontramos el contacto, devolvemos False

# Crear una instancia de Phonebook (agenda)
agenda = Phonebook()

# Insertar contactos
agenda.insert("Juan", "555-1234", "juan@example.com")
agenda.insert("Maria", "555-5678", "maria@example.com")
agenda.insert("Carlos", "555-8765", "carlos@example.com")
agenda.insert("Alicia", "555-1122", "alicia@example.com")

# Buscar un contacto
print("Buscar a Juan:", agenda.search("Juan"))  # Salida: {'phone': '555-1234', 'email': 'juan@example.com'}
print("Buscar a Maria:", agenda.search("Maria"))  # Salida: {'phone': '555-5678', 'email': 'maria@example.com'}

# Eliminar un contacto
agenda.delete("Carlos")
print("Buscar a Carlos después de eliminar:", agenda.search("Carlos"))  # Salida: None

# Buscar un contacto eliminado
print("Buscar a Alicia:", agenda.search("Alicia"))  # Salida: {'phone': '555-1122', 'email': 'alicia@example.com'}
