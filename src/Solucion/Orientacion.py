class Orientacion:
    def aceptar(self, visitor, forma):
        raise NotImplementedError

    def caminar(self, bicho):
        raise NotImplementedError

    def obtener_elemento(self, forma):
        raise NotImplementedError

    def poner_elemento(self, em, cont):
        raise NotImplementedError

    def recorrer(self, func, cont):
        raise NotImplementedError