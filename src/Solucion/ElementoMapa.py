class ElementoMapa:
    def __init__(self):
        self.comandos = []

    def aceptar(self, visitor): raise NotImplementedError
    def agregar_comando(self, c): self.comandos.append(c)
    def entrar(self, alguien): raise NotImplementedError

    def es_armario(self): return False
    def es_bomba(self): return False
    def es_puerta(self): return False
    def es_tunel(self): return False