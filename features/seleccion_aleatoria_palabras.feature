# language: es
Característica: Selección aleatoria de palabras
  Como jugador de Ahorcado
  Quiero que el sistema seleccione una palabra al azar al iniciar una nueva partida sin especificar parámetros
  Para comenzar a jugar de forma inmediata e impredecible.

  Escenario: Iniciar partida sin especificar palabra en la URL
    Dado que abro la página principal del juego sin parámetros
    Cuando visualizo el tablero
    Entonces veo la palabra enmascarada con una longitud mayor a cero
    