print('*** Argumentos variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'\nSuperheroe: {superheroe}')
    print(f'Nombre: {nombre}')
    print(f'{args}')
    # iteramos los superpoderes
    for superpoder in args:
        print(f'- Superpoder: {superpoder}')

# LLamamos la funcion
superheroe_superpoderes('Superman', 'Clark Kent')
superheroe_superpoderes('Batman', 'Tony Stark', 'Dinamita', 'Velocidad', 'Super inteligencia')
superheroe_superpoderes('Wonder Woman', 'Diana Prince', 'Agilidad', 'Fuerza', 'Velocidad')
superheroe_superpoderes('Hulk', 'Bruce Banner', 'Resistencia', 'Fuerza', 'Super inteligencia')
superheroe_superpoderes('Iron Man', 'Tony Stark', 'Invencibilidad', 'Super fuerza', 'Velocidad', 'Resistencia')