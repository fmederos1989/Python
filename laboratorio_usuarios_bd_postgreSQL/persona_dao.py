from Conexion import Conexion
from Persona import Persona
from logger_base import log
from cursor_del_pool import CursorDelPool


class PersonaDAO:
    '''
    DAO significa (Data Access Object)
    CRUD (Create - Read - Update - Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY persona'
    _INSERTAR = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Se seleccionan todas las personas')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for reg in registros:
                persona = Persona(reg[0], reg[1], reg[2], reg[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug((f'Persona insertada: {persona}'))
            return cursor.rowcount


    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug((f'Persona actualizada: {persona}'))
            return cursor.rowcount


    @classmethod
    def eliminar(cls, id_persona):
        with CursorDelPool() as cursor:
            valores = (id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug((f'Persona eliminada con id: {id_persona}'))
            return cursor.rowcount


if __name__ == "__main__":

    #! Prueba de insertar
    persona1 = Persona(nombre='Guillermo', apellido='Mederos', email='guille@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Persona insertada: {personas_insertadas}')

    #! Prueba de actualizar
    persona1 = Persona(id_persona=10, nombre='Mariela', apellido='Pavan', email='mariela@mail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')

    #! Prueba de eliminar
    persona_eliminada = PersonaDAO.eliminar(12)
    log.debug(f'Cantidad de personas eliminadadas: {persona_eliminada}')

    #! Prueba de seleccionar
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
