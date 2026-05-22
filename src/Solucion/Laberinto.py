class Laberinto:
    """Clase que representa el laberinto completo"""
    
    def __init__(self):
        self.habitaciones = {}
    
    def agregar_habitacion(self, habitacion):
        self.habitaciones[habitacion.num] = habitacion
    
    def obtener_habitacion(self, num):
        return self.habitaciones.get(num)
    
    def __str__(self):
        return f"Laberinto con {len(self.habitaciones)} habitaciones"
