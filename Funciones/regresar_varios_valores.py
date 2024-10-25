print('*** Regresar una tupla de valores desde una funcion ***')

# Definicion de la funcion
def personas_mayusculas(nombre, apellido, edad):
    print(f'Esta funcion regresa varios valores (tupla)')
    return (nombre.upper(), apellido.upper(), edad)

# Programa principal
nombre, apellido, edad = personas_mayusculas('Sandra', 'Jimenez', 30)
print(f'Resultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')