class Cofre(Contenedor):
    def aceptar_contenedor(self, visitor):
        # opcional
        pass

    def abrir(self, personaje):
        if self.hijos:
            obj = self.hijos.pop()
            print(f"Has encontrado {obj}")
            obj.usar(personaje)
