# language: es

@HU-10
Característica: Dibujo progresivo del ahorcado
  Como jugador de Ahorcado
  Quiero ver el dibujo del ahorcado completándose a medida que fallo intentos
  Para tener una representación visual de mis errores

  Escenario: Se muestra el dibujo inicial limpio al comenzar la partida
    Dado una partida con la palabra "GATO"
    Entonces se visualiza el elemento gráfico del ahorcado con la estructura inicial

  Escenario: El dibujo avanza al cometer un error
    Dado una partida con la palabra "GATO"
    Cuando ingreso la letra "Z"
    Entonces se visualiza el elemento gráfico del ahorcado con la cabeza