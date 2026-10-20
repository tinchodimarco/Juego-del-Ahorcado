from flask import Flask, request, render_template
from src.ahorcado import Ahorcado

app = Flask(__name__)
juego_actual = None 

@app.route("/", methods=["GET", "POST"])
def index():
    global juego_actual

    # GET: inicio de partida
    palabra_inicial = request.args.get("word")
    if palabra_inicial:
        juego_actual = Ahorcado(palabra_inicial)

    # POST: adivinar letra
    if request.method == "POST" and juego_actual:
        letra_ingresada = request.form.get("letra")
        if letra_ingresada:
            juego_actual.adivinar_letra(letra_ingresada.upper())

    # Renderizar vista pasando la palabra enmascarada y los intentos restantes
    palabra_a_mostrar = juego_actual.palabra_enmascarada() if juego_actual else ""
    intentos_a_mostrar = juego_actual.intentos if juego_actual else 6

    return render_template("index.html", palabra=palabra_a_mostrar, intentos=intentos_a_mostrar)

if __name__ == "__main__":
    app.run(debug=True)