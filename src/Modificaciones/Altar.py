from Solucion.Contenedor import Contenedor


class Altar(Contenedor):
    def aceptar_contenedor(self, visitor):
        pass

    def usar(self, personaje):
        print("\n🔮 Tocas el Altar sagrado...")
        print("✨ El espejo mágico brilla intensamente...")
        personaje.poder += 2
        print(f"⚡ El espejo aumenta tu poder a {personaje.poder}")

    def __str__(self):
        return "Altar"
