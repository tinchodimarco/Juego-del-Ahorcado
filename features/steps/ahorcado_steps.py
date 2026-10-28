from behave import given, when, then
from playwright.sync_api import expect

# --- Pasos existentes ---

@given('una partida con la palabra "{palabra}"')
def step_iniciar_partida(context, palabra):
    context.page.goto(f"http://127.0.0.1:5000/?word={palabra}")

@then('se ve la palabra "{esperada}"')
def step_verificar_palabra(context, esperada):
    elemento = context.page.get_by_test_id("word")
    expect(elemento).to_have_text(esperada)

@when('ingreso la letra "{letra}"')
def step_ingresar_letra(context, letra):
    # Buscamos el input en la pantalla, escribimos la letra y hacemos clic en adivinar
    context.page.get_by_test_id("letra-input").fill(letra)
    context.page.get_by_test_id("adivinar-btn").click()

# --- Pasos agregados para HU-03 (Descontar intentos) ---

@given('una partida con la palabra "{palabra}" y {intentos:d} intentos')
def step_iniciar_partida_con_intentos(context, palabra, intentos):
    context.page.goto(f"http://127.0.0.1:5000/?word={palabra}")

@then('el contador de intentos muestra "{intentos_esperados}"')
def step_verificar_intentos(context, intentos_esperados):
    elemento = context.page.get_by_test_id("intentos")
    expect(elemento).to_have_text(intentos_esperados)

# --- Paso para HU-04 (Registrar letras incorrectas)

@then('se muestra "{letra}" en las letras incorrectas')
def step_verificar_letras_incorrectas(context, letra):
    elemento = context.page.get_by_test_id("letras-incorrectas")
    expect(elemento).to_contain_text(letra)

    # --- Paso para HU-05 (Ganar partida)

@then('se muestra el mensaje "{mensaje_esperado}"')
def step_verificar_mensaje_estado(context, mensaje_esperado):
    elemento = context.page.get_by_test_id("mensaje-estado")
    expect(elemento).to_have_text(mensaje_esperado)

from playwright.sync_api import expect

@given(u'que inicio una nueva partida con la palabra "{palabra}"')
def step_iniciar_partida_con_palabra(context, palabra):
    context.page.goto(f"http://127.0.0.1:5000/?palabra={palabra}")

@given(u'agoto todos mis intentos fallando las letras')
def step_agotar_intentos(context):
    letras_incorrectas = ["X", "Y", "Z", "W", "V", "K"]
    for letra in letras_incorrectas:
        context.page.fill("input[name='letra']", letra)
        context.page.click("button[type='submit']")

@given(u'adivino correctamente todas las letras')
def step_adivinar_todas_las_letras(context):
    # Asumiendo que la palabra del escenario es "SOL"
    letras = ["S", "O", "L"]
    for letra in letras:
        context.page.fill("input[name='letra']", letra)
        context.page.click("button[type='submit']")

@then(u'veo el botón para reiniciar la partida')
def step_ver_boton_reiniciar(context):
    boton = context.page.locator("button.btn-reiniciar")
    expect(boton).to_be_visible()

@then(u'el contador de intentos se mantiene en "{intentos}"')
def step_impl(context, intentos):
    assert str(context.juego.intentos) == intentos

@then(u'la letra "{letra}" no se agrega a las letras incorrectas')
def step_impl(context, letra):
    assert letra not in context.juego.letras_incorrectas