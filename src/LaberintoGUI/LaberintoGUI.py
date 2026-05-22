class LaberintoGUI:
    def __init__(self):
        self.juego = None
        self.person = None
        self.win = None

    # ---------------------------
    # INICIO
    # ---------------------------
    def iniciar_juego(self):
        director = Director()

        ruta = r"C:\Users\usuario\source\repos\MariaMartinez128\Laberinto26-Pharo-clase\\"
        archivo = ruta + "laberinto.json"

        director.procesar(archivo)

        self.juego = director.obtener_juego()

        self.mostrar_laberinto()

        self.win = "Ventana: LaberintoGUI"
        print(self.win)

      
    # ---------------------------
    # DIBUJO
    # ---------------------------
    def calcular_posicion(self):
        pass

    def mostrar_laberinto(self):
        # pasos de renderizado l�gico
        self.calcular_posicion()

       
    # ---------------------------
    # GETTERS / SETTERS
    # ---------------------------
    def get_juego(self):
        return self.juego

    def set_juego(self, juego):
        self.juego = juego

    def get_person(self):
        return self.person

    def set_person(self, person):
        self.person = person

    def get_win(self):
        return self.win

    def set_win(self, win):
        self.win = win