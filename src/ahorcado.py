#class Ahorcado:
 #   def __init__(self, palabra: str):
  #      self.palabra_secreta = palabra

   # def palabra_enmascarada(self) -> str:
    #    return " ".join(["_"] * len(self.palabra_secreta))

class Ahorcado:
    def __init__(self, palabra: str):
        self.palabra_secreta = palabra
        # Agregamos un conjunto (set) para guardar las letras que el jugador arriesga
        self.letras_adivinadas = set() 

    def adivinar_letra(self, letra: str):
        self.letras_adivinadas.add(letra)

    def palabra_enmascarada(self) -> str:
        # Recorremos la palabra secreta: mostramos la letra si fue adivinada, sino un "_"
        caracteres = [
            letra if letra in self.letras_adivinadas else "_" 
            for letra in self.palabra_secreta
        ]
        return " ".join(caracteres)