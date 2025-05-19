import psycopg2
from config import CONNECT_DB

class Database:
    def __init__(self):
        self.conexion = None
        self.cursor = None

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
        self.cursor.execute("SELECT * FROM usuario")
        resultados = self.cursor.fetchall()
        for fila in resultados:
            print(fila)
"""
db = Database()
db.conectar()

db.realizar_select()

db.cerrar()
"""