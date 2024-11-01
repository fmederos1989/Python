class Personas:
    # Atributo clase
    contador_personas = 0

    def __init__(self, nombre, apellido):

        # Incrementamos el valor del atributo de clase
        Personas.contador_personas += 1
        self.id = Personas.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre} {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print('** Metodo Estático **')
        return Personas.contador_personas

    @classmethod # Esta es la mejor manera para trabajar los metodos de clase
    def get_contador_personas_clase(cls):
        print('** Metodo Clase **')
        return cls.contador_personas

if __name__ == '__main__':
    print(' *** Ejemplo Contador de Objetos de tipo persona ***')
    persona1 = Personas('Jose', 'Rodriguez')
    persona1.mostrar_persona()

    persona2 = Personas('Maria', 'Garcia')
    persona2.mostrar_persona()

    # imprimimos el valor del atributo de clase
    print(f'Cantidad de personas: {Personas.contador_personas}')
    print(f'Contador de objetos personas desde el metodo estatico: {Personas.get_contador_personas_estatico()}')
    print(f'Contador de objetos personas desde el metodo clase: {Personas.get_contador_personas_clase()}')
    print(f'Contador desde un persona1: {persona1.contador_personas}')