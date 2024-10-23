print('*** Suma con argumentos variables ***')

def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# llamamos la funcion
resultado = sumar(1, 2, 3 , 4, 5,6,7,8,9,10)
print(f'La suma de los numeros es: {resultado}')



