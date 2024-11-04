# POlimorfismo
class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Guau, guau!')

class Gato(Animal):
    def hacer_sonido(self):
        print('Miau, miau!')

# Function Polimórfica
def hacer_sonido_animal(animal):
    animal.hacer_sonido()

# Programa principal
print(' *** Ejemplo Polimorfismo ***')
print('Clase de Padre Animal: ')

animal1 = Animal()
#animal1.hacer_sonido()
hacer_sonido_animal(animal1)

print('\nClase hija Perro:')
perro1 = Perro()
perro1.hacer_sonido()  # Polimorfismo
hacer_sonido_animal(perro1)

print('\nClase hija Gato:')
gato1 = Gato()
gato1.hacer_sonido()  # Polimorfismo
hacer_sonido_animal(gato1)