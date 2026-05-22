from Solucion.Bicho import Bicho


class BichoMutable(Bicho):
    """Bicho especial que puede cambiar de modo durante la ejecución del juego"""
    
    def cambiar_modo(self, nuevo_modo):
        print(f"{self} cambia de modo a {nuevo_modo}")
        self.modo = nuevo_modo

    def __str__(self):
        return f"Bicho-Mutable-{self.modo}"
