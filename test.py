import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root", passwd="karla", database="amazon")

cur = cnn.cursor()
cur.execute("SELECT * FROM usuario")
datos = cur.fetchall()

for fila in datos:
    print(fila)
#print(cnn)