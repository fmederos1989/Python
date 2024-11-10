import mysql.connector

personas_db = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="admin123",
    database="personas_db"
)

cursor = personas_db.cursor()

#! Eliminando un registro en la DB

sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valores = (4, )  #! Agregamos el id como un valor para actualizar un registro
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha eliminado el registro')
personas_db.close()