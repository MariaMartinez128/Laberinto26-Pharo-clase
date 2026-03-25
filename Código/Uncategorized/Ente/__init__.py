from abc import ABC, abstractmethod

class Ente(ABC):
    def __init__(self):
        self.vidas = 50
        self.poder = 1
        self.juego = None
        self.posicion = None

    def atacar(self):
        """atacar: busca un enemigo y lo ataca si existe"""
        enemigo = self.buscar_enemigo()
        if enemigo is not None:
            enemigo.es_atacado_por(self)

    @abstractmethod
    def buscar_enemigo(self):
        """SubclassResponsibility"""
        pass

    def es_atacado_por(self, un_bicho):
        """esAtacadoPor: unBicho"""
        self.vidas -= un_bicho.poder
        print(f"{self} es atacado por {un_bicho}")
        print(f"vidas: {self.vidas}")
        
        if self.vidas <= 0:
            self.juego.muere_personaje()

    def esta_vivo(self):
        return self.vidas > 0

    @abstractmethod
    def muero(self):
        """SubclassResponsibility"""
        pass