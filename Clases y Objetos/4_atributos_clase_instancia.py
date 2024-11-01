class Persona:

    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

# Programa principal

if __name__ == '__main__':
    print(f'*** Atributos de clase ***')
    print(f'Nombre de la clase: {Persona.atributo_clase}')
    # Modificamos el atributo de la clase
    Persona.atributo_clase = 10
    print(f'Nuevo valor del atributo de la clase: {Persona.atributo_clase}\n')

    # Cremaos un primero objeto
    persona1 = Persona(15)
    print(f'Atributos de instancia 1: {persona1.atributo_clase}')
    print(f'Valor del atributo de instancia 1: {persona1.atributo_instancia}')

    # Creamos un segundo objeto
    persona2 = Persona(25)
    print(f'Atributos de instancia 2: {persona2.atributo_clase}')
    print(f'Valor del atributo de instancia 2: {persona2.atributo_instancia}')