# -*- coding: utf-8 -*-
import random
from Solucion.ElementoMapa import ElementoMapa


class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.forma = None
        self.num = None

    def aceptar(self, visitor):
        self.aceptar_contenedor(visitor)
        for h in self.hijos:
            h.aceptar(visitor)
        for o in self.forma.orientaciones:
            o.aceptar(visitor, self.forma)

    def aceptar_contenedor(self, visitor):
        raise NotImplementedError

    def agregar_hijo(self, em):
        self.hijos.append(em)

    def entrar(self, alguien):
        print(f"{alguien} está en {self}")
        alguien.posicion = self

    def poner_en(self, orien, em):
        self.forma.poner_en(orien, em)

    def obtener_orientacion_aleatoria(self):
        return random.choice(self.forma.orientaciones)
