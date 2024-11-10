import mysql.connector

personas_db = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="admin123",
    database="personas_db"
)

cursor = personas_db.cursor()

#! Insertar datos
sentencia_sql = 'INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)'
valores = ('Pedro', 'Lopez', 28)
cursor.execute(sentencia_sql, valores)
personas_db.commit()  #! Guarda los cambios en al BD
personas_db.close()  #! Cierra la connexion a la BD
