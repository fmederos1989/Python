from libro import Libro


class Biblioteca:

    def __init__(self, nombre):
        self._libros = []
        self._nombre = nombre

    def agregar_libro(self, titulo, autor, genero):
        libro = Libro(titulo, autor, genero)
        self._libros.append(libro)

    def buscar_por_autor(self, autor):
        libros_encontrados = []
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                libros_encontrados.append(libro)
        if len(libros_encontrados) == 0:
            print(f"\nNo se encontraron libros escritos por {autor}.")
        else:
            print(f"\nLibros escritos por {autor}:")
            for libro in libros_encontrados:
                print(f"- {libro.titulo} - {libro.autor} - {libro.genero}")

    def buscar_por_genero(self, genero):
        libros_encontrados = []
        for libro in self._libros:
            if libro.genero.lower() == genero.lower():
                libros_encontrados.append(libro)
        if len(libros_encontrados) == 0:
            print(f"\nNo se encontraron libros del género {genero}.")
        else:
            print(f"\nLibros del género {genero}:")
            for libro in libros_encontrados:
                print(f"- {libro.titulo} - {libro.autor} - {libro.genero}")

    def listar_todo(self):
        print(f"\nLibros de la biblioteca {self._nombre}:")
        for libro in self.libros:
            print(f"- {libro.titulo} - {libro.autor} - {libro.genero}")
