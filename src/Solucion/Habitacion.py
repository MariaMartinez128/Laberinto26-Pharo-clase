class Habitacion(Contenedor):
    def aceptar_contenedor(self, visitor):
        visitor.visitar_habitacion(self)

    def __str__(self):
        return f"Hab-{self.num}"