import json

class Director:
    def __init__(self):
        self.builder = None
        self.dict = None

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
        self.builder.fabricar_laberinto()

        for each in self.dict.get('laberinto', []):
            self.fabricar_laberinto_recursivo(each, "root")

        for each in self.dict.get('puertas', []):
            self.builder.fabricar_puerta_lado1(
                each[0], each[1],
                each[2], each[3]
            )

    def fabricar_laberinto_recursivo(self, un_dic, padre):
        tipo = un_dic.get('tipo')
