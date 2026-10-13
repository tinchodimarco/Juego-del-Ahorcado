from behave import given, when, then
from playwright.sync_api import expect

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