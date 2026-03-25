class Hoja(ElementoMapa):
    def recorrer(self, un_bloque):
        """unBloque value: self. Transcript show: self printString."""
        un_bloque(self)
        print(str(self))