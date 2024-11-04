class DispositivoEntrada():
    def __init__(self, marca, tipo_entrada):
        self.marca = marca
        self.tipo_entrada = tipo_entrada

class Raton(DispositivoEntrada):
    cantidad_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.cantidad_ratones =+ 1
        self.id = Raton.cantidad_ratones
        self.marca = marca
        self.tipo_entrada = tipo_entrada

    def __str__(self):
        return f'Raton: {self.id} // Marca: {self.marca} // Tipo de entrada: {self.tipo_entrada}'

class Teclado(DispositivoEntrada):
    cantidad_teclados = 0

    def __init__(self, marca):
        Teclado.cantidad_teclados =+ 1
        self.id = Teclado.cantidad_teclados
        self.marca = marca
        self.tipo_entrada = 'Teclado'

    def __str__(self):
        return f'Teclado: {self.id} // Marca: {self.marca} // Tipo de entrada: {self.tipo_entrada}'


class Monitor():
    cantidad_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.cantidad_monitores =+ 1
        self.id = Monitor.cantidad_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return f'Monitor: {self.id} // Marca: {self.marca} // Tamaño: {self.tamanio}'

class Computadora():
    cantidad_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.cantidad_computadoras =+ 1
        self.id = Computadora.cantidad_computadoras
        self.nombre = nombre
        self.monitor = Monitor()
        self.teclado = teclado
        self.raton = raton
