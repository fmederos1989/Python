import sys
import mysql.connector
from mysql.connector import pooling
from mysql.connector import Error


class Conexion:
    """
    Esta clase permite la conexión a una base de datos.
    """
    _DATABASE = 'zona_fit_db'
    _HOST = 'localhost'
    _USER = 'root'
    _PASSWORD = 'admin123'
    _PORT = '3306'
    _POOL_SIZE = 5
    _POOL_NAME = 'zona_fit_pool'
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pooling.MySQLConnectionPool(
                    pool_name=cls._POOL_NAME,
                    pool_size=cls._POOL_SIZE,
                    host=cls._HOST,
                    port=cls._PORT,
                    user=cls._USER,
                    password=cls._PASSWORD,
                    database=cls._DATABASE
                )
                # print(f'Pool de conexiones obtenido correctamente: {cls._pool}')
                # print(f'Nombre del pool: {cls._POOL_NAME}')
                # print(f'Tamaño del pool: {cls._POOL_SIZE}')
                return cls._pool
            except Error as e:
                print(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        return cls.obtenerPool().get_connection()

    @classmethod
    def liberarConexion(cls, connection):
        connection.close()


if __name__ == '__main__':
    #! Creamos el pool de conexion
    # pool = Conexion.obtenerPool()
    # print(pool)

    #! Obtenemos una conexion del pool
    connection1 = Conexion.obtenerConexion()
    print(connection1)
    Conexion.liberarConexion(connection1)