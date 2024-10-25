print('*** Calculado Potencias ***')

#definimos la funcion
def calular_potencias(base, potencia):
    if potencia == 0:
        return 1
    else:
        parcial = base * calular_potencias(base, potencia - 1)
        return parcial

# llamamos a la funcion
base = 6
potencia = 4

print(f'El resultado de {base} elevado a la potencia {potencia} es: {calular_potencias(base, potencia)}')