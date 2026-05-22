from Solucion.Decorator import Decorator


class HojaEspejo(Decorator):
    """Decorador para un espejo con propiedades mágicas"""
    
    def entrar(self, alguien):
        print("✨ Ves tu reflejo en el espejo mágico...")
        self.em.entrar(alguien)

    def __str__(self):
        return "Espejo"