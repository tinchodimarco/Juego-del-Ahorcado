# language: es
@HU-12
Característica: Validar la letra ingresada
  Como jugador del Ahorcado
  Quiero que el juego me avise si lo que ingreso no es una letra
  Para corregir mi entrada sin perder intentos

  @CA-01
  Escenario: Un símbolo no se acepta y no descuenta intentos
    Dado una partida con la palabra "GATO"
    Cuando ingreso la letra "1"
    Entonces veo el aviso "Ingresá una sola letra"
    Y el contador de intentos muestra "6"