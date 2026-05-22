from Solucion.Orientacion import Orientacion

class Noroeste(Orientacion):
    _instancia = None

    @classmethod
    def default(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def caminar(self, bicho):
        em = bicho.posicion.forma.no
        em.entrar(bicho)

    def poner_elemento(self, em, cont):
        cont.no = em

    def recorrer(self, func, cont):
        cont.no.recorrer(func)
