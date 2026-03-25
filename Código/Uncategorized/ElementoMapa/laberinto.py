class Laberinto(Contenedor):
    def agregar_habitacion(self, una_hab):
        self.agregar_hijo(una_hab)

    def entrar(self, alguien):
        print(f"{alguien} ha entrado en {self}")
        hab = self.obtener_habitacion(0) # Pharo usa 1, Python usa 0
        hab.entrar(alguien)

    def obtener_habitacion(self, un_num):
        return self.ems[un_num]

    def recorrer(self, un_bloque):
        print("Recorriendo el laberinto")
        for each in self.ems:
            each.recorrer(un_bloque)