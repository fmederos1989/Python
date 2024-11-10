import mysql.connector

personas_db = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="admin123",
    database="personas_db"
)

mi_cursor = personas_db.cursor()
mi_cursor.execute('SELECT * FROM personas')
resultado = mi_cursor.fetchall()
for persona in resultado:
    print(persona)

personas_db.close()