# language: es
@HU-04
Característica: Registrar letras incorrectas
  Como jugador
  quiero ver las letras incorrectas que ya arriesgué
  para no volver a intentarlas

  @CA-01
  Escenario: Arriesgar una letra incorrecta
    Dado una partida con la palabra "GATO"
    Cuando ingreso la letra "Z"
    Entonces se muestra "Z" en las letras incorrectas