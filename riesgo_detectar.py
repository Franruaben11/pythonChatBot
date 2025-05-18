from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from config import API_KEY

client = OpenAI(api_key=API_KEY)

def detectar_riesgo_con_gpt(input):
    prompt = (f"¿Este texto muestra señales de riesgo o peligro para la salud mental? Respondé solo 'Sí' o 'No'."
              f" Texto: '{input}'")

    mensajes: list[ChatCompletionMessageParam] = [
        {"role": "user", "content": prompt}
    ]
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensajes
    )
    return respuesta.choices[0].message.content.strip()

def comunicacion_agente(input):
    prompt = (f"Sos un asistente psicologico que debes responder al siguiente mensaje, teniendo en cuenta que tu "
              f"funcion es analizar a la otra persona, utiliza jerga argentina: '{input}'")

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
