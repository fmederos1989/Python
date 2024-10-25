print('*** Imprimir detalles de una persona usando kwargs ***')

# Funcion que acepta arguments variales en forma de llave-valor
def imprimir_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

# Llamamos a la funcion con algunos argumentos
imprimir_persona(Nombre='Ricardo', Apellido='Gonzalez', Edad=32, Profesion='Ingeniero')

# Llamamos a la funcion con argumentos inexistentes
imprimir_persona(Nombre='Ricardo', Apellido='Gonzalez', Edad=32, Profesion='Ingeniero', Experiencia='Desarrollador')

# Llamamos a la funcion sin argumentos
imprimir_persona()