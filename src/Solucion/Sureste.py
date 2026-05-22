from Solucion.Orientacion import Orientacion

class Sureste(Orientacion):
    _instancia = None

    @classmethod
    def default(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def caminar(self, bicho):
        em = bicho.posicion.forma.se
        em.entrar(bicho)

    def poner_elemento(self, em, cont):
        cont.se = em

    def recorrer(self, func, cont):
        cont.se.recorrer(func)
