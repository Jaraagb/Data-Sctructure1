#Clases Empleado, Gerente, Desarrollador:
class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        print(f"{self.nombre} está trabajando en el departamento de {self.departamento}.")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def trabajar(self):
        self.supervisarAEquipo()

    def supervisarAEquipo(self):
        print(f"{self.nombre} está supervisando a su equipo de empleados.")

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguajeDeProgramacion):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion

    def trabajar(self):
        self.escribirCodigo()

    def escribirCodigo(self):
        print(f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}.")

#Clases FiguraGeométrica, Triángulo, Cuadrado:

class FiguraGeométrica:
    def calcularArea(self):
        pass

class Triángulo(FiguraGeométrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeométrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado ** 2
    
#Clases Electrodoméstico, Lavadora, Refrigerador:

class Electrodoméstico:
    def __init__(self, marca, modelo, consumoEnergético):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergético = consumoEnergético

    def encender(self):
        print(f"{self.marca} {self.modelo} está encendido.")

class Lavadora(Electrodoméstico):
    def __init__(self, marca, modelo, consumoEnergético, capacidad):
        super().__init__(marca, modelo, consumoEnergético)
        self.capacidad = capacidad

    def encender(self):
        self.iniciarCicloDeLavado()

    def iniciarCicloDeLavado(self):
        print(f"La lavadora {self.marca} {self.modelo} está iniciando el ciclo de lavado.")

class Refrigerador(Electrodoméstico):
    def __init__(self, marca, modelo, consumoEnergético, tieneCongelador):
        super().__init__(marca, modelo, consumoEnergético)
        self.tieneCongelador = tieneCongelador

    def encender(self):
        self.regularTemperatura()

    def regularTemperatura(self):
        print(f"El refrigerador {self.marca} {self.modelo} está regulando la temperatura.")

#Clases Usuario, Administrador, Cliente:

class Usuario:
    def __init__(self, nombreDeUsuario, contrasena):
        self.nombreDeUsuario = nombreDeUsuario
        self.contrasena = contrasena

    def iniciarSesion(self, usuario, contrasena):
        if usuario == self.nombreDeUsuario and contrasena == self.contrasena:
            print(f"{self.nombreDeUsuario} ha iniciado sesión.")
        else:
            print("Credenciales incorrectas.")

class Administrador(Usuario):
    def __init__(self, nombreDeUsuario, contrasena):
        super().__init__(nombreDeUsuario, contrasena)

    def gestionarUsuarios(self):
        print(f"El administrador {self.nombreDeUsuario} está gestionando usuarios.")

class Cliente(Usuario):
    def __init__(self, nombreDeUsuario, contrasena):
        super().__init__(nombreDeUsuario, contrasena)

    def realizarCompra(self):
        print(f"El cliente {self.nombreDeUsuario} está realizando una compra.")








