from cuadrado import Cuadrado
from rectangulo import Rectangulo

cuadrado1 = Cuadrado(lado=8, color='rojo')
print('Cuadrado 1')
print(cuadrado1)
print(f'Area: {cuadrado1.calcular_area()} cm²')

rectangulo1 = Rectangulo(ancho=5, alto=7, color='azul')
print('\nRectangulo 1')
print(rectangulo1)
print(f'Area: {rectangulo1.calcular_area()} cm²')

rectangulo1.alto = -1
rectangulo1.alto = 6
print('Rectangulo 1 despues de cambiar el alto')
print(rectangulo1)
print(f'Area: {rectangulo1.calcular_area()} cm²')