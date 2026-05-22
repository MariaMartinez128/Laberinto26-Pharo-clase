class Este(Orientacion):
    _instancia = None

    @classmethod
    def default(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def aceptar(self, visitor, forma):
        forma.este.aceptar(visitor)

    def caminar(self, bicho):
        em = bicho.posicion.forma.este
        em.entrar(bicho)

    def obtener_elemento(self, forma):
        return forma.este

    def poner_elemento(self, em, cont):
        cont.este = em

    def recorrer(self, func, cont):
        cont.este.recorrer(func)