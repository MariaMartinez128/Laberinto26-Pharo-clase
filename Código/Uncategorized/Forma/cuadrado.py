from Uncategorized.forma import Forma


class Cuadrado(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    # Métodos setter para que las clases Orientacion puedan usarlos
    def set_norte(self, un_em): self.norte = un_em
    def set_sur(self, un_em):   self.sur = un_em
    def set_este(self, un_em):  self.este = un_em
    def set_oeste(self, un_em): self.oeste = un_em