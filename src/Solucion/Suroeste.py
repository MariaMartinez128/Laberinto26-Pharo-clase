from Solucion.Orientacion import Orientacion

class Suroeste(Orientacion):
    _instancia = None

    @classmethod
    def default(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def caminar(self, bicho):
        em = bicho.posicion.forma.so
        em.entrar(bicho)

    def poner_elemento(self, em, cont):
        cont.so = em

    def recorrer(self, func, cont):
        cont.so.recorrer(func)