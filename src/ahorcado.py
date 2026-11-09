
import random

def obtener_palabra_aleatoria(lista_palabras=None):
    if lista_palabras is None:
        lista_palabras = ["PYTHON", "FLASK", "AGILE", "TESTING", "AHORCADO"]
    return random.choice(lista_palabras)

def obtener_palabra_por_dificultad(dificultad: str = "normal") -> str:
    # Definimos listas diferenciadas por longitud de palabra
    if dificultad == "dificil":
        palabras = ["PROGRAMACION", "DESARROLLADOR", "ARQUITECTURA", "ALGORITMO"]
    else:
        # Modo normal: palabras cortas o moderadas (<= 5 o 6 letras)
        palabras = ["GATO", "PERRO", "CASA", "FLASK"]
    return obtener_palabra_aleatoria(palabras)

class Ahorcado:
    def __init__(self, palabra: str = None, intentos: int = 6, dificultad: str = "normal"):
        if palabra is None:
            palabra = obtener_palabra_por_dificultad(dificultad)
        self.palabra_secreta = palabra.upper()
        self.dificultad = dificultad
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

    def obtener_cantidad_errores(self) -> int:
        return len(self.letras_incorrectas)

    def obtener_dibujo(self) -> str:
        # Definimos los estados del dibujo del ahorcado (de 0 a 6 errores)
        estados = [
            """
              +---+
                  |
                  |
                  |
                 ===
            """,
            """
              +---+
              O   |
                  |
                  |
                 ===
            """,
            """
              +---+
              O   |
              |   |
                  |
                 ===
            """,
            """
              +---+
              O   |
             /|   |
                  |
                 ===
            """,
            """
              +---+
              O   |
             /|\  |
                  |
                 ===
            """,
            """
              +---+
              O   |
             /|\  |
             /    |
                 ===
            """,
            """
              +---+
              O   |
             /|\  |
             / \  |
                 ===
            """
        ]
        # Limitamos el índice al máximo de estados disponibles (6 errores)
        cantidad_errores = min(len(self.letras_incorrectas), len(estados) - 1)
        return estados[cantidad_errores]

