import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root", passwd="karla", database="amazon")

#def usuarios_panolis():
 #   cur = cnn.cursor()
  #  cur.execute("SELECT * FROM usuario")
   # datos = cur.fetchall()
   # cur.close()
   # cnn.close()
    #return datos

def insertar_panolis(nombre, email, telefono, sexo, fecha_nacimiento, contrasena, subtotal, cantidad_productos):
    cur = cnn.cursor()
    sql = "INSERT INTO `usuario` (`nombre`, `email`, `telefono`, `sexo`, `fecha_nacimiento`, `contrasena`, `subtotal`, `cantidad_productos`) VALUES('{}', '{}', '{}', '{}', '{}', '{}', {}, {});".format(
        nombre, email, telefono, sexo, fecha_nacimiento, contrasena, subtotal, cantidad_productos)
    cur.execute(sql)
    n = cur.rowcount
    cnn.commit()
    cur.close()
    return n

print(insertar_panolis('Luisa Martínez', 'luisa@example.com', '1239876543', 'F', '1992-07-18', 'pass123', 160.75, 5))

#datos=usuarios_panolis()
#for fila in datos:
 #   print(fila)
#print(cnn)
