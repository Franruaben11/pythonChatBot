from flask import Flask, render_template, request
from riesgo_detectar import *

app = Flask(__name__)
@app.route('/')
def index():
    log=False
    if(log):
        return render_template("chat.html", respuesta="")
    else:
        return render_template("login.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    return render_template("chat.html", respuesta="")

if __name__ == "__main__":
    app.run(debug=True)
