from flask import Flask, request, render_template_string
from src.ahorcado import Ahorcado

app = Flask(__name__)

@app.route("/")
def index():
    word = request.args.get("word", "GATO")
    juego = Ahorcado(word)
    
    html = """
    <!DOCTYPE html>
    <html>
    <body>
        <div data-testid="word">{{ enmascarada }}</div>
    </body>
    </html>
    """
    return render_template_string(html, enmascarada=juego.palabra_enmascarada())

if __name__ == "__main__":
    app.run(port=5000)