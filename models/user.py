import bcrypt

class Usuario():
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

    def verificar_login(self, cursor):
        cursor.execute("SELECT contraseña FROM usuario WHERE nombre_usuario = %s", (self.nombre_usuario,))
        resultado = cursor.fetchone()
        if resultado:
            hashed_password = resultado[0]
            #comparamos el hash de la contraseña cargada con el hash de la que tenemos en la base de datos
            return bcrypt.checkpw(self.contraseña.encode(), hashed_password.encode())
        return False
