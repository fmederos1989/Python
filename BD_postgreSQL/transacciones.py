import psycopg2 as bd

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ('Alex', 'Fernandez', 'alex@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
            valores = ('Eduardo', 'Mederos', 'eduardo@mail.com', 11)
            cursor.execute(sentencia, valores)

except Exception as e:
    print('Hubo un error durante la transaccion, se hizo un rollback')
    print(f'Error: {e}')

finally:
    conexion.close()

print('Termina la transaccion, se hizo commit.')
