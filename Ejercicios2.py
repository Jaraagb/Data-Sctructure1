class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años y soy {self.genero}.")

# Ejemplo de uso
persona = Persona("Juan", 30, "masculino")
persona.presentarse()

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class CuentaBancaria:
    def __init__(self, titular, saldo, numeroDeCuenta):
        self.titular = titular
        self.saldo = saldo
        self.numeroDeCuenta = numeroDeCuenta

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("No hay suficiente saldo para realizar el retiro.")

    def consultarSaldo(self):
        return self.saldo


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        import math
        return math.pi * (self.radio ** 2)

    def calcularCircunferencia(self):
        import math
        return 2 * math.pi * self.radio


class Libro:
    def __init__(self, titulo, autor, genero, anioDePublicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anioDePublicacion = anioDePublicacion

    def obtenerTitulo(self):
        return self.titulo

    def obtenerAutor(self):
        return self.autor

    def obtenerGenero(self):
        return self.genero

    def obtenerAnioDePublicacion(self):
        return self.anioDePublicacion

    def mostrarDetalles(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print(f"Año de publicación: {self.anioDePublicacion}")


class Cancion:
    def __init__(self, titulo, artista, album, duracion):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

    def obtenerTitulo(self):
        return self.titulo

    def obtenerArtista(self):
        return self.artista

    def obtenerAlbum(self):
        return self.album

    def obtenerDuracion(self):
        return self.duracion

    def reproducir(self):
        print(f"Reproduciendo '{self.titulo}' de {self.artista}.")


class Producto:
    def __init__(self, nombre, precio, cantidadDisponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidadDisponible = cantidadDisponible

    def obtenerNombre(self):
        return self.nombre

    def obtenerPrecio(self):
        return self.precio

    def obtenerCantidadDisponible(self):
        return self.cantidadDisponible

    def calcularTotal(self, cantidad):
        if cantidad <= self.cantidadDisponible:
            return self.precio * cantidad
        else:
            print("No hay suficiente cantidad disponible.")
            return 0


class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []

    def agregarCalificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def calcularPromedio(self):
        if len(self.calificaciones) > 0:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0

    def determinarEstado(self):
        promedio = self.calcularPromedio()
        if promedio >= 6:
            return "Aprobado"
        else:
            return "Reprobado"
