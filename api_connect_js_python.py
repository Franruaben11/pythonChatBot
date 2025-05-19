from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from riesgo_detectar import *
from models.redis_client import RedisClient

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://127.0.0.1:5000"])
@app.route("/", methods=['POST'])
def chat():
    db_redis = RedisClient()
    if request.method == "POST":
        data = request.json
        respuesta = comunicacion_agente(data.get('pregunta'))

        user_id = session.get('user_id')

        #db_redis.save_user_message(user_id, data.get('pregunta'))
        #db_redis.save_ai_message(user_id, respuesta)
        print(respuesta)
        print(data.get('pregunta'))
        print(user_id)
        print("ppppp")

        return jsonify({'respuesta': respuesta})
    return None


if __name__ == "__main__":
    app.run(port=3000)
