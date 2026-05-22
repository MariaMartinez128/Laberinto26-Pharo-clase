class LaberintoBuilder:
    def __init__(self):
        self.laberinto = None
        self.juego = None

    def asignar_orientaciones(self, forma):
        forma.orientaciones.extend([
            self.fabricar_norte(),
            self.fabricar_este(),
            self.fabricar_sur(),
            self.fabricar_oeste()
        ])

    def fabricar_laberinto(self):
        self.laberinto = Laberinto()

    def fabricar_juego(self):
        self.juego = Juego()
        self.juego.prototipo = self.laberinto
        self.juego.laberinto = self.juego.clonar()

    def fabricar_habitacion(self, num):
        hab = Habitacion()
        hab.num = num

        forma = self.fabricar_forma()
        hab.forma = forma
        forma.num = num

        for o in forma.orientaciones:
            hab.poner_en(o, self.fabricar_pared())

        self.laberinto.agregar_habitacion(hab)
        return hab

    def fabricar_armario(self, num, cont):
        arm = Armario()
        arm.num = num

        self.asignar_orientaciones(arm)

        for o in arm.orientaciones:
            arm.poner_en(o, self.fabricar_pared())

        pt = Puerta()
        pt.lado1 = arm
        pt.lado2 = cont

        arm.poner_en(self.fabricar_este(), pt)
        cont.agregar_hijo(arm)

        return arm

    def fabricar_bicho_modo_posicion(self, modo_str, num):
        metodo = getattr(self, f"fabricar_{modo_str}")
        modo = metodo()

        hab = self.juego.obtener_habitacion(num)

        bicho = Bicho(modo)
        hab.entrar(bicho)

        self.juego.agregar_bicho(bicho)
        bicho.juego = self.juego

    def fabricar_puerta_lado1(self, n1, o1, n2, o2):
        pt = Puerta()

        h1 = self.laberinto.obtener_habitacion(n1)
        h2 = self.laberinto.obtener_habitacion(n2)

        pt.lado1 = h1
        pt.lado2 = h2

        or1 = getattr(self, f"fabricar_{o1}")()
        or2 = getattr(self, f"fabricar_{o2}")()

        pt.agregar_comando(Abrir(pt))

        h1.poner_en(or1, pt)
        h2.poner_en(or2, pt)

    def fabricar_bomba_en(self, cont):
        bm = Bomba()
        cont.agregar_hijo(bm)
        return bm

    def fabricar_tunel_en(self, cont):
        tn = Tunel()
        cont.agregar_hijo(tn)
        return tn

    # -------- ORIENTACIONES --------
    def fabricar_norte(self): return Norte.default()
    def fabricar_sur(self): return Sur.default()
    def fabricar_este(self): return Este.default()
    def fabricar_oeste(self): return Oeste.default()

    def fabricar_noreste(self): return Noreste.default()
    def fabricar_noroeste(self): return Noroeste.default()
    def fabricar_sureste(self): return Sureste.default()
    def fabricar_suroeste(self): return Suroeste.default()

    def fabricar_pared(self): return Pared()

    # -------- MODOS --------
    def fabricar_agresivo(self): return Agresivo()
    def fabricar_perezoso(self): return Perezoso()

    # -------- FORMA --------
    def fabricar_forma(self):
        forma = Cuadrado()
        self.asignar_orientaciones(forma)
        return forma