from behave import given, when, then
from playwright.sync_api import expect

@given('una partida con la palabra "{palabra}"')
def step_iniciar_partida(context, palabra):
    context.page.goto(f"http://127.0.0.1:5000/?word={palabra}")

@given('una partida con la palabra "{palabra}" y {intentos:d} intentos')
def step_iniciar_partida_con_intentos(context, palabra, intentos):
    context.page.goto(
        f"http://127.0.0.1:5000/?word={palabra}&intentos={intentos}"
    )

@given('que inicio una nueva partida con la palabra "{palabra}"')
def step_iniciar_nueva_partida(context, palabra):
    context.page.goto(f"http://127.0.0.1:5000/?word={palabra}")

@when('ingreso la letra "{letra}"')
def step_ingresar_letra(context, letra):
    context.page.get_by_test_id("letra-input").fill(letra)
    context.page.get_by_test_id("adivinar-btn").click()

@then('se ve la palabra "{esperada}"')
def step_verificar_palabra(context, esperada):
    elemento = context.page.get_by_test_id("word")
    expect(elemento).to_have_text(esperada)

@then('el contador de intentos muestra "{intentos_esperados}"')
def step_verificar_intentos(context, intentos_esperados):
    elemento = context.page.get_by_test_id("intentos")
    expect(elemento).to_have_text(intentos_esperados)

@then('se muestra "{letra}" en las letras incorrectas')
def step_verificar_letras_incorrectas(context, letra):
    elemento = context.page.get_by_test_id("letras-incorrectas")
    expect(elemento).to_contain_text(letra)

@then('se muestra el mensaje "{mensaje_esperado}"')
def step_verificar_mensaje_estado(context, mensaje_esperado):
    elemento = context.page.get_by_test_id("mensaje-estado")
    expect(elemento).to_have_text(mensaje_esperado)

@given('agoto todos mis intentos fallando las letras')
def step_agotar_intentos(context):
    letras_incorrectas = ["X", "Y", "Z", "W", "V", "K"]
    for letra in letras_incorrectas:
        context.page.fill("input[name='letra']", letra)
        context.page.click("button[type='submit']")

@given('adivino correctamente todas las letras')
def step_adivinar_todas_las_letras(context):
    letras = ["S", "O", "L"]
    for letra in letras:
        context.page.fill("input[name='letra']", letra)
        context.page.click("button[type='submit']")

@then('veo el botón para reiniciar la partida')
def step_ver_boton_reiniciar(context):
    boton = context.page.locator("button.btn-reiniciar")
    expect(boton).to_be_visible()

@then('no veo el botón para reiniciar la partida')
def step_no_ver_boton_reiniciar(context):
    boton = context.page.locator("button.btn-reiniciar")
    expect(boton).to_be_hidden()

@then('el contador de intentos se mantiene en "{intentos}"')
def step_verificar_intentos_mantenidos(context, intentos):
    elemento = context.page.get_by_test_id("intentos")
    expect(elemento).to_have_text(intentos)

@then('la letra "{letra}" no se agrega a las letras incorrectas')
def step_verificar_letra_no_en_incorrectas(context, letra):
    elemento = context.page.get_by_test_id("letras-incorrectas")
    if elemento.count() > 0:
        texto = elemento.inner_text()
        assert letra not in texto

@given('que abro la página principal del juego sin parámetros')
def step_abrir_sin_parametros(context):
    context.page.goto("http://127.0.0.1:5000/")

@when('visualizo el tablero')
def step_visualizar_tablero(context):
    context.page.wait_for_selector("body")

@then('veo la palabra enmascarada con una longitud mayor a cero')
def step_ver_palabra_enmascarada(context):
    contenido = context.page.text_content("body")
    assert "_" in contenido

@then('se visualiza el elemento gráfico del ahorcado con la estructura inicial')
def step_verificar_dibujo_inicial(context):
    elemento = context.page.get_by_test_id("ahorcado-dibujo")
    expect(elemento).to_contain_text("+---+")

@then('se visualiza el elemento gráfico del ahorcado con la cabeza')
def step_verificar_dibujo_cabeza(context):
    elemento = context.page.get_by_test_id("ahorcado-dibujo")
    expect(elemento).to_contain_text("O")

@given('que selecciono la dificultad "{dificultad}"')
def step_seleccionar_dificultad(context, dificultad: str):
    context.dificultad_seleccionada = dificultad

@when('inicio una nueva partida')
def step_iniciar_partida(context):
    dificultad = getattr(context, 'dificultad_seleccionada', 'normal')
    # Navegamos a la app pasando la dificultad por parámetro
    context.page.goto(f"http://127.0.0.1:5000/?dificultad={dificultad}")

@then('la palabra secreta tiene una longitud corta o moderada')
def step_verificar_palabra_corta(context):
    texto = context.page.locator("[data-testid='word']").inner_text()
    letras = texto.replace(" ", "")
    assert len(letras) <= 5, f"La palabra '{letras}' es muy larga para el modo normal"

@then('la palabra secreta tiene una longitud mayor')
def step_verificar_palabra_larga(context):
    texto = context.page.locator("[data-testid='word']").inner_text()
    letras = texto.replace(" ", "")
    assert len(letras) > 5, f"La palabra '{letras}' es muy corta para el modo difícil"

