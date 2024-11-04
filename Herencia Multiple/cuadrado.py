from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

# Prueba de la clase

if __name__ == '__main__':
    cuadrado1 = Cuadrado(5, 'rojo')
    print(cuadrado1)
    print(f'Area: {cuadrado1.calcular_area()} cm²')