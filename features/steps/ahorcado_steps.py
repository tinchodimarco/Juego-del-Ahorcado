from behave import given, then
from playwright.sync_api import sync_playwright, expect

@given('una partida con la palabra "{palabra}"')
def step_iniciar_partida(context, palabra):
    context.browser = sync_playwright().start().chromium.launch()
    context.page = context.browser.new_page()
    context.page.goto(f"http://localhost:5000/?word={palabra}")

@then('se ve la palabra "{esperada}"')
def step_verificar_palabra(context, esperada):
    elemento = context.page.get_by_test_id("word")
    expect(elemento).to_have_text(esperada)
    context.browser.close()