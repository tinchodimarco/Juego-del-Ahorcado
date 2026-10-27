import pytest
from src.ahorcado import Ahorcado

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