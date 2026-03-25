from .orientacion import Orientacion

class Norte(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Norte, cls).__new__(cls)
        return cls._instance

    def caminar(self, un_bicho):
        em = un_bicho.posicion.forma.norte()
        em.entrar(un_bicho)

    def poner_elemento_en_contenedor(self, un_em, un_cont):
        un_cont.set_norte(un_em)

    def recorrer_en_contenedor(self, un_bloque, un_cont):
        un_cont.forma.norte().recorrer(un_bloque)