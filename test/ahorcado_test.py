import pytest
from src.ahorcado import Ahorcado

def test_representa_palabra_inicial_con_guiones_bajos():
    juego = Ahorcado("GATO")
    assert juego.palabra_enmascarada() == "_ _ _ _"