class HojaFoso(Decorator):
    def entrar(self, alguien):
        print("Has caído en un foso!")
        alguien.vidas -= 5
        self.em.entrar(alguien)