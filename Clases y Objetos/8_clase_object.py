class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Sobrescribimos el método str
    def __str__(self):
        return f'Persona: {self.nombre} {self.apellido} // Dir. mem.:{super.__str__(self)}'

# Codigo Principa

persona1 = Persona('Ana', 'Martinez')
print(persona1) # Este metodo __str__ se llama automaticamendes desde print
