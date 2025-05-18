from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from riesgo_detectar import *

app = Flask(__name__)
CORS(app)
@app.route("/", methods=['POST'])
def chat():
    if request.method == "POST":
        data = request.json
        respuesta = comunicacion_agente(data.get('pregunta'))
        return jsonify({'respuesta': respuesta})
    return None


if __name__ == "__main__":
    app.run(port=3000)
