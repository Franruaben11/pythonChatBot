from flask import Flask, render_template, request
from riesgo_detectar import detectar_riesgo_con_gpt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        mensaje = request.form["mensaje"]
        output_riesgo = detectar_riesgo_con_gpt(mensaje)
        respuesta = f"El mensaje tiene riesgo? {output_riesgo}"
        return render_template("chat.html", respuesta=respuesta)
    return render_template("chat.html", respuesta="")

if __name__ == "__main__":
    app.run(debug=True)
