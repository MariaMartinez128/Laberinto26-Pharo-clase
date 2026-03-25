class LaberintoBuilderRombo(LaberintoBuilder):
    def asignar_orientaciones(self, una_forma):
        """Sobrescribe para usar diagonales"""
        una_forma.agregar_orientacion(self.fabricar_noreste())
        una_forma.agregar_orientacion(self.fabricar_noroeste())
        una_forma.agregar_orientacion(self.fabricar_suroeste())
        una_forma.agregar_orientacion(self.fabricar_sureste())

    def fabricar_forma(self):
        forma = Rombo()
        self.asignar_orientaciones(forma)
        return forma