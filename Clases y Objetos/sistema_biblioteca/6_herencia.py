class Animal:
    def comer(self):
        print('Como mucha veces al dia')

    def dormir(self):
        print('Duermo durante todo el dia')

class Perro(Animal):
    def hacer_sonido(self):
        print('Guau, guau!')

# Programa principal

print('*** Ejemplo de Herencia en Python ***')
print('\nClase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()
