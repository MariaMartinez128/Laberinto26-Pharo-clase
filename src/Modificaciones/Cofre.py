from Solucion.Contenedor import Contenedor


class Cofre(Contenedor):
    def aceptar_contenedor(self, visitor):
        # Patrón Visitor - opcional
        pass

    def usar(self, personaje):
        if self.hijos:
            obj = self.hijos.pop(0)
            print(f"\n📦 Abres el Cofre y encuentras: {obj}")
            obj.usar(personaje)
        else:
            print("\n📦 El Cofre está vacío")

    def __str__(self):
        return "Cofre"
