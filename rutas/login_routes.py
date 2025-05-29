from contextlib import nullcontext

from flask import Blueprint, render_template, request, redirect, url_for, session
from models.db import Database

login_bp = Blueprint('auth', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = Database()
        db.conectar()

        nombre = request.form['nombre_usuario']
        clave = request.form['clave_usuario']

        login_correcto = db.verificar_login(nombre,clave)

        db.cerrar()

        if login_correcto:
            session['user_id'] = nombre
            print("b")
            return redirect(url_for('chat.chat_view'))
        else:
            print("a")
            return render_template("login.html", respuesta="Usuario o contraseña incorrecta")
    return render_template("login.html", respuesta="")