class Aritmetica:
    def __init__(self, num1=None, num2=None):
        self._num1 = num1
        self._num2 = num2

    @property
    def num1(self):
        return self._num1

    @num1.setter
    def num1(self, num1):
        self._num1 = num1

    @property
    def num2(self):
        return self._num2

    @num2.setter
    def num2(self, num2):
        self._num2 = num2

    def sumar(self):
        resultado = self._num1 + self._num2
        print(f'La suma de {self._num1} + {self._num2} = {resultado}')

    def restar(self):
        resultado = self._num1 - self._num2
        print(f'La resta de {self._num1} - {self._num2} = {resultado}')

    def multiplicar(self):
        resultado = self._num1 * self._num2
        print(f'La multiplicacion de {self._num1} * {self._num2} = {resultado}')

    def dividir(self):
        if self._num2 != 0:
            resultado = self._num1 / self._num2
            print(f'La division de {self._num1} / {self._num2} = {resultado}')

if __name__ == '__main__':
    #! Iniciamos la instancia 1
    print('--- Primera instancia ---\n')
    aritmetica1 = Aritmetica(2, 3)
    print(f'Valor del num1: {aritmetica1.num1}, valor del num2: {aritmetica1.num2}')
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
    #! Iniciamos la instancia 2
    print('\n--- Segunda instancia ---\n')
    aritmetica2 = Aritmetica(10, 3)
    print(f'Valor del num1: {aritmetica2.num1}, valor del num2: {aritmetica2.num2}')
    aritmetica2.sumar()
    aritmetica2.restar()
    aritmetica2._num1 = 20
    print(f'Valor del num1: {aritmetica2.num1}, valor del num2: {aritmetica2.num2}')
    aritmetica2.sumar()
    #! Iniciamos la instancia 3
    print('\n--- Tercera instancia ---\n')
    aritmetica3 = Aritmetica() # No pasamos valores y los declaramos luego
    aritmetica3._num1 = 5
    aritmetica3._num2 = 10
    print(f'Valor del num1: {aritmetica3.num1}, valor del num2: {aritmetica3.num2}')
    aritmetica3.sumar()
    aritmetica3.restar()
    aritmetica3.multiplicar()
    aritmetica3.dividir()
