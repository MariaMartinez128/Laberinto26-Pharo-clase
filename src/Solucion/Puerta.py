# -*- coding: utf-8 -*-
from Solucion.Hoja import Hoja


class Puerta(Hoja):
    def __init__(self):
        super().__init__()
        self.lado1 = None
        self.lado2 = None
        self.abierta = True  # Las puertas comienzan abiertas

    def aceptar(self, visitor):
        visitor.visitar_puerta(self)

    def abrir(self):
        print("Puerta abierta")
        self.abierta = True

    def cerrar(self):
        print("Puerta cerrada")
        self.abierta = False

    def entrar(self, alguien):
        if self.abierta:
            print(f"{alguien} traspasa la puerta")
            # Determinar a cuál lado ir
            if alguien.posicion == self.lado1:
                self.lado2.entrar(alguien)
            elif alguien.posicion == self.lado2:
                self.lado1.entrar(alguien)
        else:
            print("La puerta está cerrada")

    def es_puerta(self):
        return True
