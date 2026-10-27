# language: es
@HU-06
Característica: Declarar la derrota
  Como jugador
  quiero ver un mensaje de derrota cuando se agoten mis intentos
  para saber que perdí la partida

  @CA-01
  Escenario: Agotar todos los intentos arriesgando letras incorrectas
    Dado una partida con la palabra "SOL"
    Cuando ingreso la letra "X"
    Y ingreso la letra "Y"
    Y ingreso la letra "Z"
    Y ingreso la letra "A"
    Y ingreso la letra "B"
    Y ingreso la letra "C"
    Entonces se muestra el mensaje "¡Perdiste!"