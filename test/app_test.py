from app import app


def test_cada_cliente_conserva_su_propia_partida():
    primer_cliente = app.test_client()
    segundo_cliente = app.test_client()

    primer_cliente.get("/?word=GATO")
    segundo_cliente.get("/?word=SOL")
    primer_cliente.post("/", data={"letra": "A"})

    primera_partida = primer_cliente.get("/").get_data(as_text=True)
    segunda_partida = segundo_cliente.get("/").get_data(as_text=True)

    assert '<h1 data-testid="word">_ A _ _</h1>' in primera_partida
    assert '<h1 data-testid="word">_ _ _</h1>' in segunda_partida


def test_repetir_letra_incorrecta_no_descuenta_otro_intento():
    cliente = app.test_client()
    cliente.get("/?word=GATO")

    cliente.post("/", data={"letra": "Z"})
    cliente.post("/", data={"letra": "z"})
    pagina = cliente.get("/").get_data(as_text=True)

    assert '<span data-testid="intentos">5</span>' in pagina
    assert '<span data-testid="letras-incorrectas">Z</span>' in pagina

def test_la_dificultad_se_mantiene_despues_de_adivinar_una_letra():
    cliente = app.test_client()
    cliente.get("/?dificultad=dificil")

    cliente.post("/", data={"letra": "Z"})
    pagina = cliente.get("/").get_data(as_text=True)

    assert "<strong>dificil</strong>" in pagina

def test_reiniciar_mantiene_la_dificultad_elegida():
    cliente = app.test_client()
    cliente.get("/?dificultad=dificil")

    cliente.get("/reiniciar")
    pagina = cliente.get("/").get_data(as_text=True)

    assert "<strong>dificil</strong>" in pagina

def test_intentos_invalido_en_la_url_no_rompe_la_app():
    cliente = app.test_client()

    respuesta = cliente.get("/?word=GATO&intentos=abc")

    assert respuesta.status_code == 200
    assert '<span data-testid="intentos">6</span>' in respuesta.get_data(as_text=True)