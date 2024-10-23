# *args - argumentos - tupla
# **kwargs - keyword arguments - dict

print('*** Argumentos kwargs')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - Superpoderes: {args} - Mas info: {kwargs}')

# llamamos a la funcion
superheroe_superpoderes('Superman', 'Dinamita', 'Velocidad', edad=17, empresa='Marvel')
superheroe_superpoderes('Ironman', 'Dinamita', 'Armadura', edad=45)

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi Vecino', personalidad='buena onda')