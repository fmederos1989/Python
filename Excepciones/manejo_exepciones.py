from NumerosIdenticosExeption import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('Los numeros ingresados son iguales.')
    resultado = a / b

except ZeroDivisionError as e:  #! Exceptions más especificas
    print(f'ZeroDivisionError - Ocurrió un error: {e}, {type(e)}')

except TypeError as e:   #! Exceptions más especificas
    print(f'TypeError - Ocurrió un error: {e}, {type(e)}')

except Exception as e:  #! Exception mas generic
    print(f'Exception - Ocurrió un error: {e}, {type(e)}')

#! Este se ejecuta si no hubo ningún error (opcional)
else:
    print('No hubo ningún error (exception).')
#! Este bloque se ejecuta siempre que se ejecuta el programa (opcional)
finally:
    print('Se ejecuta el bloque finally.')


print(f'Resultado: {resultado}')
print('Continuamos...')