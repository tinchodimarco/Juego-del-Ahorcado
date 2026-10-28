from flask import Flask, request, render_template, url_for, redirect
from src.ahorcado import Ahorcado

app = Flask(__name__)
juego_actual = None 

@app.route("/", methods=["GET", "POST"])
def index():
    global juego_actual

    # 1. Si la URL trae un parámetro "word", tiene prioridad (para que pasen los tests de GATO, SOL, etc.)
    palabra_inicial = request.args.get("word")
    if palabra_inicial:
        intentos_iniciales = request.args.get("intentos")
        if intentos_iniciales:
            juego_actual = Ahorcado(palabra_inicial, intentos=int(intentos_iniciales))
        else:
            juego_actual = Ahorcado(palabra_inicial)
    
    # 2. Si NO trae "word" y todavía no hay partida, recién ahí creamos una aleatoria (para la HU-09)
    elif juego_actual is None:
        juego_actual = Ahorcado()

    # POST: adivinar letra
    if request.method == "POST":
        letra_ingresada = request.form.get("letra")
        if letra_ingresada and juego_actual:
            juego_actual.adivinar_letra(letra_ingresada.upper())
        return redirect(url_for('index'))

    # ... resto de la renderización ...

    # Renderizar vista con el estado actual
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
        mensaje=mensaje
    )

# Opcional: asegurate de registrar la ruta si usás el botón de reiniciar
@app.route("/reiniciar")
def reiniciar():
    global juego_actual
    juego_actual = Ahorcado()  # Genera una nueva palabra aleatoria al reiniciar
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)