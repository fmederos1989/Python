import mysql.connector

personas_db = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="admin123",
    database="personas_db"
)

cursor = personas_db.cursor()

#! Actualizar datos de una persona
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Fede', 'Mederos', 35, 1)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha modificado la información')
personas_db.close()
