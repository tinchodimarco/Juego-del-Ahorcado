import os
import secrets

from flask import Flask, redirect, render_template, request, session, url_for
from src.ahorcado import Ahorcado

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)


def cargar_juego() -> Ahorcado:
    datos_juego = session.get("juego")
    if datos_juego is None:
        return Ahorcado()

    juego = Ahorcado(datos_juego["palabra"], intentos=datos_juego["intentos"])
    juego.letras_adivinadas = set(datos_juego["letras_adivinadas"])
    juego.letras_incorrectas = set(datos_juego["letras_incorrectas"])
    return juego


def guardar_juego(juego: Ahorcado) -> None:
    session["juego"] = {
        "palabra": juego.palabra_secreta,
        "intentos": juego.intentos,
        "letras_adivinadas": sorted(juego.letras_adivinadas),
        "letras_incorrectas": sorted(juego.letras_incorrectas),
    }

@app.route("/", methods=["GET", "POST"])
def index():
    # A supplied word starts a new game; ordinary requests continue this browser's game.
    palabra_inicial = request.args.get("word")
    if palabra_inicial:
        intentos_iniciales = request.args.get("intentos")
        if intentos_iniciales:
            juego_actual = Ahorcado(palabra_inicial, intentos=int(intentos_iniciales))
        else:
            juego_actual = Ahorcado(palabra_inicial)
    else:
        juego_actual = cargar_juego()

    # POST: adivinar letra
    if request.method == "POST":
        letra_ingresada = request.form.get("letra")
        if letra_ingresada:
            juego_actual.adivinar_letra(letra_ingresada)
        guardar_juego(juego_actual)
        return redirect(url_for('index'))

    # Renderizar vista pasando la palabra enmascarada y los intentos restantes
    guardar_juego(juego_actual)
    palabra_a_mostrar = juego_actual.palabra_enmascarada()
    intentos_a_mostrar = juego_actual.intentos
    letras_erradas = ", ".join(sorted(juego_actual.letras_incorrectas))

    mensaje = ""
    if juego_actual.esta_ganado():
        mensaje = "¡Ganaste!"
    elif juego_actual.esta_perdido():
        mensaje = "¡Perdiste!"

    return render_template(
        "index.html",
        palabra=palabra_a_mostrar,
        intentos=intentos_a_mostrar,
        letras_incorrectas=letras_erradas,
        mensaje=mensaje
    )

@app.route("/reiniciar")
def reiniciar():
    guardar_juego(Ahorcado())
    return redirect(url_for('index'))

@app.route("/reset")
def reset():
    session.clear()
    return "", 200

if __name__ == "__main__":
    app.run(debug=True)
