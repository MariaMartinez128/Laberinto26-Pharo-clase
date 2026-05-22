class LaberintoBuilderRombo(LaberintoBuilder):

    def asignar_orientaciones(self, forma):
        forma.orientaciones.extend([
            self.fabricar_noreste(),
            self.fabricar_noroeste(),
            self.fabricar_sureste(),
            self.fabricar_suroeste()
        ])

    def fabricar_forma(self):
        forma = Rombo()
        self.asignar_orientaciones(forma)
        return forma