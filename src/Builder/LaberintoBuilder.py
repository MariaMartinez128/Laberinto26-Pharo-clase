from Solucion.Laberinto import Laberinto
from Solucion.Juego import Juego
from Solucion.Habitacion import Habitacion
from Solucion.Cuadrado import Cuadrado
from Solucion.Norte import Norte
from Solucion.Sur import Sur
from Solucion.Este import Este
from Solucion.Oeste import Oeste
from Solucion.Noreste import Noreste
from Solucion.Noroeste import Noroeste
from Solucion.Sureste import Sureste
from Solucion.Suroeste import Suroeste
from Solucion.Pared import Pared
from Solucion.Puerta import Puerta
from Solucion.Abrir import Abrir
from Solucion.Bicho import Bicho
from Solucion.Armario import Armario
from Solucion.Bomba import Bomba
from Solucion.Tunel import Tunel
from Solucion.Agresivo import Agresivo
from Solucion.Perezoso import Perezoso


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

    def fabricar_cofre_en(self, cont):
        from Modificaciones.Cofre import Cofre
        from Modificaciones.Pociones import PocionFuerza
        cofre = Cofre()
        cofre.agregar_hijo(PocionFuerza())
        cont.agregar_hijo(cofre)
        return cofre

    def fabricar_altar_en(self, cont):
        from Modificaciones.Altar import Altar
        altar = Altar()
        cont.agregar_hijo(altar)
        return altar

    def fabricar_pocion_fuerza_en(self, cont):
        from Modificaciones.Pociones import PocionFuerza
        pocion = PocionFuerza()
        cont.agregar_hijo(pocion)
        return pocion

    def fabricar_pocion_curacion_en(self, cont):
        from Modificaciones.Pociones import PocionCuracion
        pocion = PocionCuracion()
        cont.agregar_hijo(pocion)
        return pocion

    def fabricar_foso_en(self, cont):
        from Modificaciones.HojaFoso import HojaFoso
        foso = HojaFoso()
        cont.agregar_hijo(foso)
        return foso

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
    
    def fabricar_asustado(self):
        from Modificaciones.ModoAsustado import ModoAsustado
        return ModoAsustado()
    
    def fabricar_frenetico(self):
        from Modificaciones.ModoFrenetico import ModoFrenetico
        return ModoFrenetico()

    # -------- FORMA --------
    def fabricar_forma(self):
        forma = Cuadrado()
        self.asignar_orientaciones(forma)
        return forma