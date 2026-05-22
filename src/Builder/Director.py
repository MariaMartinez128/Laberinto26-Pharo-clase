import json
from Builder.LaberintoBuilder import LaberintoBuilder


class Director:
    def __init__(self):
        self.builder = None
        self.dict = None
        self.habitaciones = {}

    def procesar(self, archivo_json):
        with open(archivo_json, 'r', encoding='utf-8') as f:
            self.dict = json.load(f)
        
        self.fabricar_laberinto()
        self.fabricar_juego()
        self.fabricar_bichos()

    def obtener_juego(self):
        return self.builder.juego

    def fabricar_bichos(self):
        bichos = self.dict.get('bichos')
        if not bichos:
            return

        for each in bichos:
            self.builder.fabricar_bicho_modo_posicion(
                each['modo'],
                each['posicion']
            )

    def fabricar_juego(self):
        self.builder.fabricar_juego()

    def fabricar_laberinto(self):
        self.builder = LaberintoBuilder()
        self.builder.fabricar_laberinto()

        for each in self.dict.get('laberinto', []):
            hab = self.fabricar_laberinto_recursivo(each)
            self.builder.laberinto.agregar_habitacion(hab)

        for each in self.dict.get('puertas', []):
            self.builder.fabricar_puerta_lado1(
                each[0], each[1],
                each[2], each[3]
            )

    def fabricar_laberinto_recursivo(self, un_dic):
        tipo = un_dic.get('tipo')
        
        if tipo == "habitacion":
            num = un_dic.get('num')
            hab = self.builder.fabricar_habitacion(num)
            
            hijos = un_dic.get('hijos', [])
            for hijo_dic in hijos:
                tipo_hijo = hijo_dic.get('tipo')
                self.fabricar_hijo(hab, tipo_hijo)
            
            return hab
        
        return None

    def fabricar_hijo(self, habitacion, tipo):
        if tipo == "cofre":
            self.builder.fabricar_cofre_en(habitacion)
        elif tipo == "altar":
            self.builder.fabricar_altar_en(habitacion)
        elif tipo == "pocion_fuerza":
            self.builder.fabricar_pocion_fuerza_en(habitacion)
        elif tipo == "pocion_curacion":
            self.builder.fabricar_pocion_curacion_en(habitacion)
        elif tipo == "foso":
            self.builder.fabricar_foso_en(habitacion)
        elif tipo == "tunel":
            self.builder.fabricar_tunel_en(habitacion)
        elif tipo == "bomba":
            self.builder.fabricar_bomba_en(habitacion)
