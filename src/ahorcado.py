
import random

def obtener_palabra_aleatoria(lista_palabras=None):
    if lista_palabras is None:
        lista_palabras = ["PYTHON", "FLASK", "AGILE", "TESTING", "AHORCADO"]
    return random.choice(lista_palabras)

class Ahorcado:
    def __init__(self, palabra: str = None, intentos: int = 6):
        if palabra is None:
            palabra = obtener_palabra_aleatoria()
        self.palabra_secreta = palabra.upper()
        self.intentos = intentos
        self.letras_adivinadas = set() 
        self.letras_incorrectas = set()

    def adivinar_letra(self, letra: str):
        # Si el juego ya terminó, no permitimos seguir jugando
        if self.esta_ganado() or self.esta_perdido():
            return

        letra = letra.strip().upper()
        if len(letra) != 1 or not letra.isalpha():
            return

        if letra in self.letras_adivinadas or letra in self.letras_incorrectas:
            return

        if letra in self.palabra_secreta:
            self.letras_adivinadas.add(letra)
        else:
            self.intentos -= 1
            self.letras_incorrectas.add(letra)

    def palabra_enmascarada(self) -> str:
        # Recorremos la palabra secreta: mostramos la letra si fue adivinada, sino un "_"
        caracteres = [
            letra if letra in self.letras_adivinadas else "_" 
            for letra in self.palabra_secreta
        ]
        return " ".join(caracteres)
    
    def esta_ganado(self) -> bool:
        # Retorna True si todas las letras de la palabra secreta fueron adivinadas
        return set(self.palabra_secreta).issubset(self.letras_adivinadas)

    def esta_perdido(self) -> bool:
        return self.intentos <= 0
    
    def reiniciar(self, nueva_palabra: str, intentos: int = 6):
        self.palabra_secreta = nueva_palabra.upper()
        self.intentos = intentos
        self.letras_adivinadas.clear()
        self.letras_incorrectas.clear()

