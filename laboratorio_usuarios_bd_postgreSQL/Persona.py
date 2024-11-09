from logger_base import log

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_person = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
        ID: {self._id_person} Nombre: {self._nombre}
        Apellido: {self._apellido} Email: {self._email}
        '''

    @property
    def id_persona(self):
        return self._id_person

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_person = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

if __name__ == '__main__':
    persona1 = Persona(1, 'John', 'Doe', 'johndoe@example.com')
    log.debug(persona1)
    #! Simular un INSERT INTO
    persona1 = Persona(nombre='Fede', apellido='Mederos', email='fede@mal.com')
    log.debug(persona1)
    #! Simular un DELETE
    persona1 = Persona(id_persona=1)
    log.debug(persona1)
