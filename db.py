import psycopg2
from config import CONNECT_DB

try:
    # Conexión a la base de datos psicobot
    # ** desempaqueta los datos
    conexion = psycopg2.connect(**CONNECT_DB)

    cursor = conexion.cursor()

    # Ejemplo: leer todos los mensajes
    cursor.execute("SELECT * FROM mensajes;")
    filas = cursor.fetchall()

    for fila in filas:
        print(fila)

except Exception as e:
    print("Error al conectar o consultar:", e)

finally:
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()