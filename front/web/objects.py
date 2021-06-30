class Cliente:
    def __init__(self, nombre, apellido, edad, nacimiento, primera) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacimiento = nacimiento
        self.primera = primera

class Mejor:
    def __init__(self, nombre, ultima, cantidad, gasto) -> None:
        self.nombre = nombre
        self.ultimaCompra = ultima
        self.cantidad = cantidad
        self.gasto = gasto

class Juego:
    def __init__(self, nombre, plataforma, lanzamiento, clasificacion, stock) -> None:
        self.nombre = nombre
        self.plataforma = plataforma
        self.lanzamiento = lanzamiento
        self.clasificacion = clasificacion
        self.stock = stock

class MasVendido:
    def __init__(self, nombre, ultima, copias, stock) -> None:
        self.nombre = nombre
        self.ultimaCompra = ultima
        self.copiasVendidas = copias
        self.stock = stock