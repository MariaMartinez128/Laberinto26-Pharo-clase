class Hoja(ElementoMapa):
    def recorrer(self, func):
        print(self)
        func(self)