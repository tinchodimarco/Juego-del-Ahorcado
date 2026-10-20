# language: es
@HU-03
Característica: Descontar intentos al fallar
  Como jugador
  quiero que se descuenten intentos al arriesgar una letra incorrecta
  para medir mis vidas restantes

  @CA-01
  Escenario: Arriesgar una letra incorrecta
    Dado una partida con la palabra "GATO" y 6 intentos
    Cuando ingreso la letra "Z"
    Entonces el contador de intentos muestra "5"