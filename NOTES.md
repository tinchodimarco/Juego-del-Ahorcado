# NOTES · Trazabilidad Historia → AT → UT

Story Map / tablero: (https://miro.com/app/board/uXjVHq5RpzY=/)

## Mecanismo
Combinamos dos cosas:
1. Etiqueta `@HU-xx` sobre cada `Característica` (una por historia) y `@CA-xx` sobre el escenario que confirma un criterio concreto.
2. Esta matriz, que baja hasta los unit tests.

- De arriba hacia abajo: `behave --tags=@HU-02` corre los AT de esa historia, y la tabla dice qué UTs la sostienen.
- De abajo hacia arriba: buscar el nombre del test en la tabla y leer su historia.

Estado = todos los escenarios de la historia en verde en `behave`.

## Matriz
| HU | Historia | Escenarios (AT) | Unit tests | Estado |
|---|---|---|---|---|
| HU-01 | Ver la longitud de la palabra | `longitud.feature`: inicio con palabra enmascarada | `test_representa_palabra_inicial_con_guiones_bajos`, `test_representa_palabra_de_diferente_longitud` | ✅ |
| HU-02 | Acertar una letra | `acertar_letra.feature`: adivinar una letra correcta | `test_adivinar_letra_correcta_actualiza_la_palabra_enmascarada`, `test_adivinar_letra_repetida_en_otra_palabra` | ✅ |
| HU-03 | Descontar intentos al fallar | `intentos.feature`: arriesgar una letra incorrecta | `test_letra_incorrecta_descuenta_intento` | ✅ |
| HU-04 | Registrar letras incorrectas | `letras_incorrectas.feature`: arriesgar una letra incorrecta | `test_letra_incorrecta_se_agrega_a_conjunto_de_incorrectas`, `test_repetir_letra_incorrecta_no_descuenta_otro_intento` (app) | ✅ |
| HU-05 | Declarar la victoria | `victoria.feature`: adivinar la última letra | `test_juego_esta_ganado_cuando_se_adivinan_todas_las_letras` | ✅ |
| HU-06 | Declarar la derrota | `derrota.feature`: agotar los intentos | `test_juego_esta_perdido_cuando_se_agotan_los_intentos` | ✅ |
| HU-07 | Reiniciar al finalizar | `reiniciar.feature`: botón oculto en curso, visible al perder, visible al ganar | `test_reiniciar_resetea_intentos_y_letras`, `test_juego_esta_ganado_...`, `test_juego_esta_perdido_...` | ✅ |
| HU-08 | Bloquear entradas al finalizar | `bloquear_juego_terminado.feature`: tras perder, tras ganar | `test_no_permite_adivinar_letras_cuando_partida_termina` | ✅ |
| HU-09 | Selección aleatoria de palabras | `seleccion_aleatoria_palabras.feature`: partida sin palabra en la URL | `test_obtener_palabra_aleatoria_retorna_una_palabra_valida`, `test_juego_se_inicializa_con_palabra_aleatoria_por_defecto` | ✅ |
| HU-10 | Dibujo progresivo del ahorcado | `dibujo_ahorcado.feature`: dibujo inicial, dibujo con cabeza tras un error | `test_cantidad_errores_retorna_numero_de_incorrectas`, `test_obtener_dibujo_muestra_estado_inicial_y_con_errores` | ✅ |
| HU-11 | Seleccionar dificultad | `dificultad.feature`: modo normal, modo difícil, dificultad visible, dificultad se mantiene | `test_palabra_según_dificultad_normal`, `test_palabra_según_dificultad_dificil`, `test_juego_guarda_la_dificultad_con_la_que_se_crea`, `test_la_dificultad_se_mantiene_despues_de_adivinar_una_letra` (app) | ✅ |

## Pendientes conocidos
- `test_cada_cliente_conserva_su_propia_partida` (app) no tiene historia asignada.
- HU-09: el AT solo verifica que haya un `_` en la página.
- Entrada inválida: sin AT ni UT (línea sin cubrir en `src/ahorcado.py`).
- Pipeline: faltan análisis estático con quality gate y deploy.

## Convención de commits
`RED:` / `GREEN:` / `REFACTOR:` con el nivel entre corchetes: `RED: [AT] HU-xx ...`, `GREEN: [UT] HU-xx ...`.
Sin ciclo de test: `DOCS:`, `CHORE:`, `CI:`, `STYLE:`.