# Juego-del-Ahorcado
Trabajo Práctico del juego del ahorcado basado en la metodologia de trabajo ATDD.
Historia de usuario 1: Como jugador quiero ver la longitud de la palabra para orientarme
Criterio de aceptación: debe ver un espacio vacío (guion bajo sería) por cada letra de la palabra.

## Jugar

1. Instala las dependencias con `python -m pip install -r requirements.txt`.
2. Inicia la aplicación con `python app.py`.
3. Abre `http://127.0.0.1:5000` en el navegador.
4. Ingresa una letra por vez. Las letras correctas se revelan; las incorrectas aparecen en la lista y descuentan un intento. Repetir una letra no descuenta otro intento.
5. Usa **Reiniciar partida** para comenzar con una palabra aleatoria nueva.

Cada navegador conserva su propia partida.