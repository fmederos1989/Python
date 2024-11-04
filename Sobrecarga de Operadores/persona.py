class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad

# obj1 + obj2
# obj1.__add__(obj2)

obj1 = Persona('Ana', 45)
obj2 = Persona('Juan', 40)

print(obj1 + obj2)
print(obj1 - obj2)