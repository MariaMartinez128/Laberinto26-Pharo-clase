from Solucion.Contenedor import Contenedor

class Armario(Contenedor):
    def aceptar_contenedor(self, visitor):
        visitor.visitar_armario(self)

    def es_armario(self):
        return True