class HojaEspejo(Decorator):
    def entrar(self, alguien):
        print("Ves tu reflejo en el espejo...")
        self.em.entrar(alguien)