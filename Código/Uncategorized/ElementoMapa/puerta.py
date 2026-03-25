class Puerta(Hoja):
    def __init__(self):
        self.abierta = False
        self.lado1 = None
        self.lado2 = None

    def abrir(self):
        print(f"Abrimos {self}")
        self.abierta = True

    def cerrar(self):
        self.abierta = False

    def entrar(self, alguien):
        if self.abierta:
            # Lógica de cruzar la puerta
            if alguien.posicion == self.lado1:
                self.lado2.entrar(alguien)
            else:
                self.lado1.entrar(alguien)
        else:
            print("La puerta está cerrada")

    def es_puerta(self): return True