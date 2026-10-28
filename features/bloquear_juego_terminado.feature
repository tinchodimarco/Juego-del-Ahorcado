# language: es
@HU-08
Característica: Bloquear entradas al finalizar la partida
  Como jugador del Ahorcado
  Quiero que el sistema rechace el ingreso de más letras cuando la partida ya haya terminado
  Para evitar que se sigan modificando los intentos o el estado del juego tras ganar o perder

  Escenario: No se pueden ingresar letras tras perder la partida
    Dado una partida con la palabra "SOL" y 1 intentos
    Cuando ingreso la letra "X"
    Y ingreso la letra "S"
    Entonces el contador de intentos se mantiene en "0"
    Y se muestra el mensaje "¡Perdiste!"

  Escenario: No se pueden ingresar letras tras ganar la partida
    Dado una partida con la palabra "SOL"
    Cuando ingreso la letra "S"
    Y ingreso la letra "O"
    Y ingreso la letra "L"
    Y ingreso la letra "X"
    Entonces se muestra el mensaje "¡Ganaste!"
    Y la letra "X" no se agrega a las letras incorrectas