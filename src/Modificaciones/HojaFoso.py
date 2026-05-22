from Solucion.Decorator import Decorator


class HojaFoso(Decorator):
    """Decorador para un foso - obstáculo peligroso"""
    
    def entrar(self, alguien):
        print("⚠️ ¡Has caído en un FOSO!")
        print("💥 Tomas daño al caer")
        alguien.vidas -= 5
        print(f"❤️ Vidas restantes: {alguien.vidas}")
        if not self.em:
            print("🪨 Te arrastras fuera del foso...")
        else:
            self.em.entrar(alguien)

    def __str__(self):
        return "Foso"