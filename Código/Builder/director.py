class Director:
    def __init__(self):
        self.builder = None
        self.dict = None

    def leer_archivo(self, ruta_archivo):
        """Equivalente a STON fromString: jsonString"""
        import json
        with open(ruta_archivo, 'r') as f:
            self.dict = json.load(f)

    def ini_builder(self):
        """Decide qué builder usar según la forma definida en el archivo"""
        forma = self.dict.get('forma')
        if forma == 'poligono4':
            self.builder = LaberintoBuilder()
        elif forma == 'rombo':
            self.builder = LaberintoBuilderRombo()

    def fabricar_juego(self):
        self.builder.fabricar_juego()

    def fabricar_bichos(self):
        """Recorre la colección de bichos del diccionario"""
        bichos = self.dict.get('bichos', [])
        for each in bichos:
            self.builder.fabricar_bicho_modo_posicion(
                each.get('modo'), 
                each.get('posicion')
            )

    def fabricar_laberinto(self):
        self.builder.fabricar_laberinto()
        
        # Procesar habitaciones/armarios recursivamente
        elementos = self.dict.get('laberinto', [])
        for each in elementos:
            self.fabricar_laberinto_recursivo(each, 'root')

        # Procesar puertas
        puertas = self.dict.get('puertas', [])
        for each in puertas:
            # each es una lista: [lado1, or1, lado2, or2]
            self.builder.fabricar_puerta_l1_or1_l2_or2(
                each[0], each[1], each[2], each[3]
            )

    def fabricar_laberinto_recursivo(self, un_dic, padre):
        con = None
        tipo = un_dic.get('tipo')

        # Contenedores
        if tipo == 'habitacion':
            con = self.builder.fabricar_habitacion(un_dic.get('num'))
        elif tipo == 'armario':
            con = self.builder.fabricar_armario(un_dic.get('num'), padre)
        
        # Hojas
        elif tipo == 'bomba':
            con = self.builder.fabricar_bomba_en(padre)

        # Hijos (Recursión)
        hijos = un_dic.get('hijos', [])
        for hijo in hijos:
            self.fabricar_laberinto_recursivo(hijo, con)

    def obtener_juego(self):
        return self.builder.juego

    def procesar(self, ruta_archivo):
        """Flujo principal de construcción"""
        self.leer_archivo(ruta_archivo)
        self.ini_builder()
        self.fabricar_laberinto()
        self.fabricar_juego()
        self.fabricar_bichos()