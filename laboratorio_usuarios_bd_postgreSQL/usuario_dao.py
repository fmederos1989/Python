from usuario import Usuario
from logger_base import log
from cursor_del_pool import CursorDelPool

class UsuarioDAO:
    '''
    DAO significa (Data Access Object)
    CRUD (Create - Read - Update - Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuarios (username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuarios SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Se seleccionan todos los usuarios')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for reg in registros:
                usuario = Usuario(reg[0], reg[1], reg[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug('Se inserta un nuevo usuario')
            cursor.execute(cls._INSERTAR, (usuario.username, usuario.password))
            log.debug(f'Usuario creado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug('Se actualiza un usuario existente')
            cursor.execute(cls._ACTUALIZAR, (usuario.username, usuario.password, usuario.id_usuario))
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, id_usuario):
        with CursorDelPool() as cursor:
            log.debug('Se elimina un usuario')
            cursor.execute(cls._ELIMINAR, (id_usuario,))
            log.debug(f'Usuario eliminado con id: {id_usuario}')
            return cursor.rowcount
