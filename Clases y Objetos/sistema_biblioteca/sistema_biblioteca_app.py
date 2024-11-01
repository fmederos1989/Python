from biblioteca import Biblioteca

print('*** Sistema de Biblioteca ***')

# Iniciamos ua biblioteca
biblioteca_nacional = Biblioteca('Biblioteca Nacional')

# Agregamos libros a la biblioteca
biblioteca_nacional.agregar_libro('El Quijote de la Mancha', 'Miguel de Cervantes', 'Novela')
biblioteca_nacional.agregar_libro('El Quijote de la Mancha 2', 'Miguel de Cervantes', 'Novela')
biblioteca_nacional.agregar_libro('El Perro y el Raton', 'F. Scott Fitzgerald', 'Novela')
biblioteca_nacional.agregar_libro('La Odisea', 'Homero', 'Terror')
biblioteca_nacional.agregar_libro('La Odisea de los Giles', 'Homero', 'Terror')
biblioteca_nacional.agregar_libro('El Hobbit', 'J.R.R. Tolkien', 'Ficcion')
biblioteca_nacional.agregar_libro('El Señor de los Anillos', 'J.R.R. Tolkien', 'Ficcion')

# Busqueda por autor
biblioteca_nacional.buscar_por_autor('Homero')
biblioteca_nacional.buscar_por_autor('Federico')

# Busqueda por genero
biblioteca_nacional.buscar_por_genero('Novela')
biblioteca_nacional.buscar_por_genero('Terror')
biblioteca_nacional.buscar_por_genero('Accion')

# Listamos todos los libros
biblioteca_nacional.listar_todo()