#! Definicion de una clase

class Persona:
    #! Constructor de la clase
    def __init__(self, nombre, apellido):
        # Inicializamos los atributos de la clase en el constructor
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        # Mostramos los datos de la persona
        print(f'''Persona -->
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'Dir. mem de self: {id(self)}')
        print(f'Dir. mem hex self: {hex(id(self))}')

if __name__ == '__main__':
    # Creacion de objeto
    persona1 = Persona('Federico', 'Mederos') # Crea objeto vacio en memoria
    persona1.mostrar_persona()


    # Creamos un segundo objeto
    persona2 = Persona('Juan', 'Perez')
    persona2.mostrar_persona()
