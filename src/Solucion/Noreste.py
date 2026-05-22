class Noreste(Orientacion):
    _instancia = None

    @classmethod
    def default(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def caminar(self, bicho):
        em = bicho.posicion.forma.ne
        em.entrar(bicho)

    def poner_elemento(self, em, cont):
        cont.ne = em

    def recorrer(self, func, cont):
        cont.ne.recorrer(func)