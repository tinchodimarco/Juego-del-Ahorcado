import threading
from wsgiref import simple_server
from playwright.sync_api import sync_playwright
from app import app # Importa la app de tu app.py

def before_all(context):
    # Levantar Flask en un hilo paralelo para que no bloquee los tests
    context.server = simple_server.make_server('127.0.0.1', 5000, app)
    context.thread = threading.Thread(target=context.server.serve_forever)
    context.thread.start()
    
    # Iniciar Playwright a nivel global (una sola vez)
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch()

def after_all(context):
    # Cerrar todo de forma segura al terminar la suite
    context.browser.close()
    context.playwright.stop()
    context.server.shutdown()
    context.thread.join()

def before_scenario(context, scenario):
    # Cada escenario arranca con una pestaña en blanco
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    # Se cierra la pestaña al final (falle o pase el test)
    context.page.close()