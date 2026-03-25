class Bomba(Decorator):
    def __init__(self, em):
        super().__init__(em)
        self.activa = False

    def activar(self): self.activa = True
    def desactivar(self): self.activa = False

    def entrar(self, alguien=None):
        if self.activa:
            if alguien:
                print(f"{alguien}, te ha explotado una bomba")
                # ToDo: alguien.vidas -= 10
            else:
                print("Ha explotado una bomba")
        
    def es_bomba(self): return True