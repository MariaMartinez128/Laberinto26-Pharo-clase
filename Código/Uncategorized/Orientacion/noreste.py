from .orientacion import Orientacion

class Noreste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Noreste, cls).__new__(cls)
        return cls._instance

    def caminar(self, un_bicho):
        em = un_bicho.posicion.forma.noreste()
        em.entrar(un_bicho)

    def poner_elemento_en_contenedor(self, un_em, un_cont):
        un_cont.set_noreste(un_em)

    def recorrer_en_contenedor(self, un_bloque, un_cont):
        un_cont.forma.noreste().recorrer(un_bloque)