class Sur(Orientacion):
    _instancia = None

    @classmethod
    def default(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def aceptar(self, visitor, forma):
        forma.sur.aceptar(visitor)

    def caminar(self, bicho):
        em = bicho.posicion.forma.sur
        em.entrar(bicho)

    def obtener_elemento(self, forma):
        return forma.sur

    def poner_elemento(self, em, cont):
        cont.sur = em

    def recorrer(self, func, cont):
        cont.sur.recorrer(func)