class LaberintoBuilder:
    def __init__(self):
        self.laberinto = None
        self.juego = None

    # --- Factory Methods de Orientaciones ---
    def fabricar_norte(self): return Norte()
    def fabricar_sur(self): return Sur()
    def fabricar_este(self): return Este()
    def fabricar_oeste(self): return Oeste()
    def fabricar_noreste(self): return Noreste()
    def fabricar_noroeste(self): return Noroeste()
    def fabricar_sureste(self): return Sureste()
    def fabricar_suroeste(self): return Suroeste()

    # --- Factory Methods de Modos ---
    def fabricar_agresivo(self): return Agresivo()
    def fabricar_perezoso(self): return Perezoso()

    def asignar_orientaciones(self, una_forma):
        """Añade las 4 direcciones básicas"""
        una_forma.agregar_orientacion(self.fabricar_norte())
        una_forma.agregar_orientacion(self.fabricar_este())
        una_forma.agregar_orientacion(self.fabricar_sur())
        una_forma.agregar_orientacion(self.fabricar_oeste())

    def fabricar_forma(self):
        forma = Cuadrado()
        self.asignar_orientaciones(forma)
        return forma

    def fabricar_laberinto(self):
        self.laberinto = Laberinto()

    def fabricar_juego(self):
        self.juego = Juego()
        self.juego.laberinto = self.laberinto

    def fabricar_habitacion(self, un_num):
        hab = Habitacion()
        hab.num = un_num
        hab.forma = self.fabricar_forma()
        hab.forma.num = un_num
        
        # Llenar con paredes inicialmente
        for orientacion in hab.forma.orientaciones:
            hab.poner_en_elemento(orientacion, Pared())
            
        self.laberinto.agregar_habitacion(hab)
        return hab

    def fabricar_armario(self, un_num, un_cont):
        arm = Armario()
        arm.num = un_num
        arm.forma = self.fabricar_forma()
        arm.forma.num = un_num
        
        for orientacion in arm.forma.orientaciones:
            arm.poner_en_elemento(orientacion, Pared())
            
        pt = Puerta()
        pt.lado1 = arm
        pt.lado2 = un_cont
        
        arm.poner_en_elemento(self.fabricar_este(), pt)
        un_cont.agregar_hijo(arm)
        return arm

    def fabricar_bomba_en(self, un_cont):
        # Aquí el decorador envuelve a algo, o simplemente se añade
        bm = Bomba(Pared()) # Ejemplo: una pared con bomba
        un_cont.agregar_hijo(bm)
        return bm

    def fabricar_bicho_modo_posicion(self, str_modo, un_num):
        """Uso de getattr para imitar el perform: de Pharo"""
        # nombre_metodo = "fabricar_agresivo"
        nombre_metodo = f"fabricar_{str_modo.lower()}"
        metodo = getattr(self, nombre_metodo)
        modo = metodo()
        
        hab = self.juego.obtener_habitacion(un_num - 1)
        bicho = Bicho()
        bicho.modo = modo
        bicho.juego = self.juego
        
        hab.entrar(bicho)
        self.juego.bichos.append(bicho)
        return bicho

    def fabricar_puerta_l1_or1_l2_or2(self, num1, or1, num2, or2):
        pt = Puerta()
        lado1 = self.laberinto.obtener_habitacion(num1 - 1)
        lado2 = self.laberinto.obtener_habitacion(num2 - 1)
        
        pt.lado1 = lado1
        pt.lado2 = lado2
        
        # perform: or1 -> fabricar_norte
        metodo_or1 = getattr(self, f"fabricar_{or1.lower()}")
        metodo_or2 = getattr(self, f"fabricar_{or2.lower()}")
        
        obj_or1 = metodo_or1()
        obj_or2 = metodo_or2()
        
        lado1.poner_en_elemento(obj_or1, pt)
        lado2.poner_en_elemento(obj_or2, pt)