class ConsolaInteractiva:

    def __init__(self, juego):
        self.juego = juego
        self.turno = 0

    def mostrar_estado(self):
        p = self.juego.person
        print(f"\n--- TURNO {self.turno} ---")
        print(f"{p} | Vidas: {p.vidas} | Poder: {p.poder}")
        print(f"Posición: {p.posicion}")

    def loop(self):
        while True:
            self.mostrar_estado()

            cmd = input("Acción (norte/sur/este/oeste/usar/salir): ")

            if cmd == "salir":
                print("Fin del juego")
                break

            elif cmd == "norte":
                Norte.default().caminar(self.juego.person)

            elif cmd == "sur":
                Sur.default().caminar(self.juego.person)

            elif cmd == "este":
                Este.default().caminar(self.juego.person)

            elif cmd == "oeste":
                Oeste.default().caminar(self.juego.person)

            elif cmd == "usar":
                pos = self.juego.person.posicion
                if hasattr(pos, "hijos") and pos.hijos:
                    obj = pos.hijos[0]
                    if hasattr(obj, "usar"):
                        obj.usar(self.juego.person)

            # bichos actúan
            for b in self.juego.bichos:
                if b.esta_vivo():
                    b.actua()

            self.turno += 1