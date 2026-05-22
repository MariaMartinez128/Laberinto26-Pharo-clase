class Altar(Contenedor):
    def aceptar_contenedor(self, visitor):
        pass

    def usar(self, personaje):
        print("Tocas el Altar...")
        personaje.poder += 2
        print("El espejo aumenta tu poder")
