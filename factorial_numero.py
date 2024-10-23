print('*** Factorial de numero 5 ***')

# Definimos la funcion
def factorial_recursiva(numero):
    # Caso base
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial: {numero} es: 1')
        return 1
    else: # Caso recursivo
        factorial_parcial = numero * factorial_recursiva(numero-1)
        print(f'Resultado factorial parcial: {numero} es: {factorial_parcial}')
        return factorial_parcial

# Llamamos a la funcion
factorial_recursiva(5)


