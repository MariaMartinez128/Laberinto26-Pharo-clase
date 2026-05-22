import random


class GestorAmbiental:
    """Gestor de atmósfera y efectos ambientales del laberinto"""
    
    DESCRIPCIONES = {
        1: "La entrada principal del laberinto. Sientes una brisa fría que trae extraños aromas...",
        2: "Habitación con luz tenue. Los símbolos en las paredes parecen brillar...",
        3: "El aire es pesado aquí. Escuchas sonidos extraños en la oscuridad...",
        4: "Una cámara antigua y sagrada. Sientes la presencia de algo mágico...",
        5: "Un túnel serpentante lleno de misterio. El aire parece distorsionarse...",
        6: "Habitación peligrosa y amenazante. Algo no es seguro aquí..."
    }
    
    EFECTOS = [
        "Hace frío...",
        "Sientes un ambiente extraño...",
        "Huele a humedad...",
        "El silencio es inquietante...",
        "Escuchas ecos lejanos...",
        "Las sombras parecen moverse..."
    ]

    def describir_habitacion(self, numero_hab):
        desc = self.DESCRIPCIONES.get(numero_hab, "Una habitación misteriosa...")
        print(f"\n{desc}")

    def generar_efecto_aleatorio(self):
        return random.choice(self.EFECTOS)

    def describir_entrada(self, nombre_personaje):
        print("\n" + "="*60)
        print(f"🏰 BIENVENIDO AL LABERINTO 26, {nombre_personaje.upper()}")
        print("="*60)
        print(f"\n{self.generar_efecto_aleatorio()}\n")