import unittest
import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Builder.Director import Director
from Solucion.Juego import Juego
from Visitor.VistorAbrirPuertas import VistorAbrirPuertas
from Visitor.VisitorCerrarPuertas import VisitorCerrarPuertas


class LaberintoBuilderTest(unittest.TestCase):

    def setUp(self):
        self.director = Director()
        
        # Usar el archivo laberinto.json en la raiz del proyecto
        archivo = os.path.join(os.path.dirname(__file__), '..', '..', 'laberinto.json')
        
        self.director.procesar(archivo)

        self.dict = self.director.dict
        self.juego = self.director.obtener_juego()
        self.juego.agregar_personaje("Maria")

    # -------------------------
    # UTILIDADES
    # -------------------------
    def comprobar_habitacion(self, num):
        hab = self.juego.obtener_habitacion(num)
        self.assertEqual(hab.num, num)
        return hab

    def comprobar_armario(self, num, cont):
        arm = next((e for e in cont.hijos if e.es_armario()), None)
        self.assertTrue(arm.es_armario())
        return arm

    def comprobar_bomba_en(self, cont):
        bmb = next((e for e in cont.hijos if e.es_bomba()), None)
        self.assertTrue(bmb.es_bomba())
        self.comprobar_funcionamiento_bomba(bmb)

    def comprobar_funcionamiento_bomba(self, bomba):
        # hasta en Smalltalk estaba vac�o
        pass

    def comprobar_tunel_en(self, cont):
        tunel = next((e for e in cont.hijos if e.es_tunel()), None)
        self.assertTrue(tunel.es_tunel())
        self.assertIsNone(tunel.laberinto)
        self.comprobar_funcionamiento_tunel(tunel)

    def comprobar_funcionamiento_tunel(self, tunel):
        self.assertTrue(tunel.es_tunel())
        self.assertIsNone(tunel.laberinto)
        self.assertIsNotNone(self.juego.person)

        tunel.entrar(self.juego.person)

        self.assertIsNotNone(tunel.laberinto)
        self.assertEqual(
            self.juego.laberinto.numero_habitaciones(),
            tunel.laberinto.numero_habitaciones()
        )

    def comprobar_puerta(self, n1, o1, n2, o2):
        h1 = self.juego.obtener_habitacion(n1)
        h2 = self.juego.obtener_habitacion(n2)

        self.assertEqual(h1.num, n1)
        self.assertEqual(h2.num, n2)

        or1 = getattr(self.director.builder, f"fabricar_{o1}")()
        or2 = getattr(self.director.builder, f"fabricar_{o2}")()

        pt1 = h1.forma.obtener_elemento(or1)
        pt2 = h2.forma.obtener_elemento(or2)

        self.assertTrue(pt1.es_puerta())
        self.assertTrue(pt2.es_puerta())
        self.assertEqual(pt1, pt2)

        self.assertFalse(pt1.estado.esta_abierta())

    def comprobar_laberinto_recursivo(self, d, padre):
        tipo = d.get('tipo')
        cont = None

        if tipo == 'habitacion':
            cont = self.comprobar_habitacion(d['num'])

        elif tipo == 'armario':
            cont = self.comprobar_armario(d['num'], padre)

        elif tipo == 'bomba':
            self.comprobar_bomba_en(padre)

        elif tipo == 'tunel':
            self.comprobar_tunel_en(padre)

        for h in d.get('hijos', []):
            self.comprobar_laberinto_recursivo(h, cont)

    # -------------------------
    # TESTS
    # -------------------------
    def test_iniciales(self):
        self.assertIsNotNone(self.juego)
        self.assertIsNotNone(self.juego.laberinto)
        self.assertIsNotNone(self.juego.person)

    def test_laberinto(self):
        for each in self.dict.get('laberinto', []):
            self.comprobar_laberinto_recursivo(each, "root")

        for p in self.dict.get('puertas', []):
            self.comprobar_puerta(p[0], p[1], p[2], p[3])

    def test_puertas(self):
        puertas = set()

        def recoger(e):
            if e.es_puerta():
                puertas.add(e)

        self.juego.laberinto.recorrer(recoger)

        self.assertFalse(any(p.estado.esta_abierta() for p in puertas))

        self.juego.abrirPuertas()
        self.assertFalse(any(p.estado.esta_cerrada() for p in puertas))

        self.juego.cerrarPuertas()
        self.assertFalse(any(p.estado.esta_abierta() for p in puertas))

        una = next(iter(puertas))

        self.juego.person.posicion = una.lado1
        pos = self.juego.person.posicion

        una.entrar(self.juego.person)
        self.assertEqual(pos, self.juego.person.posicion)

        self.juego.abrirPuertas()
        una.entrar(self.juego.person)

        self.assertNotEqual(pos, self.juego.person.posicion)
        self.assertEqual(self.juego.person.posicion, una.lado2)

    def test_puertas_visitor(self):
        puertas = set()

        def recoger(e):
            if e.es_puerta():
                puertas.add(e)

        self.juego.laberinto.recorrer(recoger)

        self.assertFalse(any(p.estado.esta_abierta() for p in puertas))

        vab = VistorAbrirPuertas()
        self.juego.laberinto.aceptar(vab)

        self.assertFalse(any(p.estado.esta_cerrada() for p in puertas))

        vcb = VisitorCerrarPuertas()
        self.juego.laberinto.aceptar(vcb)

        self.assertFalse(any(p.estado.esta_abierta() for p in puertas))

    def test_gana_personaje(self):
        for b in self.juego.bichos:
            b.vidas = 0

        self.assertTrue(all(not b.esta_vivo() for b in self.juego.bichos))

    def test_ganan_bichos(self):
        # no implementado tambi�n en Smalltalk
        pass