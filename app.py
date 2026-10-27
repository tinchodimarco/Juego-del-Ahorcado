from flask import Flask, request, render_template, url_for, redirect
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
    letras_erradas = ", ".join(sorted(juego_actual.letras_incorrectas)) if juego_actual else ""

    mensaje = ""
    if juego_actual and juego_actual.esta_ganado():
        mensaje = "¡Ganaste!"
    elif juego_actual and juego_actual.esta_perdido():
     mensaje = "¡Perdiste!"

    return render_template(
        "index.html",
        palabra=palabra_a_mostrar,
        intentos=intentos_a_mostrar,
        letras_incorrectas=letras_erradas,
        mensaje = mensaje
        )

def reiniciar():
    global juego_actual
    # Si querés que elijo otra palabra o reinicie con la misma/nueva:
    if juego_actual:
        # Podés conservar la misma palabra secreta o generar una nueva
        palabra = juego_actual.palabra_secreta
        juego_actual = Ahorcado(palabra)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)    