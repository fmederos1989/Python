
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado
from orden import Orden

print('*** App Mundo PC ***')

# Creamos algunas computadoras
monitor = Monitor('Samsung', '27"')
teclado = Teclado('Logitech', 'USB')
raton = Raton('Razer', 'Bluetooth')
computadora = Computadora('PC 1', monitor, teclado, raton)

monitor2 = Monitor('Dell', '24"')
teclado2 = Teclado('Razer', 'Bluetooth')
raton2 = Raton('Logitech', 'USB')
computadora2 = Computadora('PC 2', monitor2, teclado2, raton2)

# Creamos un orden
computadoras1 = [computadora,computadora2]
orden1 = Orden(computadoras1)
print(orden1)

# Creamos una nueva computadora
monitor3 = Monitor('Acer', '21.5"')
teclado3 = Teclado('Genius', 'Bluetooth')
raton3 = Raton('HP', 'USB')
computadora3 = Computadora('PC 3', monitor3, teclado3, raton3)

# Agregamos la nueva computadora al primer orden
orden1.agregar_computadora(computadora3)
print(orden1)