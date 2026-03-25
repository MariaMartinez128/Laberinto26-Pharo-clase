class Pared(Hoja):
    def entrar(self, alguien=None):
        if alguien:
            print(f"{alguien} se ha chocado con una pared")
        else:
            print("Has chocado con una pared")