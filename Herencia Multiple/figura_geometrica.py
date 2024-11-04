# ABC Abstract Base Class
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print('Valor erroneo en el ancho.')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print('Valor erroneo en el alto.')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
            print('Valor cambiado correctamente en el ancho.')
        else:
            self._ancho = 0
            print('Valor erroneo en el ancho.')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
            print('Valor cambiado correctamente en el alto.')
        else:
            self._alto = 0
            print('Valor erroneo en el alto.')

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'Figura Geometrica: Ancho={self.ancho} Alto={self.alto}'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False