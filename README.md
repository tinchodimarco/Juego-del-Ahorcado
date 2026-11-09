# Juego del Ahorcado

Trabajo Práctico de Metodologías Ágiles: ahorcado web hecho con ATDD (Cucumber/Gherkin + Playwright para los AT, pytest para los UT).

- Story Map / tablero: <PEGAR ACÁ EL LINK>
- Trazabilidad Historia → AT → UT: ver [NOTES.md](NOTES.md)
- App en producción: <PENDIENTE>

## Jugar
1. Instalá las dependencias: `python -m pip install -r requirements.txt`
2. Iniciá la aplicación: `python app.py`
3. Abrí `http://127.0.0.1:5000` en el navegador.
4. Ingresá una letra por vez. Las correctas se revelan; las incorrectas aparecen en la lista y descuentan un intento. Repetir una letra no descuenta otro intento.
5. Elegí la dificultad (Normal o Difícil) con los botones de la pantalla.
6. Al ganar o perder aparece **Reiniciar partida**.

Cada navegador conserva su propia partida.

## Tests
- Unit tests y cobertura (umbral 90% sobre `src/`): `pytest --cov=src --cov-fail-under=90`
- Acceptance tests: `playwright install chromium` (una vez) y luego `behave`
- Los AT de una historia: `behave --tags=@HU-02`