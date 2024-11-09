import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Jose', 'Pavan', 'jpavan@mail.com', 4),
                ('Leandro', 'Perez', 'leandro@mail.com', 2)
                )
            cursor.executemany(  sentencia, valores)
            # conexion.commit() NO es necesario ya que usamos el bloque WITH
            print('Registro actualizado correctamente.')
            registros_insertados = cursor.rowcount
            print(f'Se actualizaron {registros_insertados} registro(s).')

except Exception as e:
    print(f'Error: {e}')
finally:
    conexion.close()