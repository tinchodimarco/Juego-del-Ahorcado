# language: es
@HU-11
Característica: Seleccionar dificultad de juego
  Como jugador
  Quiero elegir el nivel de dificultad antes de comenzar
  Para recibir palabras más desafiantes manteniendo las mismas vidas

  Escenario: Iniciar una partida en modo normal
    Dado que selecciono la dificultad "normal"
    Cuando inicio una nueva partida
    Entonces la palabra secreta tiene una longitud corta o moderada
    Y el contador de intentos muestra "6"

  Escenario: Iniciar una partida en modo difícil
    Dado que selecciono la dificultad "dificil"
    Cuando inicio una nueva partida
    Entonces la palabra secreta tiene una longitud mayor
    Y el contador de intentos muestra "6"

  Escenario: Se muestra la dificultad actual de la partida
    Dado que selecciono la dificultad "dificil"
    Cuando inicio una nueva partida
    Entonces veo que la dificultad actual es "dificil"

  
  Escenario: La dificultad se mantiene después de adivinar una letra
    Dado que selecciono la dificultad "dificil"
    Cuando inicio una nueva partida
    Y ingreso la letra "Z"
    Entonces veo que la dificultad actual es "dificil"

    
  Escenario: Reiniciar la partida mantiene la dificultad elegida
    Dado que selecciono la dificultad "dificil"
    Cuando inicio una nueva partida
    Y reinicio la partida
    Entonces veo que la dificultad actual es "dificil"