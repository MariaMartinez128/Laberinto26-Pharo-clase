from .orientacion import Orientacion

class Este(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Este, cls).__new__(cls)
        return cls._instance

    def caminar(self, un_bicho):
        em = un_bicho.posicion.forma.este()
        em.entrar(un_bicho)

    def poner_elemento_en_contenedor(self, un_em, un_cont):
        un_cont.set_este(un_em)

    def recorrer_en_contenedor(self, un_bloque, un_cont):
        un_cont.forma.este().recorrer(un_bloque)