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

        ruta = r"C:\Users\Jose.Gallud\CloudStation\asignaturas\diseño de sofware\curso25-26\laberintos\\"
        archivo = ruta + "lab4hab4bm2bichosTunel.json"

        director.procesar(archivo)

        self.juego = director.obtener_juego()

        self.mostrar_laberinto()

        # Placeholder de ventana (luego puedes usar tkinter, pygame, etc.)
        self.win = "Ventana: LaberintoGUI"
        print(self.win)

        # Opcional
        # self.agregar_personaje("Pepín")
        # self.dibujar_laberinto()

    # ---------------------------
    # DIBUJO
    # ---------------------------
    def calcular_posicion(self):
        # A implementar: calcular posiciones relativas de habitaciones
        pass

    def mostrar_laberinto(self):
        # pasos de renderizado lógico
        self.calcular_posicion()

        # Comentados igual que en Smalltalk
        # self.normalizar()
        # self.calcular_dimensiones()
        # self.asignar_puntos_reales()

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