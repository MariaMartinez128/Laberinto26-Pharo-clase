from abc import ABC, abstractmethod

class ElementoMapa(ABC):
    @abstractmethod
    def entrar(self, alguien=None):
        """entrar / entrar: alguien"""
        pass

    def es_bomba(self): return False
    def es_puerta(self): return False

    @abstractmethod
    def recorrer(self, un_bloque):
        pass

