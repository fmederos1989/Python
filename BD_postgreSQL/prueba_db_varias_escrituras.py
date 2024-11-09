import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = (
                ('Jose', 'Fernandez', 'jose@mail.com'),
                ('Jorge', 'Perez', 'jorge@mail.com'),
                ('Alberto', 'Gonzalez', 'alberto@mail.com')
            )
            cursor.executemany(sentencia, valores) #! Cambiamos el metodo para enviar mas de una tupla de valores
            # conexion.commit() NO es necesario ya que usamos el bloque WITH
            print('Registro agregado correctamente.')
            registros_insertados = cursor.rowcount
            print(f'Se insertaron {registros_insertados} registro(s).')

except Exception as e:
    print(f'Error: {e}')
finally:
    conexion.close()