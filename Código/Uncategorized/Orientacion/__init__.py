from abc import ABC, abstractmethod

class Orientacion(ABC):
    @abstractmethod
    def caminar(self, un_bicho):
        """Equivalente a caminar: unBicho"""
        pass

    @abstractmethod
    def poner_elemento_en_contenedor(self, un_em, un_cont):
        """Equivalente a ponerElemento:unEm enContenedor:unCont"""
        pass