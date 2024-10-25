# Definicion de una clase

class Persona:
    def inicializar_persona(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        # Mostramos los datos de la persona
        print(f'''Persona -->
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')

if __name__ == '__main__':
    # Creacion de objeto
    persona1 = Persona() # Crea objeto vacio en memoria
    persona1.inicializar_persona('Ricardo', 'Gonzalez')
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona()
    persona2.inicializar_persona('Juan', 'Perez')
    persona2.mostrar_persona()
