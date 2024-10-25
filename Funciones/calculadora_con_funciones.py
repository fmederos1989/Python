print('*** Calculadora con Funciones ***')

# Definimos las funciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print('No es posible dividir sobre 0.')
        return 0

if __name__ == '__main__':
    while True:
        print('\n--- Menu ---')
        print('1. Sumar')
        print('2. Restar')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Salir')

        opcion = int(input('Elija una opcion: '))
        num1 = float(input('Ingrese el primer numero: '))
        num2 = float(input('Ingrese el segundo numero: '))

        if opcion == 1:
            print(f'La suma de {num1} + {num2} es: {sumar(num1, num2)}')
        elif opcion == 2:
            print(f'La resta de {num1} - {num2} es: {restar(num1, num2)}')
        elif opcion == 3:
            print(f'La multiplicacion de {num1} * {num2} es: {multiplicar(num1, num2)}')
        elif opcion == 4:
            print(f'La division de {num1} / {num2} es: {dividir(num1, num2)}')
        elif opcion == 5:
            print('Saliendo del programa...')
            break
        else:
            print('Opcion invalida.')