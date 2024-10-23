print('*** Obtener coordenadas X, Y, Z ***')

# definimos funcion
def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z


# llamamos a la funcion y guardamos sus resultados
resultado = obtener_coordenadas()
print(resultado)

# Unpacking de la tupla
x1, y1, z1 = resultado

# imprimimos los resultados
print(f'X: {x1}, Y: {y1}, Z: {z1}')

