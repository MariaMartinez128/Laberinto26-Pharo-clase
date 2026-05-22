class Cerrada(EstadoPuerta):
    def abrir(self, puerta):
        print(f"Abrimos {puerta}")
        puerta.estado = Abierta()

    def entrar(self, alguien, puerta):
        print(f"Puerta {puerta} cerrada")

    def esta_cerrada(self):
        return True
``