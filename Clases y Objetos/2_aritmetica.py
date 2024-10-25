class Aritmetica:
    def __init__(self, num1=None, num2=None):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        resultado = self.num1 + self.num2
        print(f'La suma de {self.num1} + {self.num2} = {resultado}')

    def restar(self):
        resultado = self.num1 - self.num2
        print(f'La resta de {self.num1} - {self.num2} = {resultado}')

    def multiplicar(self):
        resultado = self.num1 * self.num2
        print(f'La multiplicacion de {self.num1} * {self.num2} = {resultado}')

    def dividir(self):
        if self.num2 != 0:
            resultado = self.num1 / self.num2
            print(f'La division de {self.num1} / {self.num2} = {resultado}')

if __name__ == '__main__':
    #! Iniciamos la instancia 1
    print('--- Primera instancia ---\n')
    aritmetica1 = Aritmetica(2, 3)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
    #! Iniciamos la instancia 2
    print('\n--- Segunda instancia ---\n')
    aritmetica2 = Aritmetica(10, 3)
    aritmetica2.sumar()
    aritmetica2.restar()
    aritmetica2.multiplicar()
    aritmetica2.dividir()
    #! Iniciamos la instancia 3
    print('\n--- Tercera instancia ---\n')
    aritmetica3 = Aritmetica() # No pasamos valores y los declaramos luego
    aritmetica3.num1 = 5
    aritmetica3.num2 = 10
    aritmetica3.sumar()
    aritmetica3.restar()
    aritmetica3.multiplicar()
    aritmetica3.dividir()
