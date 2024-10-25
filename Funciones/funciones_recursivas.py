print('*** Funciones Recursivas - Imprimir de 1 a 5 ***')

# Definimos la funcion
def funcion_recursiva(numero):
    # Caso base
    if numero == 1:
        print(numero, end=' ')
    else: # Caso recursivo
        funcion_recursiva(numero - 1)
        # Impresion del numero
        print(numero, end=' ')


# Llamamos a la funcion
funcion_recursiva(5)


