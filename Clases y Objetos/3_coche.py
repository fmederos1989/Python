# Definimos la clase coche

class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido

    def conducir(self):
        print(f'''Conduciendo el coche:\nMarca: {self._marca}\nModelo: {self._modelo}\nColor: {self._color}''')

    # def get_marca(self):
    #     return self._marca

    @property # Otra forma de definir el metodo get
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def model(self):
        return self._modelo

    @model.setter
    def model(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Programa principal
if __name__ == '__main__':
    # Creamos el primer coche
    coche1 = Coche('Toyota', 'Corolla', 'Rojo')
    coche1.conducir()
    # No debemos acceder a los atributos que no sean publicos
    coche1.marca = 'Ford'
    coche1.modelo = 'Mustang'
    coche1.color= 'Azul'
    coche1.conducir()
    print(f'Atributo marca coche1: {coche1.marca}')
    coche1.marca = 'Toyota'
    print(f'Atributo marca coche1 despues de cambiarlo: {coche1.marca}')

    # intentamos agregar un atributo a este objeto
    setattr(coche1, 'nuevo_atributo', 'valor nuevo atributo')
    coche1.nuevo_atributo2 = ' Valor nuevo atributo 2' # Otra opcion de agregar atributos a un objeto
    coche1.conducir()
    print(coche1.nuevo_atributo)
    print(f'Atributos del coche:{coche1.__dict__}') # Muestra todos los atributos de un objeto

    # Creamos el segundo coche
    coche2 = Coche('Honda', 'Civic', 'Negro')
    coche2.conducir()
