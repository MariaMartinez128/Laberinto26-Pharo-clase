class Bomba(Hoja):
    def __init__(self):
        super().__init__()
        self.activa = False

    def aceptar(self, visitor):
        visitor.visitar_bomba(self)

    def activar(self):
        print("Bomba activada")
        self.activa = True

    def desactivar(self):
        print("Bomba desactivada")
        self.activa = False

    def entrar(self, alguien):
        if self.activa:
            print(f"{alguien} explotó")

    def es_bomba(self):
        return True
``