#import modulo_funcion_sumar
from modulo_funcion_sumar import sumar
print('*** Funcion sumar ***')

#def sumar(a, b):
#    resultado_suma = a + b
#    return resultado_suma

#resultado_funcion = modulo_funcion_sumar.sumar(5,8)
resultado_funcion = sumar(5,8)
print(f'La suma de 5 y 8 es: {resultado_funcion}')
print(__name__)

#resultado_funcion = sumar(10,9)
#print(f'La suma de 10 y 9 es: {resultado_funcion}')