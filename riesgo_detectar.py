from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

client = OpenAI(api_key="x")

def detectar_riesgo_con_gpt(input):
    prompt = f"¿Este texto muestra señales de riesgo o peligro para la salud mental? Respondé solo 'Sí' o 'No'. Texto: '{input}'"

    mensajes: list[ChatCompletionMessageParam] = [
        {"role": "user", "content": prompt}
    ]

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensajes
    )

    return respuesta.choices[0].message.content.strip()


