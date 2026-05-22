from Solucion.Orientacion import Orientacion

class Norte(Orientacion):
    _instancia = None

    @classmethod
    def default(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def aceptar(self, visitor, forma):
        forma.norte.aceptar(visitor)

    def caminar(self, bicho):
        em = bicho.posicion.forma.norte
        em.entrar(bicho)

    def obtener_elemento(self, forma):
        return forma.norte

    def poner_elemento(self, em, cont):
        cont.norte = em

    def recorrer(self, func, cont):
        cont.norte.recorrer(func)