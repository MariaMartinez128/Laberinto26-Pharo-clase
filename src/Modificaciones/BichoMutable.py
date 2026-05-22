class BichoMutable(Bicho):
    def cambiar_modo(self, nuevo_modo):
        print(f"{self} cambia de modo a {nuevo_modo}")
        self.modo = nuevo_modo
