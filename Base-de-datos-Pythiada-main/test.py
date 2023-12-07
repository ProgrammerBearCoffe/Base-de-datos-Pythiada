import mysql.connector

class test:
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", passwd="karla", database="amazon")
    
    def __str__(self):
        datos=self.usuarios_panolis()
        aux=""
        for row in datos:
            aux=aux + str(row)+"\n"
        return aux

    def usuarios_panolis(self):
       cur = self.cnn.cursor()
       cur.execute("SELECT * FROM usuario")
       datos = cur.fetchall()
       cur.close()
       return datos
    
    def insertar_panolis(self,nombre, email, telefono, sexo, fecha_nacimiento, contrasena, subtotal, cantidad_productos):
        cur = self.cnn.cursor()
        sql = "INSERT INTO `usuario` (`nombre`, `email`, `telefono`, `sexo`, `fecha_nacimiento`, `contrasena`, `subtotal`, `cantidad_productos`) VALUES('{}', '{}', '{}', '{}', '{}', '{}', {}, {});".format(
        nombre, email, telefono, sexo, fecha_nacimiento, contrasena, subtotal, cantidad_productos)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    

    print(insertar_panolis('Luisa Martínez', 'luisa@example.com', '1239876543', 'F', '1992-07-18', 'pass123', 160.75, 5))

#datos=usuarios_panolis()
#for fila in datos:
 #   print(fila)
#print(cnn)