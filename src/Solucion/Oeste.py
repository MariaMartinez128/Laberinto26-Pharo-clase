from Solucion.Orientacion import Orientacion

class Oeste(Orientacion):
    _instancia = None

    @classmethod
    def default(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def aceptar(self, visitor, forma):
        forma.oeste.aceptar(visitor)

    def caminar(self, bicho):
        em = bicho.posicion.forma.oeste
        em.entrar(bicho)

    def obtener_elemento(self, forma):
        return forma.oeste

    def poner_elemento(self, em, cont):
        cont.oeste = em

    def recorrer(self, func, cont):
        cont.oeste.recorrer(func)
