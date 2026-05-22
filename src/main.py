if __name__ == "__main__":
    director = Director()
    director.procesar("laberinto.json")

    juego = director.obtener_juego()
    juego.agregar_personaje("Maria")

    consola = ConsolaInteractiva(juego)
    consola.loop()
