from flask import Flask, render_template, request, redirect, url_for, session
from config import FLASK_SECRET_KEY
from riesgo_detectar import *
from models.db import Database
from models.user import Usuario

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
    #Esto hace que cuando alguien vaya a '/', automáticamente lo redirija a la ruta llamada 'login'.
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Este se compila cuando es POST (apreto el boton iniciar sesion)
        db = Database()
        db.conectar()

        nombre = request.form['nombre_usuario']
        clave = request.form['clave_usuario']

        user = Usuario(nombre, clave)
        login_correcto = user.verificar_login(db.cursor)

        db.cerrar()

        if login_correcto:
            session['user_id'] = "id_test"       #Guardo el user_id para poder utilizarlo luego

            return render_template("chat.html")
        else:
            return render_template("login.html", respuesta="Usuario o contraseña incorrecta")
    # este se compila cuando es 'GET' cuando entra por primera vez (no apreta POST)
    return render_template("login.html", respuesta="")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    return render_template("chat.html", respuesta="")


if __name__ == "__main__":
    app.run(debug=True)
