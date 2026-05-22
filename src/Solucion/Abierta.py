
class Abierta(EstadoPuerta):
    def cerrar(self, puerta):
        print(f"Cerramos {puerta}")
        puerta.estado = Cerrada()

    def entrar(self, alguien, puerta):
        puerta.puede_entrar(alguien)

    def esta_abierta(self):
        return True