from Solucion.Comando import Comando

class Abrir(Comando):
    def ejecutar(self, alguien):
        self.receptor.abrir()
