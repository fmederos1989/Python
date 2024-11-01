class Libro:
    cantidad_libros = 0

    def __init__(self, titulo, autor, genero):
        Libro.cantidad_libros += 1
        self._id = Libro.cantidad_libros
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def genero(self):
        return self._genero

    @classmethod
    def get_cantidad_libros(cls):
        return cls.cantidad_libros
