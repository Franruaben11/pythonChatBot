from flask import Blueprint, request, jsonify
import time

from models.redis_client import RedisClient

usuarios_activos = {}
tiempo_maximo = 30 #segundos
db_redis = RedisClient()

ping_user_bp = Blueprint('enviar_ping', __name__)

#Cuando se hace un post a "/api/enviar_ping", se ejecuta cerrar_registro()
@ping_user_bp.route('/api/enviar_ping', methods=['POST'])
def enviar_ping():
    limpiar_usuarios_inactivos()
    data = request.get_json()
    usuario_id = data.get('usuarioId')
    usuarios_activos[usuario_id] = time.time()
    print(usuario_id)
    return jsonify({'respuesta': request.get_json()})


def limpiar_usuarios_inactivos():
    ahora = time.time()
    usuarios_para_eliminar = []

    for usuario_id, ultimo_ping in usuarios_activos.items():
        if ahora - ultimo_ping > tiempo_maximo:
            usuarios_para_eliminar.append(usuario_id)

    for usuario_id in usuarios_para_eliminar:
        del usuarios_activos[usuario_id]
        db_redis.clear_chat(usuario_id)
        print(f"sesion cerrada para usuario {usuario_id} por inactividad.")


