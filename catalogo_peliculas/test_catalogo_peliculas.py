from service.catalogo_peliculas import CatalogoPeliculas as cp
from dominio.Pelicula import Pelicula

print(' Sistema de catalogo de Peliculas '.center(50, '-'))

opcion = None

while True:
    try:
        print('\nMenú principal:')
        print('1. Agregar pelicula')
        print('2. Listar peliculas')
        print('3. Eliminar pelicula')
        print('4. Salir')
        opcion = int(input('Ingrese una opcion: '))
    except Exception as e:
        print('Error:', e)
        opcion = None

    if opcion == 1:
        nombre_pelicula = input('Ingrese el nombre de la pelicula: ')
        pelicula = Pelicula(nombre_pelicula)
        cp.agregar_pelicula(pelicula)

    elif opcion == 2:
        cp.listar_peliculas()

    elif opcion == 3:
        cp.eliminar_pelicula()

    elif opcion == 4:
        print('Saliendo del sistema...')
        break
    else:
        print('Opción inválida.')
