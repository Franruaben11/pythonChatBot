from contextlib import nullcontext

from flask import Blueprint, render_template, request, redirect, url_for, session
from models.db import Database
from models.user import Usuario

login_bp = Blueprint('auth', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = Database()
        db.conectar()

        nombre = request.form['nombre_usuario']
        clave = request.form['clave_usuario']

        user = Usuario(nombre, clave)
        login_correcto = user.verificar_login(db.cursor)

        db.cerrar()

        if login_correcto:
            session['user_id'] = nombre
            return render_template('chat.html', user_id = session['user_id'])

        else:
            return render_template("login.html", respuesta="Usuario o contraseña incorrecta")
    return render_template("login.html", respuesta="")