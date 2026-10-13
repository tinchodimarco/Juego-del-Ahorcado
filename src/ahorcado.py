class Ahorcado:
    def __init__(self, palabra: str):
        self.palabra_secreta = palabra

    def palabra_enmascarada(self) -> str:
        return " ".join(["_"] * len(self.palabra_secreta))