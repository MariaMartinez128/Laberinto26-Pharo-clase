from Solucion.ElementoMapa import ElementoMapa

class Hoja(ElementoMapa):
    def recorrer(self, func):
        print(self)
        func(self)