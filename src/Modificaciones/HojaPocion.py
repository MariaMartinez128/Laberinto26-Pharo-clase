from Solucion.Decorator import Decorator


class HojaPocion(Decorator):
    """Decorador para pociones - añade efecto visual"""
    
    def usar(self, personaje):
        print("✨ La poción brilla intensamente...")
        self.em.usar(personaje)

    def __str__(self):
        return f"{self.em} (decorada)"