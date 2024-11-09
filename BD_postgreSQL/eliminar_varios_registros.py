import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los ids a eliminar (separados por coma): ')
            valores = (tuple(entrada.split(',')),)   #! Agregamos el ip_persona como un valor para actualizar un registro
            cursor.execute(sentencia, valores)
            # conexion.commit() NO es necesario ya que usamos el bloque WITH
            print('Registros eliminados correctamente.')
            registros_insertados = cursor.rowcount
            print(f'Se eliminaron {registros_insertados} registro(s).')

except Exception as e:
    print(f'Error: {e}')
finally:
    conexion.close()