import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1', port='5432',database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # # llaves_primarias = ((1, 2, 3),)
            entrada = input('Proporciona los id a buscar (separado pos comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)  #! Tuples de tuples
            # # id_persona = input('Proporciona el id que buscas: ')
            # sentencia = "UPDATE persona SET nombre = 'Juan' WHERE id_persona = 2"
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()  #! Recupera todos los registros
            # registros = cursor.fetchone() #! Recupera apenas uno de los registros
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Error: {e}')
finally:
    conexion.close()

