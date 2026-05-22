class GestorAmbiental:

    def describir(self, habitacion):
        descs = [
            "Hace frío...",
            "Sientes un ambiente extraño...",
            "Huele a humedad...",
            "El silencio es inquietante..."
        ]
        import random
        print(random.choice(descs))