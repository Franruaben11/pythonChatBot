from flask import Flask, redirect, url_for
from flask_cors import CORS
from config import FLASK_SECRET_KEY
from rutas.chat_routes import chat_bp
from rutas.login_routes import login_bp
from rutas.ping_user import ping_user_bp

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

CORS(app, supports_credentials=True, origins=["http://127.0.0.1:5000"])
@app.route('/', methods=['GET'])
def index():
    #Esto hace que cuando alguien vaya a '/', automáticamente lo redirija a la ruta llamada 'login'.
    return redirect(url_for('auth.login'))

app.register_blueprint(login_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(ping_user_bp)

if __name__ == "__main__":
    app.run(debug=True)

