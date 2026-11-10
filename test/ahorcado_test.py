import pytest
from src.ahorcado import Ahorcado, obtener_palabra_por_dificultad, obtener_palabra_aleatoria



def test_representa_palabra_inicial_con_guiones_bajos():
    juego = Ahorcado("GATO")
    assert juego.palabra_enmascarada() == "_ _ _ _"

def test_representa_palabra_de_diferente_longitud():
    juego = Ahorcado("PERRO")
    assert juego.palabra_enmascarada() == "_ _ _ _ _"

def test_adivinar_letra_correcta_actualiza_la_palabra_enmascarada():
    juego = Ahorcado("GATO")
    juego.adivinar_letra("A")  # Inventamos este método
    assert juego.palabra_enmascarada() == "_ A _ _"

def test_adivinar_letra_repetida_en_otra_palabra():
    juego = Ahorcado("PERRO")
    juego.adivinar_letra("R")
    assert juego.palabra_enmascarada() == "_ _ R R _"

def test_letra_incorrecta_descuenta_intento():
    juego = Ahorcado("GATO", intentos=6)
    juego.adivinar_letra("Z")
    assert juego.intentos == 5

def test_letra_incorrecta_se_agrega_a_conjunto_de_incorrectas():
    juego = Ahorcado("GATO")
    juego.adivinar_letra("Z")
    assert "Z" in juego.letras_incorrectas

def test_juego_esta_ganado_cuando_se_adivinan_todas_las_letras():
    juego = Ahorcado("SOL")
    juego.adivinar_letra("S")
    juego.adivinar_letra("O")
    juego.adivinar_letra("L")
    assert juego.esta_ganado() is True

def test_juego_esta_perdido_cuando_se_agotan_los_intentos():
    juego = Ahorcado("SOL", intentos=1)
    assert juego.esta_perdido() is False
    juego.adivinar_letra("X")  # Falla y gasta el último intento
    assert juego.esta_perdido() is True

def test_reiniciar_resetea_intentos_y_letras():
    
    juego = Ahorcado("SOL")
    juego.adivinar_letra("X")  # Falla un intento
    juego.adivinar_letra("S")  # Aciierta
    
    
    juego.reiniciar("LUNA")
    
    assert juego.palabra_secreta == "LUNA"
    assert juego.intentos == 6
    assert len(juego.letras_adivinadas) == 0
    assert len(juego.letras_incorrectas) == 0

def test_no_permite_adivinar_letras_cuando_partida_termina():
    juego = Ahorcado("SOL", intentos=1)
    juego.adivinar_letra("X")  # Pierde el juego
    assert juego.esta_perdido() is True
    
    intentos_antes = juego.intentos
    juego.adivinar_letra("S")  # Intenta adivinar de nuevo
    
    # Comprobamos que el estado no cambió y no sigue descontando o agregando
    assert juego.intentos == intentos_antes
    assert "S" not in juego.letras_adivinadas

def test_obtener_palabra_aleatoria_retorna_una_palabra_valida():
    palabras = ["PYTHON", "FLASK", "AGILE", "TESTING"]
    palabra = obtener_palabra_aleatoria(palabras)
    assert palabra in palabras

def test_juego_se_inicializa_con_palabra_aleatoria_por_defecto(monkeypatch):
    # Usamos *args para que no importe si se llama con o sin argumentos
     monkeypatch.setattr("src.ahorcado.obtener_palabra_aleatoria", lambda *args: "PYTHON")
     juego = Ahorcado()
     assert juego.palabra_secreta == "PYTHON"

def test_cantidad_errores_retorna_numero_de_incorrectas():
    juego = Ahorcado("GATO")
    assert juego.obtener_cantidad_errores() == 0
    juego.adivinar_letra("Z")
    assert juego.obtener_cantidad_errores() == 1

def test_obtener_dibujo_muestra_estado_inicial_y_con_errores():
    juego = Ahorcado("GATO")
    # Estado inicial (0 errores) -> debe mostrar la horca sin el monigote
    dibujo_inicial = juego.obtener_dibujo()
    assert "+---+" in dibujo_inicial
    
    # Cometemos un error
    juego.adivinar_letra("Z")
    dibujo_con_error = juego.obtener_dibujo()
    # Verificamos que aparece la cabeza 'O' tras el primer error
    assert "O" in dibujo_con_error

def test_palabra_según_dificultad_normal():
    juego = Ahorcado(dificultad="normal")
    assert len(juego.palabra_secreta) <= 5

def test_palabra_según_dificultad_dificil():
    juego = Ahorcado(dificultad="dificil")
    assert len(juego.palabra_secreta) > 5

def test_juego_guarda_la_dificultad_con_la_que_se_crea():
    juego = Ahorcado("GATO", dificultad="dificil")
    assert juego.dificultad == "dificil"

@pytest.mark.parametrize("entrada", ["a", "Z", "ñ"])
def test_es_letra_valida_acepta_una_sola_letra(entrada):
    assert Ahorcado.es_letra_valida(entrada) is True


@pytest.mark.parametrize("entrada", ["1", "?", "ab", "", " "])
def test_es_letra_valida_rechaza_lo_que_no_es_una_sola_letra(entrada):
    assert Ahorcado.es_letra_valida(entrada) is False