import bcrypt
import psycopg2
from config import CONNECT_DB

class Database:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = psycopg2.connect(**CONNECT_DB)
            self.cursor = self.conexion.cursor()
        except (Exception, psycopg2.Error) as error:
            print("Error al conectar: ", error)

    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()

    def realizar_select(self):
        self.cursor.execute("SELECT * FROM interacciones")
        resultados = self.cursor.fetchall()
        for fila in resultados:
            print(fila)

    def registrar_usuario(self, nombre_usuario, contraseña):
        hashed = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt()).decode()
        self.cursor.execute(
            "INSERT INTO usuario (nombre_usuario, contraseña) VALUES (%s, %s)",
            (nombre_usuario, hashed)
        )
        self.conexion.commit()

    def verificar_login(self, nombre_usuario, contraseña):
        self.cursor.execute(
            "SELECT contraseña FROM usuario WHERE nombre_usuario = %s",
            (nombre_usuario,)
        )
        resultado = self.cursor.fetchone()
        if resultado:
            hashed_password = resultado[0]
            return bcrypt.checkpw(contraseña.encode(), hashed_password.encode())
        return False

    def obtener_usuarios(self):
        self.cursor.execute("SELECT nombre_usuario FROM usuario")
        usuarios = self.cursor.fetchall()
        return [u[0] for u in usuarios]  # devuelve una lista con los nombres

