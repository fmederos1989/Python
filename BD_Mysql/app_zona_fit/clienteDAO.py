from BD_Mysql.app_zona_fit.cliente import Cliente
from pool_conexion import Conexion

class ClienteDao:

    _SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    _INSERTAR = 'INSERT INTO cliente (nombre, apellido, membresia) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def listarClientes(self):
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            cursor.execute(self._SELECCIONAR)
            registros = cursor.fetchall()
            #! Mapeo de clase-tabla cliente
            clientes = []
            for reg in registros:
                cliente = Cliente(reg[0],reg[1],reg[2],reg[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Error al listar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)

    @classmethod
    def agregarCliente(self, cliente):
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(self._INSERTAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al agregar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)

    @classmethod
    def actualizarCliente(self, cliente):
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(self._ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al actualizar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)

    @classmethod
    def eliminarCliente(self, id):
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            cursor.execute(self._ELIMINAR, (id,))
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al eliminar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)

if __name__ == '__main__':
    #! Prueba agregar cliente
    # cliene1 = Cliente(nombre='Joselo', apellido='Perez', membresia=800)
    # cliente_insertado = ClienteDao.agregarCliente(cliene1)
    # print(f'Clientes agregados correctamente: {cliente_insertado}.')

    #! Prueba actualizar cliente
    cliente2 = Cliente(id=3, nombre='Fede', apellido='Mederos', membresia=901)
    cliente_actualizado = ClienteDao.actualizarCliente(cliente2)
    print(f'Clientes actualizados correctamente: {cliente_actualizado}.')

    #! Prueba eliminar cliente
    cliente_eliminado = ClienteDao.eliminarCliente(6)
    print(f'Clientes eliminados correctamente: {cliente_eliminado}.')

    #! Prueba listar clientes
    clientes = ClienteDao.listarClientes()
    for cliente in clientes:
        print(cliente)