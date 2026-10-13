# language: es
@HU-02
Característica: Acertar una letra
  Como jugador
  quiero ingresar una letra que pertenezca a la palabra
  para descubrir su posición

@CA-01
  Escenario: Adivinar una letra correcta
    Dado una partida con la palabra "GATO"
    Cuando ingreso la letra "A"
    Entonces se ve la palabra "_ A _ _"