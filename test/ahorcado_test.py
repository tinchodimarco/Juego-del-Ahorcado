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