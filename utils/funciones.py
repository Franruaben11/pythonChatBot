from flask import session
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from config import API_KEY
from models import Database

client = OpenAI(api_key=API_KEY)

def comunicacion_agente(input, prompt_aux=""):
    prompt = (
        f"Sos un psicólogo virtual que charla con la persona para ayudarla a desahogarse. "
        f"Usás jerga argentina, empatizás y analizás lo que dice para conocerla mejor. "
        f"Teniendo en cuenta el contexto previo: {prompt_aux}, respondé al siguiente mensaje "
        f"de forma amable, haciendo preguntas que inviten a que la persona se abra y reflexione. "
        f"La persona dice: '{input}'."
    )
    mensajes: list[ChatCompletionMessageParam] = [
        {"role": "user", "content": prompt}
    ]
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensajes
    )
    return respuesta.choices[0].message.content.strip()


def analizar_mensaje_con_ia(input):
    prompt = f"""
    Analizá este mensaje: "{input}".
    Si contiene algo emocional relevante según estos criterios:
    1. Información personal importante (ejemplo: nombre, edad, contexto familiar o laboral).
    2. Emociones intensas (tristeza, ansiedad, enojo, etc).
    3. Soledad o pedido de ayuda.
    4. Cambios en el estado emocional.
    Devolvé un resumen corto: emoción + tema.
    Si no hay nada, devolvé: "NINGUNO"
    """
    mensajes: list[ChatCompletionMessageParam] = [
        {"role": "user", "content": prompt}
    ]
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensajes
    )
    return respuesta.choices[0].message.content.strip()


def resumir_conversacion(user_id, db_redis):
    db_postgre = Database()
    db_postgre.conectar()

    resumen_historico = db_postgre.realizar_select()

    data_conversacion = db_redis.get_all_msg(user_id)

    prompt_resumen = (
        "Eres un psicólogo. Resume la conversación solo si hay datos realmente importantes. "
        "Tienes un máximo de 20 tokens para hacerlo. Si no hay nada relevante, responde 'NADA RELEVANTE'. "
        f"La conversación es: {data_conversacion}"
    )

    resumen_diario = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Actúa como un psicólogo experto en detectar lo relevante."},
            {"role": "user", "content": prompt_resumen}
        ],
        max_tokens=25,
        temperature=0.5,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.3
    )

    prompt_almacenar = (
        "Debes fusionar dos resúmenes: uno diario y otro histórico. "
        "Solo almacena datos muy relevantes, ya que esto será guardado en una base de datos. "
        f"Resumen diario: {resumen_diario.choices[0].message.content}, "
        f"Resumen histórico: {resumen_historico}"
    )

    respuesta_fusion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "Actúa como un psicólogo que filtra y sintetiza información importante para almacenar."},
            {"role": "user", "content": prompt_almacenar}
        ],
        max_tokens=100,  # Lo podés ajustar según cuánto querés que dure el resumen final
        temperature=0.5,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.3
    )

    print(respuesta_fusion.choices[0].message.content)

    db_postgre.cerrar()