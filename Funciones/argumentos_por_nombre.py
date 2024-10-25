print('*** Funcion con argumentos por nombre ***')

def imprimir_persona(nombre, apellido='NO APORTAR', edad='NO APORTAR'):
    print(f'''
    Persona:
        Nombre: {nombre}
        Apellido: {apellido}
        Edad: {edad}''')

# Primero llamamos la funcion pasando los argumentso de manera posicional
imprimir_persona('Ricardo', 'Gonzalez', 32)

# Luego llamamos la funcion pasando los argumentos por nombre
imprimir_persona(apellido='Gonzalez', edad=32, nombre='Ricardo')

# Llamar la funcion con argumentos por default
imprimir_persona(nombre='Juan', apellido='Gonzalez',)




