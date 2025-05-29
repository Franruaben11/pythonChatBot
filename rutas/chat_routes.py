from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for
from utils.funciones import comunicacion_agente
from models.redis_client import RedisClient

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/api/chat', methods=['POST'])
def chat():
    user_id = session.get('user_id')
    data = request.json
    pregunta = data.get('pregunta')
    db_redis = RedisClient()
    db_redis.save_user_message(user_id, pregunta)

    respuesta = comunicacion_agente(pregunta, db_redis.get_last_12_msg(user_id))

    db_redis.save_ai_message(user_id, respuesta)

    return jsonify({'respuesta': respuesta})

@chat_bp.route('/chat', methods=['GET'])
def chat_view():
    if session.get("user_id") is not None:
        return render_template("chat.html")
    else:
        return redirect(url_for("auth.login"))

