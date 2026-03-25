from .orientacion import Orientacion

class Sureste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Sureste, cls).__new__(cls)
        return cls._instance

    def caminar(self, un_bicho):
        em = un_bicho.posicion.forma.sureste()
        em.entrar(un_bicho)

    def poner_elemento_en_contenedor(self, un_em, un_cont):
        un_cont.set_sureste(un_em)

    def recorrer_en_contenedor(self, un_bloque, un_cont):
        un_cont.forma.sureste().recorrer(un_bloque)