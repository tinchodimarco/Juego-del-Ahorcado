# language: es
@HU-05
Característica: Declarar la victoria
  Como jugador
  quiero ver un mensaje de victoria al adivinar todas las letras
  para saber que gané la partida

  @CA-01
  Escenario: Adivinar la última letra correctamente
    Dado una partida con la palabra "SOL"
    Cuando ingreso la letra "S"
    Y ingreso la letra "O"
    Y ingreso la letra "L"
    Entonces se muestra el mensaje "¡Ganaste!"