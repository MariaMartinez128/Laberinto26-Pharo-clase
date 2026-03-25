import time
from abc import ABC, abstractmethod

class Modo(ABC):
    def actua(self, un_bicho):
        """actua: unBicho"""
        self.camina(un_bicho)
        un_bicho.atacar()
        self.duerme(un_bicho)

    def camina(self, un_bicho):
        """camina: unBicho"""
        # or := unBicho posicion forma obtenerOrientacionAleatoria
        orientacion = un_bicho.posicion.forma.obtener_orientacion_aleatoria()
        orientacion.caminar(un_bicho)

    @abstractmethod
    def duerme(self, un_bicho):
        """duerme: unBicho -> SubclassResponsibility"""
        pass

    def es_agresivo(self):
        """esAgresivo -> ^false"""
        return False

    def es_perezoso(self):
        """esPerezoso -> ^false"""
        return False