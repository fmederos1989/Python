from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self.id = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return (f'''Nombre: {self.nombre}
{self.monitor}
{self.teclado}
{self.raton}\n\n''')

# Codigo de prueba

if __name__ == '__main__':
    monitor = Monitor('Samsung', '27"')
    teclado = Teclado('Logitech', 'USB')
    raton = Raton('Razer', 'Bluetooth')
    computadora = Computadora('PC 1', monitor, teclado, raton)
    print(computadora)

    monitor2 = Monitor('Dell', '24"')
    teclado2 = Teclado('Razer', 'Bluetooth')
    raton2 = Raton('Logitech', 'USB')
    computadora2 = Computadora('PC 2', monitor2, teclado2, raton2)
    print(computadora2)