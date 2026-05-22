class VisitorCerrarPuertas(Visitor):
    def visitar_puerta(self, puerta):
        puerta.cerrar()