from Solucion.Hoja import Hoja

class Pared(Hoja):
    def aceptar(self, visitor):
        visitor.visitar_pared(self)

    def entrar(self, alguien):
        print(f"{alguien} se ha chocado con una pared")