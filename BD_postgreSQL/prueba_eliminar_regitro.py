import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Proporciona un id para eliminar: ')
            valores = (entrada,)   #! Agregamos el ip_persona como un valor para actualizar un registro
            cursor.execute(sentencia, valores)
            # conexion.commit() NO es necesario ya que usamos el bloque WITH
            print('Registro eliminado correctamente.')
            registros_insertados = cursor.rowcount
            print(f'Se elimino {registros_insertados} registro(s).')

except Exception as e:
    print(f'Error: {e}')
finally:
    conexion.close()