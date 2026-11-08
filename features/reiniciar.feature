# language: es
@HU-07
Característica: Reiniciar la partida al finalizar
  Como jugador del Ahorcado
  Quiero que aparezca un botón de reinicio al terminar la partida
  Para poder volver a jugar de inmediato si gano o pierdo

  @CA-01
  Escenario: El botón de reiniciar no aparece mientras la partida está en curso
    Dado una partida con la palabra "GATO"
    Cuando ingreso la letra "A"
    Entonces no veo el botón para reiniciar la partida

  Escenario: El botón de reiniciar aparece cuando se pierden todos los intentos
    Dado que inicio una nueva partida con la palabra "SOL"
    Y agoto todos mis intentos fallando las letras
    Entonces veo el botón para reiniciar la partida

  Escenario: El botón de reiniciar aparece cuando se adivina la palabra
    Dado que inicio una nueva partida con la palabra "SOL"
    Y adivino correctamente todas las letras
    Entonces veo el botón para reiniciar la partida