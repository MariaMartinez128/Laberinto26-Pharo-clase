class EstadoPuerta:
    def abrir(self, puerta): pass
    def cerrar(self, puerta): pass
    def entrar(self, alguien, puerta): raise NotImplementedError
    def esta_abierta(self): return False
    def esta_cerrada(self): return False
``